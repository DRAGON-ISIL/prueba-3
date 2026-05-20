# 🎸 Trivia de Cantantes del Rock Peruano en Streamlit

## `app.py`

```python
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
    st.session_state.answered = False
    st.session_state.selected = None

    # Mezclar preguntas
    questions = QUESTIONS.copy()
    random.shuffle(questions)

    # Tomar solo 5 preguntas y mezclar opciones
    prepared = []
    for q in questions[:5]:
        q_copy = q.copy()
        options = q_copy["options"].copy()
        random.shuffle(options)
        q_copy["options"] = options
        prepared.append(q_copy)

    st.session_state.questions = prepared


# Inicialización
if "questions" not in st.session_state:
    initialize_game()


# Título
st.title("🎸 Trivia: Cantantes del Rock Peruano")
st.write("Responde las 5 preguntas. ¡Si aciertas todas, recibirás una sorpresa! 🎉")


# Datos actuales
index = st.session_state.current_question
score = st.session_state.score
questions = st.session_state.questions


# Barra de progreso
progress = index / len(questions)
st.progress(progress)
st.write(f"**Puntaje:** {score} / {len(questions)}")


# Si todavía hay preguntas
if index < len(questions):
    q = questions[index]

    st.subheader(f"Pregunta {index + 1} de {len(questions)}")
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
            st.error(f"❌ Incorrecto. La respuesta correcta era: {q['answer']}")

        st.session_state.current_question += 1
        st.rerun()

# Fin del juego
else:
    total = len(questions)
    st.header("🏁 Trivia finalizada")    
    st.write(f"Tu puntaje final es **{score} de {total}**.")

    if score == total:
        st.balloons()
        st.success("🏆 ¡Felicidades! ¡Respondiste correctamente las 5 preguntas! 🎸🤘")
        st.markdown(
            """
            ## 🌟 ¡Eres un verdadero experto del rock peruano! 🌟
            """
        )
    elif score >= 3:
        st.info("🎵 ¡Muy bien! Conoces bastante del rock peruano.")
    else:
        st.warning("📚 Sigue escuchando rock peruano y vuelve a intentarlo.")

    if st.button("🔄 Jugar nuevamente"):
        initialize_game()
        st.rerun()
```

---

## `requirements.txt`

```txt
streamlit>=1.45.0
```

---

# 📁 Estructura del Proyecto

```text
trivia-rock-peruano/
├── app.py
└── requirements.txt
```

---

# 🚀 Cómo subir a GitHub

1. Crea un repositorio en GitHub llamado `trivia-rock-peruano`.
2. Sube los archivos `app.py` y `requirements.txt`.
3. Haz commit y push.

---

# ☁️ Cómo desplegar en Streamlit Cloud

1. Ingresa a [https://share.streamlit.io](https://share.streamlit.io)
2. Inicia sesión con tu cuenta de GitHub.
3. Selecciona el repositorio `trivia-rock-peruano`.
4. En `Main file path`, escribe `app.py`.
5. Haz clic en **Deploy**.

---

# ▶️ Ejecutar localmente

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

# ✨ Características incluidas

* ✅ 5 preguntas sobre cantantes del rock peruano.
* ✅ Opciones mezcladas aleatoriamente.
* ✅ Preguntas en orden aleatorio.
* ✅ Puntaje automático.
* ✅ Barra de progreso.
* ✅ Animación con globos si el jugador obtiene 5/5.
* ✅ Botón para reiniciar el juego.
