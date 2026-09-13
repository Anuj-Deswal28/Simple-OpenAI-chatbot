from prompt import chat_template

from dotenv import load_dotenv
import streamlit as st

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()
model = ChatOpenAI()
st.header("Demo Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    try:
        with open("memory.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()

        for line in lines:
            line = line.strip()

            if line.startswith("Human:"):
                st.session_state.chat_history.append(
                    HumanMessage(content=line.replace("Human:", "", 1).strip())
                )

            elif line.startswith("AI:"):
                st.session_state.chat_history.append(
                    AIMessage(content=line.replace("AI:", "", 1).strip())
                )

    except FileNotFoundError:
        pass

query = st.text_input("Enter your query")

if st.button("Submit") and query:
    human_message = HumanMessage(content=query)
    st.session_state.chat_history.append(human_message)

    prompt = chat_template.invoke({
        "chat_history": st.session_state.chat_history,
        "topic": query
    })

    result = model.invoke(prompt)
    ai_message = AIMessage(content=result.content)
    st.session_state.chat_history.append(ai_message)

    with open("memory.txt", "a", encoding="utf-8") as f:

        f.write(f"Human: {query}\n")
        f.write(f"AI: {result.content}\n")

    st.write(result.content)