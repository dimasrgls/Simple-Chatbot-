import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")


menu = {
    "Burger": 25000,
    "Fried Chicken": 20000,
    "French Fries": 15000,
    "Soft Drink": 10000
}


st.title("🍔 Chatbot Pemesanan Restoran Cepat Saji")


if "messages" not in st.session_state:
    st.session_state.messages = []


for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])


if prompt := st.chat_input("Mau pesan apa hari ini?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    
    response = ""
    total = 0
    for item, harga in menu.items():
        if item.lower() in prompt.lower():
            response += f" {item} ditambahkan (Rp {harga})\n"
            total += harga

    if total > 0:
        response += f"\n Total sementara: Rp {total}"
    else:
        response = " Maaf, menu tidak tersedia. Coba pesan Burger, Fried Chicken, French Fries, atau Soft Drink."

    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").markdown(response)