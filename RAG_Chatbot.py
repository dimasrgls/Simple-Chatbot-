import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from PyPDF2 import PdfReader

# Load API Key Gemini
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

# Fungsi untuk baca PDF menu
def read_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

# --- UI Streamlit ---
st.title("🍔 RAG Chatbot Pemesanan Restoran")

# Upload file menu
uploaded_file = st.file_uploader("📂 Upload file menu (PDF/TXT)", type=["pdf", "txt"])

if uploaded_file:
    if uploaded_file.name.endswith(".pdf"):
        menu_text = read_pdf(uploaded_file)
    else:
        menu_text = uploaded_file.read().decode("utf-8")

    st.success("✅ Menu berhasil dimuat!")

    # Simpan chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Tampilkan chat history
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).markdown(msg["content"])

    # Input user
    if prompt := st.chat_input("Mau pesan apa hari ini?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").markdown(prompt)

        # Prompt dengan menu (RAG)
        full_prompt = f"""
        Kamu adalah chatbot pemesanan restoran cepat saji.
        Berikut adalah daftar menu restoran:
        {menu_text}

        Jawablah dan bantu pemesanan hanya berdasarkan menu di atas.
        User: {prompt}
        """

        response = model.generate_content(full_prompt)
        answer = response.text

        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.chat_message("assistant").markdown(answer)
else:
    st.info("⬆️ Silakan upload file menu dulu")