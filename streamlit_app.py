import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import re

st.set_page_config(page_title="LifeForge v2", layout="wide")

st.title("💡 LifeForge: AI-Enhanced Personal Journey Designer (Prototype v2)")

with st.form("life_options"):
    st.subheader("Step 1: Define Two Life Options")
    option1 = st.text_area("🅰️ Option 1", height=120)
    option2 = st.text_area("🅱️ Option 2", height=120)

    st.subheader("Step 2: Enter Your Profile")
    age = st.slider("Your Age", 18, 70, 25)
    personality = st.selectbox("Your Personality Trait", ["Resilient", "Ambitious", "Flexible"])
    lifestyle_pref = st.slider("Importance of Lifestyle Quality", 1, 10, 5)

    simulate = st.form_submit_button("Run Simulation")

def interpret_option(text):
    themes = {
        "career": 0,
        "migration": 0,
        "passion": 0,
        "stability": 0,
        "family": 0
    }
    keywords = {
        "career": ["job", "salary", "promotion", "company", "income"],
        "migration": ["abroad", "canada", "japan", "move", "relocate", "visa"],
        "passion": ["dream", "startup", "art", "music", "business"],
        "stability": ["stay", "safe", "secure", "known", "same"],
        "family": ["parents", "support", "close", "home", "kids"]
    }

    for theme, keys in keywords.items():
        for word in keys:
            if re.search(rf"\b{word}\b", text.lower()):
                themes[theme] += 1
    return themes

def simulate_outcomes(themes, lifestyle):
    happiness = 5 + themes["passion"] + themes["family"]
    income = 2000 + 1000 * themes["career"]
    stress = 5 + themes["migration"] - themes["stability"]
    happiness += lifestyle // 3
    stress -= lifestyle // 4
    final_score = round((2 * happiness + 2 * income / 1000 - stress) / 5, 2)

    return {
        "happiness": min(happiness, 10),
        "income": income,
        "stress": max(stress, 1),
        "score": final_score
    }

def display_results(title, result):
    st.markdown(f"### {title}")
    st.metric("🧘 Happiness", f"{result['happiness']}/10")
    st.metric("💰 Income", f"${result['income']}")
    st.metric("💢 Stress", f"{result['stress']}/10")
    st.success(f"Final Score: {result['score']}")

def draw_comparison_chart(results):
    try:
        categories = ["Happiness", "Income", "Stress"]
        values1 = [results[0]["happiness"], results[0]["income"], results[0]["stress"]]
        values2 = [results[1]["happiness"], results[1]["income"], results[1]["stress"]]

        x = np.arange(len(categories))
        width = 0.35

        fig, ax = plt.subplots()
        ax.bar(x - width/2, values1, width, label='Option 1', color="#1f77b4")
        ax.bar(x + width/2, values2, width, label='Option 2', color="#ff7f0e")
        ax.set_ylabel('Scores')
        ax.set_title('Option Comparison')
        ax.set_xticks(x)
        ax.set_xticklabels(categories)
        ax.legend()
        st.pyplot(fig)
    except Exception as e:
        st.error(f"❌ Failed to generate chart: {e}")

# Main logic
if simulate and option1 and option2:
    st.subheader("🔍 Simulation Output")

    themes1 = interpret_option(option1)
    themes2 = interpret_option(option2)

    result1 = simulate_outcomes(themes1, lifestyle_pref)
    result2 = simulate_outcomes(themes2, lifestyle_pref)

    col1, col2 = st.columns(2)
    with col1:
        display_results("🅰️ Option 1", result1)
    with col2:
        display_results("🅱️ Option 2", result2)

    st.markdown("### 📊 Visual Comparison")
    draw_comparison_chart([result1, result2])

    st.info("ℹ️ Prototype based on keyword-based NLP. Future versions will use transformer-based models and real-world datasets.")
