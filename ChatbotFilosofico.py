import streamlit as st
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

st.set_page_config(page_title="RealeGPT 📚", page_icon="🧠")

st.title("📚 RealeGPT - Filosofía Antigua y Medieval")
st.markdown("Hacé una pregunta sobre el pensamiento filosófico desde los griegos hasta la escolástica:")

# Carga la base vectorial
@st.cache_resource
def load_chain():
    embeddings = HuggingFaceEmbeddings()
    db = FAISS.load_local("vectordb", embeddings)
    chain = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model_name="gpt-3.5-turbo"),
        retriever=db.as_retriever()
    )
    return chain

qa_chain = load_chain()

# Interfaz de consulta
user_question = st.text_input("✍️ Escribí tu pregunta:")

if user_question:
    with st.spinner("Pensando..."):
        respuesta = qa_chain.run(user_question)
        st.markdown("### 🤖 Respuesta:")
        st.write(respuesta)
