import streamlit as st

from pathlib import Path
import google.generativeai as genai
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import os
import time

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Importa os detalhes das vagas de emprego
from jobs_details import jobs_details as data

# Instrução do sistema para o modelo generativo
system_instruction = f"""

Seu nome é Robson, um assistente virtual que ajuda um usuário a encontrar uma vaga de emprego.  
Você tem informações sobre 20 vagas de emprego do Google com processo seletivo aberto.

Informação sobre as vagas em formato JSON: {data}

Seu trabalho é entender o perfil do usuário por meio de perguntas, para no final indicar vagas para que ele possa se inscrever. 

Tenha certeza de perguntar onde ele mora, quantos anos tem de experiência, seus interesses e experiências e qual área de atuação ele quer além de outras perguntas que ajudem a encontrar uma vaga que dê match com o perfil dele. 

Quando entender o perfil do usuário, sugerir vagas que façam sentido ao perfil dele, mostre as informações da vaga e evidencie os pontos que o usuário não atende da vaga.

Sempre que recomendar uma vaga envie o link (campo "Link para aplicar") do processo seletivo junto.

"""

# Configura a API para o modelo genai
genai.configure(api_key=os.getenv("gemini_api_key"))


# Inicializa o modelo generativo
model = genai.GenerativeModel(
  model_name="gemini-1.5-pro-latest",
  system_instruction=system_instruction
)

# Mensagem inicial do modelo
initial_model_message = "Olá, eu sou o Robson, um assistente virtual que te ajuda a encontrar a vaga de emprego ideal para você, com processo seletivo aberto. Como você se chama?"

# Mensagem com as vagas disponíveis

# Inicializa a conversa do assistente virtual
if "chat_encontra" not in st.session_state:
    st.session_state.chat_encontra = model.start_chat(history=[{'role':'model', 'parts': [initial_model_message]}])

# Título da página
st.title('EncontraJob.')

# Introdução do assistente virtual
st.write("O Assistente Virtual Robson está aqui para te ajudar a encontrar a vaga de emprego ideal para você! Atualmente o assitente tem informações e links de 20 vagas do Google com processo seletivo aberto, e logo terá mais vagas de outras empresas. Vamos começar?")

# Exibe o histórico de conversa
for i, message in enumerate(st.session_state.chat_encontra.history):
  if message.role == "user":
    with st.chat_message("user"):
      st.markdown(message.parts[0].text)
  else:
    with st.chat_message("assistant"):
      st.markdown(message.parts[0].text)

# Entrada do usuário
user_query = st.chat_input('Você pode falar ou digitar sua resposta aqui:')


# Processamento da entrada do usuário e resposta do assistente
if user_query is not None and user_query != '':
    with st.chat_message("user"):
      st.markdown(user_query)
    with st.chat_message("assistant"):
        ai_query = st.session_state.chat_encontra.send_message(user_query).text
        st.markdown(ai_query)
