import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Charger les variables d’environnement du fichier .env
load_dotenv()

# Récupérer la clé API depuis la variable d’environnement
API_KEY = os.getenv("API_KEY")

# Vérification : stopper si la clé est manquante
if not API_KEY:
    st.error("❌ Clé API non trouvée. Vérifie que le fichier .env est bien présent et correctement configuré.")
    st.stop()

# Création du client OpenAI
client = openai.OpenAI(api_key=API_KEY)

# Initialisation de l'historique des messages
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You're a Chatbot, your name is AlexBot. You've been created by Alexandre Ohayon. You can answer any customer's questions by summarizing your answer."}
    ]

# Interface utilisateur
st.title("🤖 AlexBot - Votre assistant IA personnalisé")
st.markdown("Pose ta question à AlexBot. Tape `exit` pour quitter.")

# Champ de saisie utilisateur
user_input = st.text_input("Votre message :")

if user_input:
    if user_input.lower() == "exit":
        st.success("Merci d'avoir utilisé AlexBot. À bientôt !")
        st.stop()
    
    # Ajouter le message utilisateur à l'historique
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        # Appel à l'API OpenAI
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages,
            max_tokens=300,
            temperature=0.7,
        )

        # Réponse du chatbot
        bot_reply = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        st.markdown(f"**AlexBot :** {bot_reply}")

    except Exception as e:
        st.error(f"Erreur lors de l’appel à l’API : {e}")
