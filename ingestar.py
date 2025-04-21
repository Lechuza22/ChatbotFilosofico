from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Carga y divide el texto
loader = TextLoader("manual_completo_reale.txt")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
chunks = splitter.split_documents(docs)

# Usa embeddings de HuggingFace
embedding = HuggingFaceEmbeddings()

# Crea y guarda la base vectorial
db = FAISS.from_documents(chunks, embedding)
db.save_local("vectordb")
print("✅ Base vectorial guardada en 'vectordb'")
