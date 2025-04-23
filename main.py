import spacy
import streamlit as st

# modelo en español
nlp = spacy.load("es_core_news_md")

# Dividir en párrafos
with open("manual_completo_reale.txt", "r", encoding="utf-8") as f:
    fragments = f.read().split("\n\n")

st.title("💬 Consulta filosófica con spaCy")
query = st.text_input("Escribí tu pregunta")

if query:
    doc_query = nlp(query)
    results = []

    for frag in fragments:
        frag_doc = nlp(frag)
        score = doc_query.similarity(frag_doc)
        results.append((frag, score))

    # Ordenar por mayor similitud
    results.sort(key=lambda x: x[1], reverse=True)
    for res, score in results[:3]:
        st.markdown(f"📖 Fragmento (similitud {score:.2f}):\n\n{res[:400]}...")
