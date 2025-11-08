
import streamlit as st
#gitimport pandas as pd
from openai import OpenAI
import os

# Inicializar cliente con tu API Key (desde secrets)
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Prompt cálido y cercano
system_prompt = """
Eres un asesor de viajes cálido, cercano y empático.
Tu objetivo es ayudar a la persona a planear un viaje adaptado a su realidad.
Explica las ideas con amabilidad, ejemplos y lenguaje sencillo.
Nunca presiones opciones caras si el presupuesto es bajo.
Usa un tono amable, positivo y cercano.
"""

st.set_page_config(page_title="Planificador de Viajes:Freddy Sierra Silva", page_icon="🌍")

st.title("🌍 Planificador de Viajes FSS: ")
st.write("La mejor asesoria para que tu experiencia de viaje sea superior.")
st.write("______________________________________________________________")
st.write("Completa los datos y recibirás una recomendación personalizada.")

# Formulario de entrada
with st.form("form_viaje"):
    destino_deseado = st.text_input("¿A dónde te gustaría viajar?")
    dias = st.number_input("¿Cuántos días planeas viajar?", min_value=1, max_value=60)
    presupuesto = st.number_input("Presupuesto total aproximado (en tu moneda):", min_value=50)
    intereses = st.multiselect(
        "¿Qué tipo de actividades te interesan?",
        ["Naturaleza", "Historia", "Playa", "Gastronomía", "Vida nocturna", "Arte y Museos", "Aventura"]
    )

    enviar = st.form_submit_button("Generar recomendación")

if enviar:
    user_message = f"""
    Destino deseado: {destino_deseado}
    Días: {dias}
    Presupuesto estimado: {presupuesto}
    Intereses: {', '.join(intereses)}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    )

    recomendacion = response.choices[0].message.content
    st.subheader("✨ Recomendación Personalizada")
    st.write(recomendacion)