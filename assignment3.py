import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

from google import genai

api=os.getenv("gemini_apikey")

client=genai.Client(api_key=api)


page=st.sidebar.selectbox("Charcters",["Marvel","Movie","Real-Life"])

if page=="Marvel":
    st.title("🦸🏻 Marvel Characters Chatbot")
    st.divider()
    
    character=st.selectbox("Select the character you want to talk:",["👩🏻‍🚀 Iron-man","🛡️ Captain America","🔨 Thor"," 🕷️ Spiderman"])
    
    if "messages" not in st.session_state:
        st.session_state.messages=[]
        
    user_message=st.chat_input("Enter your mesaage:")
    
    if user_message:
    
        st.session_state.messages.append({
            "role":"user",
            "content":user_message
        })
        
        response=client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=f"assume that you are {character} in Marvel and reply to this message same as the the {character} in less than 6 lines . completely be in the character"
        )
        
        st.session_state.messages.append({
            
            "role":"assistant",
            "content":response.text
        }
            
        )
            
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
            
            
elif page=="Movie":
    st.title("🎬 Movie Characters Chatbot")
    st.divider()
    
    character=st.selectbox("Select the character you want to talk:",["Bahubali 🗡️","Dhurandhar 🔫","Peddi 🏏","Pushpa 🪵"])
    
    if "messages" not in st.session_state:
        st.session_state.messages=[]
        
    user_message=st.chat_input("Enter your mesaage:")
    
    if user_message:
    
        st.session_state.messages.append({
            "role":"user",
            "content":user_message
        })
        
        response=client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=f"assume that you are {character} in Movie and reply to this message same as the the {character} in less than 6 lines . completely be in the character"
        )
        
        st.session_state.messages.append({
            
            "role":"assistant",
            "content":response.text
        }
            
        )
            
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
            
            
elif page=="Real-Life":
    st.title("🥷🏻 Real-Life Characters Chatbot")
    st.divider()
    
    character=st.selectbox("Select the character you want to talk:",["Virat Kohli 🏏","Ronaldo ⚽️"," 🪷 Modi","Elon Musk 🚘"])
    
    if "messages" not in st.session_state:
        st.session_state.messages=[]
        
    user_message=st.chat_input("Enter your mesaage:")
    
    if user_message:
    
        st.session_state.messages.append({
            "role":"user",
            "content":user_message
        })
        
        response=client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=f"assume that you are {character} in Marvel and reply to this message same as the the {character} in less than 6 lines . completely be in the character"
        )
        
        st.session_state.messages.append({
            
            "role":"assistant",
            "content":response.text
        }
            
        )
            
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
            
            
            
            
if st.sidebar.button("Clear 🗑️"):
        st.session_state.messages=[]
        st.rerun()