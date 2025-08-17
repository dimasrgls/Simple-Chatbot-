# Chatbot Pemesanan Restoran dengan Streamlit + Gemini (RAG)

Chatbot sederhana untuk membantu pelanggan melakukan **pemesanan makanan di restoran cepat saji**.  
Dibuat menggunakan **Python, Streamlit, dan Google Gemini API**.  
Chatbot ini mendukung **RAG (Retrieval-Augmented Generation)** sehingga bisa membaca **file menu restoran (PDF/TXT)** lalu menjawab pertanyaan atau memproses pesanan berdasarkan menu tersebut.  

---

## Fitur
- ✅ Upload file menu restoran (format `.pdf` atau `.txt`)  
- ✅ Chatbot menjawab hanya berdasarkan isi menu  
- ✅ Mendukung percakapan multi-turn (chat history tersimpan)  
- ✅ Bisa digunakan untuk pemesanan makanan secara interaktif  

---

##  Instalasi & Setup

### 1. Clone repository

git clone https://github.com/USERNAME/NAMA-REPO.git
cd NAMA-REPO

### 2. Buat virtual environment 
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # Mac/Linux

### 3. Install dependencies
pip install -r requirements.txt
Atau manual:
pip install streamlit python-dotenv google-generativeai PyPDF2
Konfigurasi API Key Gemini

### 4. Buat file .env di root project, isi dengan:

GOOGLE_API_KEY=YOUR_GEMINI_API_KEY


Ganti YOUR_GEMINI_API_KEY dengan API key milikmu dari Google AI Studio.


# Menjalankan Chatbot
Untuk chatbot standar (menu di-hardcode di script):
streamlit run main.py

Untuk chatbot RAG (membaca menu dari file PDF/TXT):
streamlit run RAG_chatbot.py

# 📂 Contoh File Menu
## menu.txt
🍔 Burger - Rp 25.000
🍗 Fried Chicken - Rp 20.000
🍟 French Fries - Rp 15.000
🥤 Soft Drink - Rp 10.000

menu.pdf

# Cara Menggunakan

1. Jalankan aplikasi dengan perintah di atas.
2. Upload file menu (menu.txt atau menu.pdf).
3. Mulai chat dengan chatbot, misalnya:
   -"Saya mau pesan 2 burger dan 1 soft drink"
   -"Ada menu ayam goreng?"
   -"Berapa harga kentang goreng?"

#  Tech Stack

Python 3.9+
Streamlit → UI chatbot
Google Gemini API → LLM untuk memahami pertanyaan
PyPDF2 → Membaca teks dari PDF menu

# Catatan

1.Tanpa file menu → chatbot tidak bisa menjawab.
2. Dengan file menu → chatbot hanya menjawab berdasarkan daftar menu yang diunggah.
3. Proyek ini cocok untuk final project Hacktiv8, demo, atau prototype chatbot restoran.

# Author
Dibuat oleh Dimas Ragil Sampoerna sebagai final project Hacktiv8 LLM-Based Tools and Gemini API Integration for Data Scientists
