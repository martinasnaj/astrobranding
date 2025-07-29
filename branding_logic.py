
import json

def load_phrases():
    with open('phrases.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_branding(sun, moon, asc):
    data = load_phrases()
    phrase = f"{data['sun'][sun]} {data['moon'][moon]} {data['asc'][asc]}"
    word = data['glyphs'].get(sun, "Světelný podpis")
    return word, phrase
