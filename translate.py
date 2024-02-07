#from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
from langchain_community.chat_models import AzureChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate


## Function to load OpenAI model and get respones

def get_openai_response(question):
    azure_openai_api_key = os.getenv("AZURE_OPENAI_API_KEY")
    azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")

    llm = AzureChatOpenAI(
    openai_api_version=os.getenv("OPENAI_API_VERSION"),
    azure_deployment="gpt-35-turbo",
    )

    template='you are an assistant in translating the contents from english to Tamil'
    human_template="{question}"

    chatprompt= ChatPromptTemplate.from_messages([("system",template),("human",human_template)])
    chain= chatprompt|llm
    
    response=chain.invoke({"question":question})
    
    
    
    return response.content


## initialize streamlit app

st.set_page_config(page_title="Translation bot")

st.header("Translation Langchain Application")

input=st.text_input("Enter the sentence in English: ",key="input")
response= get_openai_response(input)

submit= st.button("Translate")


if submit:
    st.subheader("The translated response in Tamil ")
    st.write(response)
