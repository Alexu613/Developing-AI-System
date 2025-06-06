import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Charger la clé API depuis .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Fonction pour envoyer une requête à l'API OpenAI
def get_bot_response(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # ou "gpt-4" si tu y as accès
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    )
    return response["choices"][0]["message"]["content"]

# Interface Streamlit
st.title("🤖 OpenAI Chatbot")

# Stocker l'historique
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Saisie utilisateur
user_input = st.text_input("You:", key="user_input")

# Traitement de la conversation
if user_input:
    st.session_state.chat_history.append(("Client", user_input))
    response = get_bot_response(user_input)
    st.session_state.chat_history.append(("Bot", response))
    st.experimental_rerun()

# Afficher la conversation
st.markdown("### Conversation")
for sender, message in st.session_state.chat_history:
    if sender == "Client":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**🤖 Bot:** {message}")
