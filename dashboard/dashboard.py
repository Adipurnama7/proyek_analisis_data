import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df_payment = pd.read_csv("data/order_payments_dataset.csv")
df_sellers = pd.read_csv("data/sellers_dataset.csv")

# Judul Dashboard
st.title("📊 Dashboard Analisis Metode Pembayaran & Aktivitas Penjual")

# **1. Analisis Metode Pembayaran**
st.header("📌 Metode Pembayaran yang Paling Sering Digunakan")

# Hitung jumlah transaksi per metode pembayaran
payment_counts = df_payment["payment_type"].value_counts()

# Tambahkan filter pilihan metode pembayaran
selected_payment = st.selectbox("Pilih metode pembayaran:", payment_counts.index)

# **Filter data berdasarkan pilihan pengguna**
filtered_payment_data = df_payment[df_payment["payment_type"] == selected_payment]

# Buat grafik yang berubah sesuai pilihan
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(payment_counts.index, payment_counts.values, color="skyblue")
ax.set_xlabel("Metode Pembayaran")
ax.set_ylabel("Jumlah Transaksi")
ax.set_title("Distribusi Metode Pembayaran")

# Beri warna khusus pada metode yang dipilih
highlight_color = "red"
ax.bar(selected_payment, payment_counts[selected_payment], color=highlight_color)

# Tampilkan grafik
st.pyplot(fig)

# Informasi tambahan
st.write("**Metode pembayaran yang paling sering digunakan:**", payment_counts.idxmax())
st.write("**Jumlah transaksi tertinggi:**", payment_counts.max())
st.write(f"**Jumlah transaksi untuk {selected_payment}:**", payment_counts[selected_payment])

# **2. Analisis Penjual per Negara Bagian**
st.header("📌 Negara Bagian dengan Penjual Terbanyak")

# Hitung jumlah penjual per negara bagian
seller_counts = df_sellers["seller_state"].value_counts()

# Tambahkan filter pilihan negara bagian
selected_state = st.selectbox("Pilih negara bagian:", seller_counts.index)

# **Filter data berdasarkan pilihan pengguna**
filtered_seller_data = df_sellers[df_sellers["seller_state"] == selected_state]

# Buat visualisasi
fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.bar(seller_counts.index, seller_counts.values, color="skyblue")
ax2.set_xlabel("Negara Bagian")
ax2.set_ylabel("Jumlah Penjual")
ax2.set_title("Distribusi Penjual per Negara Bagian")

# Beri warna khusus pada negara bagian yang dipilih
ax2.bar(selected_state, seller_counts[selected_state], color=highlight_color)

# Tampilkan grafik
st.pyplot(fig2)

# Informasi tambahan
st.write("**Negara bagian dengan jumlah penjual terbanyak:**", seller_counts.idxmax(), f"({seller_counts.max()} penjual)")
st.write(f"**Jumlah penjual di {selected_state}:**", seller_counts[selected_state])
