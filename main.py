
import re
import streamlit as st
import time

st.title("Say Hello to Gaurav ChatAssist 👋")
def getoutput(user_input):
    response_patterns = {
        r'hi|hello': "Hello Fellow Human! How can I help you with today?",
        r'who are you': "I'm just a bunch of code written in python, but I'm doing great! How about you?",
        r'what is your name': "I'm a chatAssist Linus",
        r'bye|exit|quit': "Goodbye! Have a great day!",
        r'Who created you': "Gaurav created me, He's a great guy !!",
        r'how are you':"I am just fine, how about you ",
        r'I am fine | I am good':"Thats great !!👌👌"
    }

    for pattern, response in response_patterns.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response

    return "I'm sorry, I don't understand that. Can you please rephrase? ＞﹏＜"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


prompt = st.chat_input("what's up?")

if prompt:
    

    st.session_state.messages.append({"role":"user","content": prompt})
    
    with st.chat_message(name = "user",avatar= '🧑‍🦱'):
        st.markdown(prompt)

    time.sleep(0.7)
   
    with st.chat_message(name = "bot",avatar= '🤖'):
        response = getoutput(prompt)
        st.markdown(response)
    st.session_state.messages.append({"role":"bot ", "content" : response})




