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
        "Pitágoras": {
            "Biografía": "[Pitágoras](https://es.wikipedia.org/wiki/Pit%C3%A1goras) (c. 570-495 a.C.) fue un filósofo y matemático griego, fundador de la escuela pitagórica, que creía en la relación entre las matemáticas y la realidad.",
            "Obras": "No dejó escritos, su pensamiento fue transmitido por sus seguidores.",
            "Ideas": [
                "Los números son la esencia de todas las cosas.",
                "El universo sigue un orden matemático.",
                "El alma es inmortal y transmigra.",
                "La música tiene bases matemáticas.",
                "La armonía rige la naturaleza."
            ]
        },
        "Epicuro": {
            "Biografía": "[Epicuro](https://es.wikipedia.org/wiki/Epicuro) (341-270 a.C.) fue un filósofo griego fundador del epicureísmo, que defendía la búsqueda del placer moderado y la ausencia de dolor como clave para la felicidad.",
            "Obras": "Algunas de sus obras más importantes son *Carta a Meneceo* y *Máximas capitales*.",
            "Ideas": [
                "El placer es el bien supremo.",
                "El miedo a los dioses es infundado.",
                "La muerte no debe ser temida.",
                "La amistad es esencial para la felicidad.",
                "La tranquilidad del alma se logra evitando deseos innecesarios."
            ]
        },
        "Diógenes": {
            "Biografía": "[Diógenes de Sinope](https://es.wikipedia.org/wiki/Diógenes_de_Sinope) (c. 412-323 a.C.) fue un filósofo cínico que despreciaba las convenciones sociales y promovía una vida sencilla y autosuficiente.",
            "Obras": "No dejó escritos, sus ideas fueron transmitidas por anécdotas y relatos de sus contemporáneos.",
            "Ideas": [
                "El desprecio por las normas sociales.",
                "La autosuficiencia es clave para la felicidad.",
                "Los deseos deben ser reducidos al mínimo.",
                "El verdadero sabio vive en armonía con la naturaleza.",
                "La virtud es más importante que la riqueza o el poder."
            ]
        },
        "Plotino": {
            "Biografía": "[Plotino](https://es.wikipedia.org/wiki/Plotino) (205-270 d.C.) fue un filósofo neoplatónico que desarrolló una visión mística del universo basada en la emanación del Uno.",
            "Obras": "Su obra principal es *Las Enéadas*, recopilada por su discípulo Porfirio.",
            "Ideas": [
                "El Uno es la fuente de todo ser.",
                "El alma busca reunirse con el Uno.",
                "La realidad se estructura en niveles de emanación.",
                "La materia es la forma más baja de existencia.",
                "La contemplación es el camino a la verdad."
            ]
        },
        "Galeno": {
            "Biografía": "[Galeno](https://es.wikipedia.org/wiki/Galeno) (129-216 d.C.) fue un médico y filósofo romano cuya obra influyó en la medicina occidental durante siglos.",
            "Obras": "Algunas de sus obras más importantes son *Sobre los temperamentos* y *Sobre el uso de las partes del cuerpo*.",
            "Ideas": [
                "La teoría de los cuatro humores.",
                "La importancia de la disección en la medicina.",
                "La relación entre mente y cuerpo.",
                "La dieta y el ejercicio como factores clave para la salud.",
                "La medicina debe basarse en la observación y la experiencia."
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
