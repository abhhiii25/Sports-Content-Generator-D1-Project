import streamlit as st
import requests

st.set_page_config(page_title="Sports Content Generator", layout="wide")

st.title("🏆 Sports Content Generator")
st.markdown("Generate professional match recaps instantly.")

col1, col2 = st.columns(2)

with col1:
    sport = st.selectbox("Select Sport", ["Cricket", "Football", "Basketball"])
    teams = st.text_input("Teams (e.g., India vs Australia)")
    score = st.text_input("Final Score")
    tone = st.selectbox("Tone", ["Professional", "Analytical", "Casual"])

with col2:
    moments = st.text_area("Key Match Moments", height=200)

if st.button("Generate Recap 🚀"):

    data = {
        "sport": sport,
        "teams": teams,
        "score": score,
        "moments": moments,
        "tone": tone
    }

    response = requests.post("http://127.0.0.1:8000/generate", json=data)

    if response.status_code == 200:
        st.subheader("Generated Recap")
        st.write(response.json()["recap"])
    else:
        st.error("Error generating content")
