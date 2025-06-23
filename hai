# lifeforge_app.py

import streamlit as st
import random

st.set_page_config(page_title="LifeForge", layout="wide")

st.title("🧠 LifeForge: AI-Enhanced Personal Journey Designer")

with st.form("life_input_form"):
    st.header("Describe Two Life Paths You’re Considering")

    option1 = st.text_area("🔹 Life Path Option 1")
    option2 = st.text_area("🔹 Life Path Option 2")

    st.subheader("Your Profile")
    age = st.slider("Age", 18, 70, 25)
    personality = st.selectbox("Personality", ["Resilient", "Ambitious", "Flexible"])
    lifestyle = st.slider("Importance of Lifestyle", 1, 10, 5)

    submitted = st.form_submit_button("Simulate")

# Simple logic to score each option (placeholder)
def simulate_life(option_text, age, personality, lifestyle):
    # Fake NLP tags for demonstration
    themes = {
        "career": 0,
        "migration": 0,
        "passion": 0,
        "stability": 0
    }
    text = option_text.lower()
    if "abroad" in text or "move" in text or "canada" in text:
        themes["migration"] += 1
    if "startup" in text or "business" in text or "dream" in text:
        themes["passion"] += 1
    if "salary" in text or "job" in text or "promotion" in text:
        themes["career"] += 1
    if "stay" in text or "home" in text or "parents" in text:
        themes["stability"] += 1

    # Simulated scores
    happiness = random.randint(6, 10) if themes["passion"] else random.randint(3, 8)
    income = random.randint(3000, 8000) if themes["career"] else random.randint(1500, 5000)
    stress = random.randint(4, 8) if themes["migration"] else random.randint(2, 5)

    # Final score logic
    score = round((2 * happiness + 2 * income / 1000 - stress) / 5, 2)

    return {
        "happiness": happiness,
        "income": income,
        "stress": stress,
        "score": score
    }

# Run simulation and show results
if submitted:
    st.divider()
    st.subheader("🔍 Simulation Results")

    result1 = simulate_life(option1, age, personality, lifestyle)
    result2 = simulate_life(option2, age, personality, lifestyle)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Option 1")
        st.metric("Happiness", result1["happiness"])
        st.metric("Income (USD)", result1["income"])
        st.metric("Stress", result1["stress"])
        st.success(f"Final Score: {result1['score']}")

    with col2:
        st.markdown("### Option 2")
        st.metric("Happiness", result2["happiness"])
        st.metric("Income (USD)", result2["income"])
        st.metric("Stress", result2["stress"])
        st.success(f"Final Score: {result2['score']}")

    st.markdown("✅ *Note: This is a prototype simulation. Scores are based on simplified logic and random values.*")
