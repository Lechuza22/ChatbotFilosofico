import streamlit as st
import openai
import os
from langchain_openai import ChatOpenAI

# Configurar API Key de OpenAI
openai_api_key = st.secrets.get(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") or os.getenv("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")

if not openai_api_key:
    st.error("Error: No se encontró la API Key de OpenAI. Asegúrate de configurarla correctamente.")
    st.stop()

# Datos de los filósofos
philosophers = {
    "Tales de Mileto": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/65/Thales_of_Miletus.jpg",
        "bio": "Tales de Mileto fue un filósofo presocrático considerado uno de los Siete Sabios de Grecia. Es conocido por su teoría de que el agua es el principio de todas las cosas.",
        "topics": "El principio del agua, Matemáticas y geometría, Astronomía primitiva"
    },
    "Parménides": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/2/2d/Parmenides.jpg",
        "bio": "Parménides de Elea fue un filósofo presocrático que sostuvo que el ser es uno, eterno e inmutable. Su obra más conocida es un poema filosófico llamado 'Sobre la naturaleza'.",
        "topics": "El ser y la inmovilidad, La lógica y la razón, La ilusión del cambio"
    },
    "Pitágoras": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Pythagoras_in_the_Roman_Forum%2C_Cologne.jpg/330px-Pythagoras_in_the_Roman_Forum%2C_Cologne.jpg",
        "bio": "Pitágoras fue un filósofo y matemático griego que fundó una escuela donde la matemática y la filosofía estaban estrechamente relacionadas. Es famoso por el teorema que lleva su nombre.",
        "topics": "Números y realidad, La armonía del cosmos, El alma y la reencarnación"
    },
    "Sócrates": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/7/76/Socrates_Louvre.jpg",
        "bio": "Sócrates fue un filósofo griego conocido por su método dialéctico y por no haber dejado escritos propios. Su pensamiento fue transmitido por Platón y Jenofonte.",
        "topics": "El conocimiento de sí mismo, La ética y la virtud, La mayéutica"
    },
    "Platón": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/3a/Plato_Silanion_Musei_Capitolini_MC1377.jpg",
        "bio": "Platón fue un discípulo de Sócrates y maestro de Aristóteles. Fundó la Academia y desarrolló la teoría de las Ideas, que influenció profundamente la filosofía occidental.",
        "topics": "El mundo de las Ideas, La justicia y la República, El conocimiento y la educación"
    },
    "Aristóteles": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/f/fb/Aristotle_Altemps_Inv8575.jpg",
        "bio": "Aristóteles fue un filósofo y científico de la Antigua Grecia. Fue discípulo de Platón y tutor de Alejandro Magno. Fundó el Liceo y desarrolló la lógica y la metafísica.",
        "topics": "La lógica y el silogismo, La ética y la felicidad, La política y el bien común"
    }
}

# Inicializar modelo de IA con LangChain
try:
    chat_model = ChatOpenAI(model="gpt-4", openai_api_key=openai_api_key)
except openai.error.AuthenticationError:
    st.error("Error de autenticación: La API Key de OpenAI no es válida. Verifica tu clave.")
    st.stop()
except openai.error.APIConnectionError:
    st.error("Error de conexión: No se pudo conectar con OpenAI. Verifica tu conexión a internet.")
    st.stop()

def chatbot_response(question, philosopher):
    prompt = f"""
    Imagina que eres {philosopher}, un filósofo de la antigua Grecia. Responde de manera coherente con tu pensamiento,
    sin anacronismos y evitando temas fuera de tu contexto histórico.
    
    **Tu filosofía se basa en los siguientes temas:** {philosophers[philosopher]['topics']}
    
    Pregunta: {question}
    Respuesta:
    """
    
    try:
        response = chat_model.invoke(prompt)
        return response
    except openai.error.OpenAIError as e:
        return f"Hubo un error con OpenAI: {str(e)}"

# Interfaz de usuario en Streamlit
st.title("Chatbot de Filósofos Antiguos")

# Menú de selección de filósofos
philosopher = st.selectbox("Elige un filósofo para conversar:", list(philosophers.keys()))

# Mostrar información del filósofo seleccionado
if philosopher:
    st.image(philosophers[philosopher]["image"], width=200)
    st.write(f"**{philosopher}**: {philosophers[philosopher]['bio']}")
    
    # Pregunta del usuario
    user_input = st.text_input("Haz una pregunta al filósofo:")
    if st.button("Preguntar") and user_input:
        response = chatbot_response(user_input, philosopher)
        st.write(f"**{philosopher}**: {response}")
