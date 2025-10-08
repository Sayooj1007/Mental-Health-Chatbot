import streamlit as st


st.title("📂 Conversation History")

if "history" in st.session_state and st.session_state.history:
    for i, entry in enumerate(st.session_state.history, 1):
        st.markdown(f"**{i}. You said:** {entry['user']}")
        st.markdown(f"🧭 *Mood:* `{entry['mood'].capitalize()}`")
        st.markdown(f"🤗 *Bot Response:* {entry['bot']}")
        st.markdown("---")
else:
    st.info("No conversation history found yet.")
