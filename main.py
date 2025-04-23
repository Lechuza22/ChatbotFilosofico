from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# 1. Cargás tu texto y lo partís en párrafos o fragmentos
with open("manual_completo_reale.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()
fragments = raw_text.split("\n\n")  # podés mejorar esta separación

# 2. Interfaz Streamlit
st.title("🔍 Consulta Filosófica (TF-IDF)")
query = st.text_input("¿Qué querés preguntar?")

# 3. TF-IDF + Cosine
if query:
    corpus = fragments + [query]
    vectorizer = TfidfVectorizer().fit_transform(corpus)
    sim_scores = cosine_similarity(vectorizer[-1], vectorizer[:-1])
    top_idx = sim_scores.argsort()[0][-3:][::-1]  # top 3
    for idx in top_idx:
        st.markdown(f"📌 Fragmento relevante:\n\n{fragments[idx][:100000]}...")
