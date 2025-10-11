# Mental Health Companion Chatbot
This project is a Mental Health Support Chatbot built using [Streamlit](https://streamlit.io/) and [Google AI studio](https://aistudio.google.com/prompts/new_chat) model. It provides mental health support through a chat interface, offering sentiment analysis, mood tracking, and personalized coping strategies based on user input.

## Installation
### 1. Cloning the Repository:
```
git clone https://github.com/Sayooj1007/Mental-Health-Chatbot.git
cd Mental-Health-Chatbot
```
### 2. Create a virtual environment and activate it:
```
python -m venv env
.\env\Scripts\activate
```
### 3. Install the required packages:
```
pip install -r requirements.txt
```
### 4. Set up your Gemini AI API key:
- Obtain your Gemini AI API key from [Google AI Studio](https://aistudio.google.com/prompts/new_chat).
- Add your API key to the environment variable `GEMINI_API_KEY` replace the code with your actual API key.

## Usage
### 1. Run the Streamlit application:
```
streamlit run app.py
```
### 2. Open the provided URL (typically http://localhost:8501) in your web browser.
### 3. Start interacting with the chatbot:
- Type your message in the input box and press "Send."
- The chatbot will respond to your message, analyze the sentiment, track your mood, and provide coping strategies as needed.
