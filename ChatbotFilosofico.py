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

        "Anaxágoras": {
            "Biografía": "[Anaxágoras](https://es.wikipedia.org/wiki/Anax%C3%A1goras) (500-428 a.C.) fue un filósofo presocrático que introdujo el concepto de Nous (mente) como principio ordenador del cosmos.",
            "Obras": "Escribió *Sobre la Naturaleza*, del cual se conservan fragmentos.",
            "Ideas": [
                "El Nous es la inteligencia cósmica que organiza el universo.",
                "El Sol es una masa de fuego y no un dios.",
                "Todas las cosas contienen una porción de todo.",
                "La Luna refleja la luz del Sol.",
                "El universo es eterno y en constante movimiento."
            ]
        },
        "Parménides": {
            "Biografía": "[Parménides](https://es.wikipedia.org/wiki/Parm%C3%A9nides) (c. 515-450 a.C.) fue un filósofo presocrático fundador de la escuela eleática. Propuso la idea de que el ser es inmutable y eterno.",
            "Obras": "Su única obra conocida es *Poema sobre la Naturaleza*.",
            "Ideas": [
                "El ser es y el no-ser no es.",
                "El cambio y la multiplicidad son ilusiones.",
                "El conocimiento verdadero se alcanza a través de la razón.",
                "El universo es una unidad indivisible.",
                "La realidad es eterna e inmutable."
            ]
        },
        "Heráclito": {
            "Biografía": "[Heráclito](https://es.wikipedia.org/wiki/Her%C3%A1clito) (c. 535-475 a.C.) fue un filósofo presocrático de Éfeso que postuló la doctrina del cambio constante.",
            "Obras": "Su obra principal, *Sobre la Naturaleza*, se ha perdido, pero se conservan fragmentos.",
            "Ideas": [
                "Todo fluye y nada permanece.",
                "El fuego es el principio fundamental del universo.",
                "El conflicto es el motor del cambio.",
                "La realidad está en constante transformación.",
                "La armonía surge de la tensión de los opuestos."
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
            st.image(imagen_path, caption=seleccion, use_container_width=True)
        
        st.subheader("Biografía")
        st.markdown(filosofos[seleccion]["Biografía"])
        
        st.subheader("Obras Principales")
        st.markdown(filosofos[seleccion]["Obras"])
        
        st.subheader("Principales Ideas")
        st.markdown("\n".join([f"- {idea}" for idea in filosofos[seleccion]["Ideas"]]))


### LINEA TEMPORAL

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
