import streamlit as st

st.title("Aplikasi Sederhana")
nama = st.text_input("Masukkan nama kamu:")
if nama:
    st.write(f"Halo, {nama}! Selamat datang di Streamlit!")
    
