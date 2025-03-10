import streamlit as st
import openai
import pandas as pd
import plotly.express as px
import os

# Configuración de la API de OpenAI desde variable de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

def obtener_respuesta(mensaje):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": mensaje}]
    )
    return response["choices"][0]["message"]["content"]

# Configuración de la aplicación Streamlit
st.set_page_config(page_title="Chat Filosófico", layout="wide")
st.title("Chat Filosófico")

# Menú de opciones
menu = st.sidebar.radio("Menú", ["Chatbot", "Filósofos Antiguos", "Línea Temporal"])

if menu == "Chatbot":
    st.header("Chatbot Filosófico")
    mensaje_usuario = st.text_input("Escribe tu pregunta filosófica:")
    if st.button("Enviar"):
        if mensaje_usuario:
            respuesta = obtener_respuesta(mensaje_usuario)
            st.write("**Chatbot:**", respuesta)
        else:
            st.warning("Por favor, escribe una pregunta.")

elif menu == "Filósofos Antiguos":
    st.header("Filósofos de la Antigüedad")
    
    filosofos = {
        "Tales de Mileto": {
            "Biografía": "[Tales de Mileto](https://es.wikipedia.org/wiki/Tales_de_Mileto) fue un filósofo presocrático griego (c. 624-546 a.C.), considerado el primer filósofo de la historia occidental y uno de los Siete Sabios de Grecia.",
            "Obras": "No dejó textos escritos, pero sus ideas fueron transmitidas por sus discípulos.",
            "Ideas": [
                "El agua es el principio de todas las cosas.",
                "La Tierra flota sobre el agua.",
                "Todo está lleno de dioses (concepto de animismo).",
                "La observación de la naturaleza permite conocer sus leyes.",
                "Predijo un eclipse solar con exactitud."
            ]
        },
        "Anaximandro": {
            "Biografía": "[Anaximandro](https://es.wikipedia.org/wiki/Anaximandro) (c. 610-546 a.C.) fue un filósofo presocrático discípulo de Tales, que desarrolló la idea del 'ápeiron', un principio infinito e indeterminado como origen del universo.",
            "Obras": "Escribió un tratado llamado 'Sobre la Naturaleza', del cual solo quedan fragmentos.",
            "Ideas": [
                "El ápeiron es el principio de todas las cosas.",
                "La evolución de los seres vivos proviene del agua.",
                "La Tierra es un cilindro suspendido en el espacio.",
                "Las leyes naturales regulan el cosmos.",
                "El universo es infinito y eterno."
            ]
        },
        "Sócrates": {
            "Biografía": "[Sócrates](https://es.wikipedia.org/wiki/S%C3%B3crates) (470-399 a.C.) fue un filósofo ateniense, considerado uno de los fundadores de la filosofía occidental. No dejó escritos, y su pensamiento fue recogido por Platón y Jenofonte.",
            "Obras": "No dejó obras escritas, su pensamiento fue registrado en los diálogos de Platón.",
            "Ideas": [
                "El conocimiento es virtud.",
                "La mayéutica: el conocimiento surge del diálogo.",
                "Conócete a ti mismo.",
                "La ética es fundamental para la vida humana.",
                "Fue condenado a muerte por cuestionar las creencias de Atenas."
            ]
        },
        "Platón": {
            "Biografía": "[Platón](https://es.wikipedia.org/wiki/Plat%C3%B3n) (427-347 a.C.) fue un filósofo griego, discípulo de Sócrates y maestro de Aristóteles. Fundó la Academia de Atenas, la primera institución de educación superior de Occidente.",
            "Obras": "Entre sus obras más importantes están *La República*, *El Banquete* y *Fedón*.",
            "Ideas": [
                "Teoría de las Ideas: el mundo sensible es una copia imperfecta del mundo de las Ideas.",
                "El alma es inmortal y preexistente.",
                "El conocimiento es reminiscencia de las Ideas.",
                "El Estado ideal se basa en la justicia y la filosofía.",
                "Criticó la democracia ateniense y defendió el gobierno de los sabios."
            ]
        },
        "Aristóteles": {
            "Biografía": "[Aristóteles](https://es.wikipedia.org/wiki/Arist%C3%B3teles) (384-322 a.C.) fue un filósofo griego, discípulo de Platón y maestro de Alejandro Magno. Fundó el Liceo y desarrolló un sistema filosófico que influyó profundamente en la ciencia y la lógica.",
            "Obras": "Algunas de sus obras más importantes incluyen *Ética a Nicómaco*, *Metafísica* y *Política*.",
            "Ideas": [
                "La sustancia es la combinación de materia y forma.",
                "La lógica como herramienta del conocimiento.",
                "El ser humano es un animal político.",
                "El conocimiento se obtiene a través de la experiencia.",
                "La ética de la virtud se basa en el término medio."
            ]
        }
    }
    
    seleccion = st.selectbox("Selecciona un filósofo", list(filosofos.keys()))
    
    if seleccion:
        imagen_path = os.path.join("imagenes", f"{seleccion}.jpg")
        if os.path.exists(imagen_path):
            st.image(imagen_path, caption=seleccion, use_column_width=True)
        
        st.subheader("Biografía")
        st.markdown(filosofos[seleccion]["Biografía"])
        
        st.subheader("Obras Principales")
        st.markdown(filosofos[seleccion]["Obras"])
        
        st.subheader("Principales Ideas")
        st.markdown("\n".join([f"- {idea}" for idea in filosofos[seleccion]["Ideas"]]))
