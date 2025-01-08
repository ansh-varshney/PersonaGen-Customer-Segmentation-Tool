from langchain_google_vertexai import ChatVertexAI
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Initialize the Google Vertex AI model
model = ChatVertexAI(model="gemini-1.5-flash",project="gen-lang-client-0540753381")

# Define the prompt template
prompt = """
You're a creative brand strategist, given the following customer information, come up with next marketing strategy based on AI generated response, explained step by step.

Customer Information:
{cust_info}

Customer Information:
{ai_response}

Your Response:
* Predicted Segment:
* Next Marketing Strategy:
"""

# Define the chain function (this replaces LLMChain)
def chain(customer_details):
    # Set up the request to the AI model
    response = model.invoke(customer_details)
    return response

# Example usage of the chain function
customer_info = "Sample customer details go here."
response = chain(customer_info)
print(response)
