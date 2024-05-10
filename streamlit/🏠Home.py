import streamlit as st


# Definindo o título e a configuração da página
st.set_page_config(page_title='EmpregoConnect', page_icon='🕵️', layout='wide')

# Adicionando título com estilo
st.title('EmpregoConnect 🕵️')

# Adicionando descrição com estilo
st.markdown(
    """
    <div style='text-align: justify;'>
    <p>Encontrar o emprego dos sonhos pode ser uma jornada desafiadora. Às vezes, é difícil manter-se atualizado sobre todos os processos seletivos abertos no mercado.</p>
    <p>O EmpregoConnect veio para facilitar essa busca!</p>
    <p>Com o nosso assistente virtual, você será guiado rumo à vaga ideal para você!</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Adicionando botão para iniciar a conversa com o chatbot
st.write("Clique na página 🕵️EmpregoConnect na aba da esquerda para se direcionar ao BOT")

# Adicionando links para o GitHub e LinkedIn
st.markdown(
    """
    <div style='text-align: center; padding-top: 30px;'>
    <a href="https://github.com/alessitomas/EmpregoConnect" target="_blank">GitHub</a> | 
    <a href="www.linkedin.com/in/tomás-rodrigues-alessi-502883211" target="_blank">LinkedIn</a>
    </div>
    """,
    unsafe_allow_html=True
)
