# PersonaGen 
**Customer Segmentation and Strategy Application**  

Empower your business with data-driven customer segmentation and AI-generated strategies for engagement!  

---

## Overview  
PersonaGen is a cutting-edge tool designed for businesses to:  

- **Predict customer segments** using behavioral and transactional data.  
- **Generate AI-powered strategies** for personalized engagement, leveraging state-of-the-art technologies.  

By utilizing machine learning, clustering techniques, and generative AI, PersonaGen empowers businesses to enhance customer experiences and optimize decision-making processes.  

---

## Features  
- **Customer Segmentation**: Classify customers into distinct segments using clustering techniques.  
- **AI Strategy Generation**: Craft personalized, actionable strategies powered by advanced generative AI.  
- **REST API**: Seamlessly integrate customer insights into other business applications.  
- **Scalable and Portable**: Dockerized for easy deployment across multiple environments.  
- **Cloud Integration**: Enhanced performance with Google Vertex AI for generative AI tasks.  

---

## Technologies Used  
- **Python **: Backend development  
- **FastAPI **: High-performance API framework for building RESTful services  
- **LangChain **: Facilitates natural language understanding and AI-driven workflows  
- **Google Vertex AI **: Cloud-based infrastructure for generative AI and model management  
- **Pandas **: Data preprocessing and manipulation  
- **K-Means Clustering **: Machine learning technique for customer segmentation  
- **Custom ML Model **: Trained to predict customer segments effectively  
- **Docker **: Containerization for simplified deployment and scalability  

---

## API Endpoints  

### Home Endpoint  
- **Method**: `GET`  
- **URL**: `/`  
- **Description**: Verifies the service is live.  

### Predict User Segment  
- **Method**: `POST`  
- **URL**: `/predict`  
- **Description**: Predicts the customer segment based on behavioral data (e.g., order count, average spend, return ratio).  

### Generate Strategy  
- **Method**: `POST`  
- **URL**: `/ai`  
- **Description**: Generates an AI-driven strategy tailored to customer details, leveraging LangChain and Google Vertex AI.  

---

## Use Cases  
1. **Targeted Marketing Campaigns**: Craft customized marketing efforts for specific customer clusters.  
2. **Customer Retention**: Identify customers at risk of churn and provide timely, personalized offers.  
3. **Business Analytics**: Gain deeper insights into customer behavior to refine business strategies.  
4. **Customer Experience Enhancement**: Use generative AI to create unique engagement strategies, meeting diverse customer needs.  

---

## Machine Learning Techniques  
- **K-Means Clustering**: Used for grouping customers into meaningful segments based on behavioral data.  
- **Custom Predictive Models**: Built to predict customer segments using input features like order count, average spend, and return ratio.  
- **Generative AI**: Deployed through LangChain and Google Vertex AI for context-aware strategy generation.  

---

## Deployment  
PersonaGen is containerized using **Docker** for streamlined deployment across local and cloud-based environments, ensuring portability and scalability.  

---

## Credits  
The `model.pkl`, `df_segment.csv`, `ecommerce-cluster.csv`, `df_customer.csv`, and project architecture used have been adapted from the [ahmadluay9 GitHub repository: Generative-AI-for-Personalized-E-commerce-Customer-Segmentation](https://github.com/ahmadluay9/Generative-AI-for-Personalized-E-commerce-Customer-Segmentation).  
