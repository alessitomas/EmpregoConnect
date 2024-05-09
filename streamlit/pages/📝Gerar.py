import streamlit as st
from pathlib import Path
import google.generativeai as genai
from dotenv import load_dotenv
from streamlit_mic_recorder import mic_recorder
import os


st.set_page_config(page_title='Agente de Viagem', page_icon='', layout='wide')

load_dotenv()
genai.configure(api_key=os.getenv("gemini_api_key"))

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
    st.session_state.chat_history.append( ("assistant", ("Olá sou o Robson e serei seu agente de viagem, como você se chama?")))

st.title('Simulação de um processo seletivo')

for role, message in st.session_state.chat_history:
  if role == "user":
    with st.chat_message("user"):
      st.markdown(message)
  else:
    with st.chat_message("assistant"):
      st.markdown(message)


user_query = st.chat_input('Você pode falar ou digitar sua resposta aqui:') 


if user_query is not None and user_query != '':
    st.session_state.chat_history.append(("user", user_query))
    
    with st.chat_message("user"):
      st.markdown(user_query)
    
    with st.chat_message("assistant"):
      ai_query = "Hello Ber"
      st.markdown(ai_query)

    st.session_state.chat_history.append(("assistant", ai_query))

# audio = mic_recorder(
#     start_prompt="Start recording",
#     stop_prompt="Stop recording",
#     just_once=False,
#     use_container_width=False,
#     callback=None,
#     args=(),
#     kwargs={},
#     key=None
# )

# if audio:
#     st.audio(audio["bytes"], format="audio/wav")
    # if st.button('Gerar Prontuário Eletrônico Médico'):
    #     with st.chat_message("assistant"):
    #         for chunk in get_response():
    #             st.markdown(chunk.text)
    #     st.success('A transcrição foi feita com sucesso')