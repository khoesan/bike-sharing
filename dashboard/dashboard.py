import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data hasil cleaning
@st.cache_data  # Cache agar tidak membaca ulang setiap kali dijalankan
def load_data():
    df = pd.read_csv("dashboard/main_data.csv")
    return df

df = load_data()

# Judul Dashboard
st.title("📊 Dashboard Penyewaan Sepeda")

# Tambahkan deskripsi
st.markdown("Dashboard ini menampilkan analisis data penyewaan sepeda berdasarkan musim dan kondisi cuaca.")

# Sidebar untuk filter
st.sidebar.header("Filter Data")
season_filter = st.sidebar.selectbox("Pilih Musim", ["All", "Spring", "Summer", "Fall", "Winter"])

# Filter data berdasarkan musim
if season_filter != "All":
    df = df[df["season"] == season_filter]

# --- 1. Visualisasi Pengaruh Musim ---
st.subheader("🚴 Penyewaan Sepeda Berdasarkan Musim")

# Hitung total penyewaan per musim
season_rentals = df.groupby("season")["cnt"].sum().reset_index()

# Buat barplot
fig, ax = plt.subplots()
sns.barplot(x="season", y="cnt", data=season_rentals, palette="coolwarm", ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Total Penyewaan Sepeda")
ax.set_title("Pengaruh Musim terhadap Penyewaan Sepeda")

# Tampilkan di Streamlit
st.pyplot(fig)

# --- 2. Visualisasi Pengaruh Cuaca ---
st.subheader("🌦️ Penyewaan Sepeda Berdasarkan Kondisi Cuaca")

# Hitung total penyewaan per kondisi cuaca
weather_rentals = df.groupby("weathersit")["cnt"].sum().reset_index()

# Buat barplot
fig, ax = plt.subplots()
sns.barplot(x="weathersit", y="cnt", data=weather_rentals, palette="viridis", ax=ax)
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Total Penyewaan Sepeda")
ax.set_title("Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda")

# Tampilkan di Streamlit
st.pyplot(fig)
