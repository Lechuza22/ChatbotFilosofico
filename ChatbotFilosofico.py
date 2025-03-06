import streamlit as st
import random

# Datos de los filósofos
philosophers = {
    "Tales de Mileto": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/65/Thales_of_Miletus.jpg",
        "bio": "Tales de Mileto fue un filósofo presocrático considerado uno de los Siete Sabios de Grecia. Es conocido por su teoría de que el agua es el principio de todas las cosas.",
        "topics": ["El principio del agua", "Matemáticas y geometría", "Astronomía primitiva"]
    },
    "Parménides": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/2/2d/Parmenides.jpg",
        "bio": "Parménides de Elea fue un filósofo presocrático que sostuvo que el ser es uno, eterno e inmutable. Su obra más conocida es un poema filosófico llamado 'Sobre la naturaleza'.",
        "topics": ["El ser y la inmovilidad", "La lógica y la razón", "La ilusión del cambio"]
    },
    "Pitágoras": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Pythagoras_in_the_Roman_Forum%2C_Cologne.jpg/330px-Pythagoras_in_the_Roman_Forum%2C_Cologne.jpg",
        "bio": "Pitágoras fue un filósofo y matemático griego que fundó una escuela donde la matemática y la filosofía estaban estrechamente relacionadas. Es famoso por el teorema que lleva su nombre.",
        "topics": ["Números y realidad", "La armonía del cosmos", "El alma y la reencarnación"]
    },
    "Sócrates": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/7/76/Socrates_Louvre.jpg",
        "bio": "Sócrates fue un filósofo griego conocido por su método dialéctico y por no haber dejado escritos propios. Su pensamiento fue transmitido por Platón y Jenofonte.",
        "topics": ["El conocimiento de sí mismo", "La ética y la virtud", "La mayéutica"]
    },
    "Platón": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/3a/Plato_Silanion_Musei_Capitolini_MC1377.jpg",
        "bio": "Platón fue un discípulo de Sócrates y maestro de Aristóteles. Fundó la Academia y desarrolló la teoría de las Ideas, que influenció profundamente la filosofía occidental.",
        "topics": ["El mundo de las Ideas", "La justicia y la República", "El conocimiento y la educación"]
    },
    "Aristóteles": {
        "image": "https://upload.wikimedia.org/wikipedia/commons/f/fb/Aristotle_Altemps_Inv8575.jpg",
        "bio": "Aristóteles fue un filósofo y científico de la Antigua Grecia. Fue discípulo de Platón y tutor de Alejandro Magno. Fundó el Liceo y desarrolló la lógica y la metafísica.",
        "topics": ["La lógica y el silogismo", "La ética y la felicidad", "La política y el bien común"]
    }
}

# Función para generar respuestas
responses = {
    "¿Cuáles son los principales temas de tu pensamiento?": "Mis principales temas de estudio incluyen: {topics}.",
    "¿Qué opinas sobre la vida?": "Mi pensamiento sobre la vida está relacionado con {topics}.",
    "¿Cuál es tu obra más importante?": "Mi obra más importante es '{work}', donde desarrollo mis principales ideas."
}

def chatbot_response(question, philosopher):
    if question in responses:
        return responses[question].format(topics=", ".join(philosophers[philosopher]["topics"]))
    else:
        return "Esa pregunta no se encuentra en mi campo de estudio o es anacrónica."

# Interfaz de usuario en Streamlit
st.title("Chatbot de Filósofos Antiguos")

# Menú de selección de filósofos
philosopher = st.selectbox("Elige un filósofo para conversar:", list(philosophers.keys()))

# Mostrar información del filósofo seleccionado
if philosopher:
    st.image(philosophers[philosopher]["image"], width=200)
    st.write(f"**{philosopher}**: {philosophers[philosopher]['bio']}")

    st.write("### Preguntas sugeridas:")
    question = st.radio("Elige una pregunta para hacerle:", list(responses.keys()))
    
    if st.button("Preguntar"): 
        response = chatbot_response(question, philosopher)
        st.write(f"**{philosopher}**: {response}")
