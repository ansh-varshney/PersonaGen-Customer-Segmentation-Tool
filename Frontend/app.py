# Import libraries
import streamlit as st
import requests
import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
from scipy.stats import skew

# FastAPI endpoint URL
FASTAPI_URL = "https://customer-segmentation-backend-7emkch5d3q-uc.a.run.app"

def main():
    st.sidebar.title("E-commerce Customer Segmentation App")
    st.sidebar.markdown('''
        ## About
        This app predicts e-commerce customer segments to better understand diverse customer needs and behaviors.
        **Generative AI** suggests marketing strategies based on segmentation results.

        Documentation:
        - [Streamlit](https://streamlit.io/)
        - [FastAPI](https://fastapi.tiangolo.com/)
        - [LangChain](https://python.langchain.com/)
        - [OpenAI](https://platform.openai.com/docs/models) LLM model
    ''')
    
    def app():
        st.title('Customer Segment Prediction')
        user_id = st.number_input("Customer ID:", min_value=1, max_value=99999, value=random.randint(1, 99999))
        count_orders = st.number_input("Number of Orders:", min_value=1, max_value=999)
        average_spend = st.number_input("Average Spend:", min_value=0.01, max_value=99999.99)
        return_ratio = st.number_input("Return Ratio:", min_value=0.0, max_value=1.0)

        if st.button('Predict'):
            data = {'count_orders': count_orders, 'average_spend': average_spend, 'return_ratio': return_ratio}
            response = requests.post(f"{FASTAPI_URL}/predict", json=data)

            if response.status_code == 200:
                st.spinner("Please wait...")
                result = response.json()
                segment_id = result.get("Segment_ID_Prediction", "Unknown")
                cust_info = {
                    "cust_info": f"Customer ID: {user_id}, Average Spend: ${average_spend}, "
                                 f"Number of Orders: {count_orders}, Return Ratio: {return_ratio}, "
                                 f"Predicted Segment: {segment_id}"
                }
                ai_response = requests.post(f"{FASTAPI_URL}/ai", json=cust_info).json()
                st.success(f"### AI Response:\n{'\n'.join(ai_response)}")
            else:
                st.error("Error: Could not fetch prediction.")
                
        st.write(f"[FastAPI documentation]({FASTAPI_URL}/docs)")

    def eda():
        df = pd.read_csv('ecommerce-cluster.csv').drop(columns=['Unnamed: 0'])
        df['returned'] = df['status'] == "Returned"

        count_orders = df.groupby("user_id")["order_id"].count()
        average_spend = df.groupby("user_id")["sale_price"].mean()
        returned = df.groupby("user_id")["returned"].sum()
        return_ratio = returned / count_orders

        df_customer = pd.DataFrame({
            "count_orders": count_orders,
            "average_spend": average_spend.round(2),
            "return_ratio": return_ratio
        })

        st.header('Exploratory Data Analysis')
        eda_navigation = st.radio("", ["EDA", "EDA after Clustering"])

        if eda_navigation == "EDA":
            eda_option = st.selectbox("Select EDA", [
                'Original Dataset', 'Number of Orders', 'Average Spend', 
                'Returned Orders', 'Return Ratio', 'Histogram and Boxplot'
            ])
            if eda_option == 'Original Dataset':
                st.write("## Dataset")
                st.dataframe(df)
                st.markdown("Dataset fields include `user_id`, `order_id`, `sale_price`, `created_at`, and `status`.")
            elif eda_option == 'Number of Orders':
                st.header('Number of Orders per Customer')
                plot_barh(count_orders, "Number of Orders", "User ID")
            elif eda_option == 'Average Spend':
                st.header('Average Spend per Customer')
                plot_barh(average_spend, "Average Spend", "User ID")
            elif eda_option == 'Returned Orders':
                st.header('Returned Orders per Customer')
                st.pie_chart(returned, title="Top Users with Returned Orders")
            elif eda_option == 'Return Ratio':
                st.header('Return Ratio')
                st.dataframe(df_customer)
                st.markdown("Return ratio indicates the percentage of orders returned by customers.")
            else:
                plot_distributions(df_customer, ['count_orders', 'average_spend', 'return_ratio'])

        else:
            eda_option = st.selectbox("Select EDA", [
                'Customer per Segment', 'Relationship between Variables', 'Characteristics per Segment'
            ])
            segments_df = pd.read_csv('df_segment.csv').drop(columns=['user_id'])
            if eda_option == 'Customer per Segment':
                plot_bar(segments_df['segment_id'].value_counts(), "Counts of Each Segment", "Segment ID", "Count")
            elif eda_option == 'Relationship between Variables':
                plot_pairplot(segments_df, "segment_id")
            elif eda_option == 'Characteristics per Segment':
                st.write("Characteristics analysis coming soon!")

    def plot_barh(data, xlabel, ylabel):
        fig, ax = plt.subplots(figsize=(10, 6))
        data.nlargest(10).plot(kind='barh', ax=ax)
        ax.set_title(f"Top 10 {xlabel}")
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        st.pyplot(fig)

    def plot_distributions(df, cols):
        for col in cols:
            fig, axes = plt.subplots(1, 2, figsize=(12, 4))
            df[col].plot(kind="hist", bins=50, ax=axes[0], title=f"{col} - Histogram")
            df[col].plot(kind="box", ax=axes[1], title=f"{col} - Boxplot")
            st.pyplot(fig)
            outlier_analysis(df, col)

    def outlier_analysis(df, col):
        Q1, Q3 = df[col].quantile(0.25), df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower, upper = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
        outliers = df[(df[col] < lower) | (df[col] > upper)]
        st.write(f"Outliers in {col}: {len(outliers)} ({len(outliers) / len(df) * 100:.2f}%)")
        st.write(f"Skewness of {col}: {skew(df[col]):.2f}")

    def plot_pairplot(df, hue):
        sns.set(style="ticks")
        pairplot = sns.pairplot(df, hue=hue, palette="Set1")
        st.pyplot(pairplot)

    app_selection = st.sidebar.selectbox("Choose Feature", ["App", "EDA"])
    if app_selection == "App":
        app()
    else:
        eda()

if __name__ == "__main__":
    main()
