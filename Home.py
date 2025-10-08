import streamlit as st
import google.generativeai as genai
import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from dotenv import load_dotenv

load_dotenv()
client = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=client)
model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="Mental Health Companion", layout="centered")
st.title("🧘 Mental Health Companion Chatbot")

st.session_state.setdefault("history",[])

user_input = st.text_area("How are you feeling today?", height= 150)

def get_response(user_input, mood):
    prompt = f"""
    Act as a compassionate mental health chatbot. The user feels {mood}.
    Respond empathetically to this message: "{user_input}"
    Include motivational support and a gentle tone.
    """
    response = model.generate_content(prompt)
    return response.text

analyzer = SentimentIntensityAnalyzer()
def analyze_sentiment(text):
    scores = analyzer.polarity_scores(text)
    compound = scores["compound"]
    print(f"VADER Polarity score: {compound}")

    if compound >= 0.3:
        return "positive"
    elif compound <= -0.3:
        return "negative"
    else:
        return "neutral"

def get_relaxation_tip(mood):
    prompt = f"""Act as a compassionate mental health chatbot. The user feels {mood}.
                Suggest the user meditation guide or tips according to the user mood and {user_input}."""
    guide = model.generate_content(prompt)
    return guide.text  

if st.button("Send"):
    if user_input.strip():
        with st.spinner("Generating..."):
            mood = analyze_sentiment(user_input)
            response = get_response(user_input, mood)
            tip = get_relaxation_tip(mood)

            st.session_state["history"].append({
                "user": user_input,
                "mood": mood,
                "bot": response,
                "tip": tip
            })

            st.markdown("### 🤗 Chatbot Response")
            st.write(response)

            st.markdown("### 🌿 Relaxation Tip")
            st.info(tip)

    else:
        st.warning("Please enter a message.")



