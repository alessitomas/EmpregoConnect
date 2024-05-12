import streamlit as st


# Adicionando título 
st.title('EmpregoConnect 🚀')

# Adicionando descrição do projeto
st.write("Conseguir um emprego que combine com você é um processo desafiador que exige tempo e dedicação. O EmpregoConnect é uma plataforma com 3 assistentes virtuais que te ajudam em todas as etapas desse processo.")

# Adicionando as etapas do projeto
etapas = [
    {
        "nome": "Encontrar uma Vaga",
        "icone": "🕵️",
        "descricao": "Encontre uma vaga com processo seletivo aberto que faça sentido para você, com base nas suas experiências e interesses.",
        "pagina": "[EncontraJob](https://empregoconnect.streamlit.app/EncontraJob)"
    },
    {
        "nome": "Preparar para Entrevista",
        "icone": "🥋",
        "descricao": "Prepare-se para a entrevista de emprego da vaga que você deseja, simulando perguntas de um processo seletivo.",
        "pagina": "[PreparoSoftSkills](https://empregoconnect.streamlit.app/PreparoSoftSkills)"
    },
    {
        "nome": "Produzir Currículo",
        "icone": "📄",
        "descricao": "Produza um currículo que destaque suas habilidades e experiências para determinada vaga.",
        "pagina": "[ProducaoCurriculo](https://empregoconnect.streamlit.app/ProducaoCurriculo)"
    }
]

# Adicionando as etapas como seções
for etapa in etapas:
    st.header(f"{etapa['icone']} {etapa['nome']}")
    st.write(etapa['descricao'])
    st.markdown(f"**Página da solução:** {etapa['pagina']}")
