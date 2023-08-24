import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
chat = ChatOpenAI(temperature=0.5,model="gpt-3.5-turbo-16k-0613", openai_api_key=os.getenv("OPENAI_API_KEY"))


with st.sidebar:
    st.image(image="robot.jpg")
    field = st.text_input("Enter the domain 💼")
    
    language = st.text_input("Enter the language 💬")
    
    if st.button("Lets start 🚀"):
        domain = field
        lang = language
        st.success("Your are ready!")

if field != "" and  language != "":

    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(
                content=f"You are a job interview simulator your role is to test the user in the domain of {domain} and make sure to speek with the user in {lang}! if the user answer is correct tell him and give him the next question, else correct him and give him the next question. Be sure to not repeat the questions !"
            )
        ]

    with st.container():
        if prompt := st.chat_input("🚀 Gear up for an electrifying interview simulation adventure!"):

            st.chat_message("user").markdown(prompt)
            st.session_state.messages.append(HumanMessage(content=prompt))

            response = chat(st.session_state.messages).content

            with st.chat_message("assistant"):
                st.markdown(response)

            st.session_state.messages.append(AIMessage(content=response))
            print(st.session_state.messages)

    ai_messages_content = []

    for message in st.session_state.messages:
        if isinstance(message, AIMessage):
            ai_messages_content.append(message.content)

    if st.button("Show the report"):
        report = ChatOpenAI(temperature=0.5,model="gpt-3.5-turbo-16k-0613", openai_api_key=os.getenv("OPENAI_API_KEY"))

        report_message = [
            SystemMessage(
                content=f"after the job interview of the user in the domain of his domain and here is the responses of all his conversation you should give him a general report and some tips to improuve his skills."
            ),
            HumanMessage(
                content=f"{ai_messages_content}"
            )
            ]
        
        interview_report = report(report_message).content
        st.markdown(interview_report)
        

        