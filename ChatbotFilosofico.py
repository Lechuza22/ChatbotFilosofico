import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

# 1. Carga de datos
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
loader = TextLoader("manual_completo_reale.txt")
docs = loader.load()

# 2. Chunking
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
chunks = splitter.split_documents(docs)

# 3. Embeddings + Vector Store (FAISS)
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings()
vectorstore = FAISS.from_documents(chunks, embeddings)

# 4. Pregunta-respuesta
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model="gpt-3.5-turbo"),  # o GPT-4 si lo tenés habilitado
    retriever=vectorstore.as_retriever()
)

# 5. Interfaz simple con Streamlit
import streamlit as st

st.title("🤖 RealeGPT - Filosofía Antigua")
query = st.text_input("Preguntame algo sobre filosofía griega, platónica o medieval:")
if query:
    respuesta = qa_chain.run(query)
    st.write(respuesta)
        st.markdown(respuesta)
