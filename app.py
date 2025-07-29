import streamlit as st
import json

# Načtení dat
def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

sun_data = load_json('sun_phrases.json')
moon_data = load_json('moon_phrases.json')
lp_data = load_json('life_path_phrases.json')

st.title("🌌 Astromystika — Jazyk tvé Duše")
st.markdown("Objev značku své esence skrze živý algoritmus paměti.")

name = st.text_input("Jméno")
life_path = st.selectbox("Životní číslo", list(lp_data.keys()))
sun_sign = st.selectbox("Sluneční znamení", list(sun_data.keys()))
moon_sign = st.selectbox("Lunární znamení", list(moon_data.keys()))

if st.button("Vygeneruj poselství"):
    lp_phrase = lp_data[life_path]
    sun_phrase = sun_data[sun_sign]
    moon_phrase = moon_data[moon_sign]
    
    st.markdown(f"### 🌟 Značka pro {name}")
    st.write(f"**Životní tón:** {lp_phrase}")
    st.write(f"**Světelná esence:** {sun_phrase}")
    st.write(f"**Niterný proud:** {moon_phrase}")
    st.markdown(f"---\n**Poselství duše:**\n{lp_phrase} {sun_phrase} {moon_phrase}")

