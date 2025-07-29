
import streamlit as st
from astro_calc import calculate_positions
from branding_logic import generate_branding

st.title("🌟 Astrobranding – Tvá hvězdná značka")

name = st.text_input("Jméno")
date = st.text_input("Datum narození (DD.MM.RRRR)")
time = st.text_input("Čas narození (HH:MM)")
place = st.text_input("Místo narození")

if st.button("Získat značku"):
    sun, moon, asc = calculate_positions(date, time, place)
    word, phrase = generate_branding(sun, moon, asc)
    st.markdown(f"## 🌠 {name}")
    st.write(f"**Slunce:** {sun}")
    st.write(f"**Luna:** {moon}")
    st.write(f"**Ascendent:** {asc}")
    st.markdown(f"### ✨ Značka duše: *{word}*")
    st.markdown(f"---\n**Poselství:** {phrase}")
