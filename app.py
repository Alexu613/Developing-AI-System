import streamlit as st

st.title("🤖 Simple Chatbot")

# Stocker l'historique
if "history" not in st.session_state:
    st.session_state.history = []

# Saisie utilisateur
user_input = st.text_input("You:")

# Si l'utilisateur écrit quelque chose
if user_input:
    bot_reply = f"You said: {user_input}"
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", bot_reply))

# Affichage de l'historique
for sender, message in st.session_state.history:
    st.write(f"**{sender}:** {message}")
