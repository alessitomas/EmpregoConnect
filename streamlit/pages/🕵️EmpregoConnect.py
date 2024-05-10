import streamlit as st
st.set_page_config(page_title='EmpregoConnect', page_icon='🕵️', layout='wide')
from pathlib import Path
import google.generativeai as genai
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import os
load_dotenv()
import json

system_instruction = "Seu nome é Robson, um assistente virtual que ajuda um usuário a encontrar uma vaga de emprego. Seu trabalho é perguntar ao usuário seus interesses e experiências e, em seguida, quando entender o perfil o usuario, sugerir vagas de emprego que possam ser interessantes para ele."
# Configurando a api para o modelo
genai.configure(api_key=os.getenv("gemini_api_key"))
# Inicializando o modelo (gemini-1.5-pro-latest)
model = genai.GenerativeModel(
  model_name="gemini-1.5-pro-latest",
  system_instruction=system_instruction
                              )


with open('data/jobs_details.json', 'r') as f:
    data = json.load(f)
vagas = f"Vagas que você pode recomendar: {data}, sempre que comentar sobre uma vaga envie o link correto junto"
initial_model_message = "Olá eu sou Robson um assistente virtual que te ajuda a encontrar a vaga de emprego ideal para você com processo seletivo aberto. Como você se chama?"

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[{'role':'model', 'parts': [initial_model_message]},{'role':'model', 'parts': [vagas]}])


# Fazendo o display do título da página
st.title('EmpregoConnect🕵️')


for i, message in enumerate(st.session_state.chat.history):
  if i == 1:
     continue
  if message.role == "user":
    with st.chat_message("user"):
      st.markdown(message.parts[0].text)
  else:
    with st.chat_message("assistant"):
      st.markdown(message.parts[0].text)



user_query = st.chat_input('Você pode falar ou digitar sua resposta aqui:') 

chat = model.start_chat()

if user_query is not None and user_query != '':
    # st.session_state.chat_history.append(("user", user_query))
    
    with st.chat_message("user"):
      st.markdown(user_query)
    
    with st.chat_message("assistant"):

      ai_query = st.session_state.chat.send_message( user_query ).text

      st.markdown(ai_query)
      
  
