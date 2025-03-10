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
        "Tales de Mileto": {"Biografía": "Filósofo presocrático considerado el primero de los filósofos griegos...", "Obras": "No dejó textos escritos", "Ideas": "El agua como principio fundamental de todas las cosas."},
        "Anaximandro": {"Biografía": "Discípulo de Tales, desarrolló la idea del apeiron...", "Obras": "Fragmentos recopilados", "Ideas": "El apeiron como principio de todo."},
        "Anaxágoras": {"Biografía": "Filósofo presocrático que introdujo la noción de Nous...", "Obras": "Sobre la naturaleza", "Ideas": "El Nous (mente) como principio ordenador del cosmos."},
        "Parménides": {"Biografía": "Filósofo eleático que desarrolló la idea del ser inmutable...", "Obras": "Poema sobre la naturaleza", "Ideas": "El ser es y el no-ser no es."},
        "Heráclito": {"Biografía": "Filósofo de Éfeso que postuló la doctrina del cambio...", "Obras": "Fragmentos recopilados", "Ideas": "Todo fluye, el cambio es la única constante."},
        "Pitágoras": {"Biografía": "Filósofo y matemático griego...", "Obras": "No dejó textos escritos", "Ideas": "El número como principio fundamental del universo."},
        "Galeno": {"Biografía": "Médico y filósofo romano...", "Obras": "Sobre los temperamentos", "Ideas": "Influencia de los humores en la salud."},
        "Sócrates": {"Biografía": "Filósofo ateniense, maestro de Platón...", "Obras": "No dejó escritos, su pensamiento fue registrado por Platón", "Ideas": "Conócete a ti mismo, la mayéutica."},
        "Platón": {"Biografía": "Discípulo de Sócrates y maestro de Aristóteles...", "Obras": "La República, El Banquete", "Ideas": "Teoría de las Ideas, el mundo sensible y el inteligible."},
        "Aristóteles": {"Biografía": "Discípulo de Platón y maestro de Alejandro Magno...", "Obras": "Ética a Nicómaco, Metafísica", "Ideas": "La sustancia, la lógica, la ética de la virtud."},
        "Plotino": {"Biografía": "Fundador del neoplatonismo...", "Obras": "Las Enéadas", "Ideas": "Emanación del Uno, jerarquía del ser."},
        "Diógenes": {"Biografía": "Filósofo cínico, discípulo de Antístenes...", "Obras": "No dejó textos escritos", "Ideas": "El desprecio por las convenciones sociales, la autosuficiencia."},
        "Epicuro": {"Biografía": "Filósofo griego, fundador del epicureísmo...", "Obras": "Carta a Meneceo", "Ideas": "Búsqueda del placer moderado, la ausencia de dolor como felicidad."}
    }
    
    seleccion = st.selectbox("Selecciona un filósofo", list(filosofos.keys()))
    
    if seleccion:
        imagen_path = os.path.join("imagenes", f"{seleccion}.jpg")
        if os.path.exists(imagen_path):
            st.image(imagen_path, caption=seleccion, use_column_width=True)
        
        st.subheader("Biografía")
        st.write(filosofos[seleccion]["Biografía"])
        
        st.subheader("Obras Principales")
        st.write(filosofos[seleccion]["Obras"])
        
        st.subheader("Principales Ideas")
        st.write(filosofos[seleccion]["Ideas"])

elif menu == "Línea Temporal":
    st.header("Línea Temporal de la Filosofía")
    
    datos = [
        ("Tales de Mileto", -624),
        ("Anaximandro", -610),
        ("Anaxágoras", -500),
        ("Parménides", -515),
        ("Heráclito", -535),
        ("Pitágoras", -570),
        ("Sócrates", -470),
        ("Platón", -427),
        ("Aristóteles", -384),
        ("Epicuro", -341),
        ("Diógenes", -412),
        ("Plotino", 205),
        ("Galeno", 129)
    ]
    
    df = pd.DataFrame(datos, columns=["Filósofo", "Año"])
    
    fig = px.scatter(
        df, x="Año", y="Filósofo", size=[10]*len(df),
        color="Año", text="Filósofo", hover_data=["Año"],
        size_max=15, color_continuous_scale=px.colors.sequential.Viridis,
        title="Línea Temporal de la Filosofía"
    )
    fig.update_layout(yaxis_title="Filósofo", xaxis_title="Año")
    st.plotly_chart(fig)
