import streamlit as st
import random

st.set_page_config(
    page_title="Trivia Rock Peruano",
    page_icon="🎸",
    layout="centered"
)

# Banco de preguntas
QUESTIONS = [
    {
        "question": "¿Quién fue el vocalista principal de Arena Hash?",
        "options": [
            "Pedro Suárez-Vértiz",
            "Wicho García",
            "Raúl Romero",
            "Jhovan Tomasevich",
        ],
        "answer": "Pedro Suárez-Vértiz",
    },
    {
        "question": "¿Quién fue el vocalista de Nosequién y los Nosecuántos?",
        "options": [
            "Raúl Romero",
            "Miki González",
            "Pedro Suárez-Vértiz",
            "Daniel F",
        ],
        "answer": "Raúl Romero",
    },
    {
        "question": "¿Quién es el vocalista de Zen?",
        "options": [
            "Jhovan Tomasevich",
            "Wicho García",
            "Raúl Romero",
            "Pedro Suárez-Vértiz",
        ],
        "answer": "Jhovan Tomasevich",
    },
    {
        "question": "¿Quién es el vocalista de Mar de Copas?",
        "options": [
            "Wicho García",
            "Miki González",
            "Daniel F",
            "Pelo Madueño",
        ],
        "answer": "Wicho García",
    },
    {
        "question": "¿Qué cantante peruano es conocido por temas como 'Akundún'?",
        "options": [
            "Miki González",
            "Pedro Suárez-Vértiz",
            "Raúl Romero",
            "Jhovan Tomasevich",
        ],
        "answer": "Miki González",
    },
]


def initialize_game():
    """Inicializa o reinicia la partida."""
    st.session_state.current_question = 0
    st.session_state.score = 0

    # Mezclar preguntas
    questions = QUESTIONS.copy()
    random.shuffle(questions)

    # Mezclar opciones de cada pregunta
    prepared = []
    for q in questions[:5]:
        q_copy = q.copy()
        options = q_copy["options"].copy()
        random.shuffle(options)
        q_copy["options"] = options
        prepared.append(q_copy)

    st.session_state.questions = prepared


# Inicialización del juego
if "questions" not in st.session_state:
    initialize_game()


# Título
st.title("🎸 Trivia: Cantantes del Rock Peruano")
st.write(
    "Responde las 5 preguntas. "
    "¡Si aciertas todas, recibirás una animación de celebración! 🎉"
)

# Variables de estado
index = st.session_state.current_question
score = st.session_state.score
questions = st.session_state.questions
total_questions = len(questions)

# Barra de progreso
st.progress(index / total_questions)
st.write(f"**Puntaje actual:** {score} / {total_questions}")

# Mostrar preguntas
if index < total_questions:
    q = questions[index]

    st.subheader(f"Pregunta {index + 1} de {total_questions}")
    st.write(q["question"])

    selected = st.radio(
        "Selecciona tu respuesta:",
        q["options"],
        key=f"question_{index}"
    )

    if st.button("Responder"):
        if selected == q["answer"]:
            st.success("✅ ¡Correcto!")
            st.session_state.score += 1
        else:
            st.error(
                f"❌ Incorrecto. La respuesta correcta era: {q['answer']}"
            )

        st.session_state.current_question += 1
        st.rerun()

# Fin del juego
else:
    final_score = st.session_state.score

    st.header("🏁 Trivia finalizada")
    st.write(
        f"Tu puntaje final es "
        f"**{final_score} de {total_questions}**."
    )

    # Si acertó todas las preguntas
    if final_score == total_questions:
        st.balloons()
        st.success(
            "🏆 ¡Felicidades! "
            "¡Respondiste correctamente las 5 preguntas! 🎸🤘"
        )
        st.markdown("## 🌟 ¡Eres un verdadero experto del rock peruano! 🌟")

    elif final_score >= 3:
        st.info("🎵 ¡Muy bien! Conoces bastante del rock peruano.")
    else:
        st.warning(
            "📚 Sigue escuchando rock peruano y vuelve a intentarlo."
        )

    # Botón para reiniciar
    if st.button("🔄 Jugar nuevamente"):
        initialize_game()
        st.rerun()
