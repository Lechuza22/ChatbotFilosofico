import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

# ------------------------------
# CONFIGURACIÓN DE LA APP
# ------------------------------
st.set_page_config(page_title="📚 Chatbot Filosófico", page_icon="🧠")
st.title("📚 Chatbot sobre Historia de la Filosofía – Reale & Antiseri")
st.markdown("Consultá el contenido de los tres tomos del manual de Reale con ayuda de IA 🤖")

# ------------------------------
# CARGA DEL VECTORSTORE FAISS
# ------------------------------
@st.cache_resource
def cargar_vectorstore():
    embeddings = OpenAIEmbeddings()
    return FAISS.load_local("reale_faiss_index", embeddings, allow_dangerous_deserialization=True)

vectorstore = cargar_vectorstore()
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

# ------------------------------
# MODELO DE LENGUAJE
# ------------------------------
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.2)
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# ------------------------------
# INTERFAZ DEL CHATBOT
# ------------------------------
pregunta = st.text_input("💬 Hacé tu pregunta sobre los pensadores del manual:")

if pregunta:
    with st.spinner("Pensando la mejor respuesta..."):
        respuesta = qa_chain.run(pregunta)
        st.success("Respuesta:")
        st.markdown(respuesta)
