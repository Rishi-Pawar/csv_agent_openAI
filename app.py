import streamlit as st
from langchain_experimental.agents import create_csv_agent
# from langchain.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
import os

Set OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY", None)

if not openai_api_key:
    st.error("Please set the `OPENAI_API_KEY` as an environment variable or pass it directly in the code.")
    st.stop()

# Load Titanic dataset and create an agent
csv_path = "titanic.csv"  # Path to your Titanic CSV file
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, openai_api_key=openai_api_key)

# Create the CSV agent
agent = create_csv_agent(llm=llm, path=csv_path, allow_dangerous_code=True, verbose=True)

# Streamlit interface
st.title("CSV Agent for Titanic Dataset")
st.write("Ask any question about the Titanic dataset!")

query = st.text_input("Enter your question:")

if query:
    with st.spinner("Processing your question..."):
        try:
            # Use the agent to answer the query
            response = agent.invoke(query)
            st.write("### Response:")
            st.write(response)
        except Exception as e:
            st.error(f"Error processing the query: {e}")



