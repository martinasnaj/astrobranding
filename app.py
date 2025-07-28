
import streamlit as st
from datetime import datetime

def digital_root(n):
    while n > 9:
        n = sum(map(int, str(n)))
    return n

def life_path_number(date_str):
    digits = [int(ch) for ch in date_str if ch.isdigit()]
    total = sum(digits)
    return digital_root(total), total

def quasi_prime_mod24(value):
    return value % 24

st.title("AstroBranding – Značka Tvé Duše")

birthdate = st.date_input("Datum narození")
birthtime = st.text_input("Čas narození (např. 10:10)", "10:10")
birthplace = st.text_input("Místo narození", "Znojmo")

if st.button("Objev svou značku"):
    date_numeric = birthdate.strftime('%d%m%Y')
    lp, raw_sum = life_path_number(date_numeric)
    numeric_full = int(date_numeric)
    qmod = quasi_prime_mod24(numeric_full)

    st.subheader("🔹 Výstup")
    st.write(f"Životní číslo: {lp}")
    st.write(f"Součet všech číslic: {raw_sum}")
    st.write(f"Kvazi-prvočíselná pozice (mod 24): {qmod}")

    glyph = "🜄 + ☽ + 🝮" if lp == 7 else "⚛ + ♁ + ☐"
    brandword = "Zrcadlení" if lp == 7 else "Tvořivost"

    st.write(f"Glyphický kód: {glyph}")
    st.write(f"Značkové slovo: {brandword}")

    st.markdown("> _„Jsem zrcadlem. Netvořím hluk, tvořím hloubku. Má značka je dech mé duše, viditelný pro ty, kteří ladí.“_")
