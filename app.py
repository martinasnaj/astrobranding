
import streamlit as st
from datetime import datetime
from skyfield.api import N, E, wgs84, load, Topos

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

# UI
st.title("AstroBranding – Značka Tvé Duše")

birthdate = st.date_input("Datum narození", value=datetime(1980, 7, 9), min_value=datetime(1900, 1, 1), max_value=datetime(2035, 12, 31))
birthtime = st.text_input("Čas narození (např. 10:10)", "10:10")
birthplace = st.text_input("Místo narození (prozatím bez geo výpočtu)", "Znojmo")

if st.button("Objev svou značku"):
    date_numeric = birthdate.strftime('%d%m%Y')
    lp, raw_sum = life_path_number(date_numeric)
    numeric_full = int(date_numeric)
    qmod = quasi_prime_mod24(numeric_full)
    
    st.subheader("🔹 Numerologický Výstup")
    st.write(f"Životní číslo: {lp}")
    st.write(f"Součet všech číslic: {raw_sum}")
    st.write(f"Kvazi-prvočíselná pozice (mod 24): {qmod}")
    
    # ASTRO modul
    ts = load.timescale()
    hour, minute = map(int, birthtime.split(":"))
    dt = datetime.combine(birthdate, datetime.min.time()).replace(hour=hour, minute=minute)
    t = ts.utc(dt.year, dt.month, dt.day, dt.hour, dt.minute)
    
    eph = load('de421.bsp')
    sun, moon = eph['sun'], eph['moon']
    earth = eph['earth']
    loc = earth + wgs84.latlon(48.855, 16.048)  # Znojmo approx
    
    astrometric_sun = loc.at(t).observe(sun).apparent()
    astrometric_moon = loc.at(t).observe(moon).apparent()
    
    sun_ra, sun_dec, _ = astrometric_sun.radec()
    moon_ra, moon_dec, _ = astrometric_moon.radec()
    
    st.subheader("🌞 Astrologický Výstup")
    st.write(f"RA Slunce: {sun_ra.hours:.2f}h")
    st.write(f"RA Měsíc: {moon_ra.hours:.2f}h")
    
    glyph = "🜄 + ☽ + 🝮" if lp == 7 else "⚛ + ♁ + ☐"
    brandword = "Zrcadlení" if lp == 7 else "Tvořivost"
    
    st.write(f"Glyphický kód: {glyph}")
    st.write(f"Značkové slovo: {brandword}")
    
    st.markdown("> _„Jsem zrcadlem. Netvořím hluk, tvořím hloubku. Má značka je dech mé duše, viditelný pro ty, kteří ladí.“_")
