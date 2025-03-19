import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Supress warning untuk penggunaan pyplot global
st.set_option('deprecation.showPyplotGlobalUse', False)

# Fungsi untuk load data dengan cache menggunakan st.cache_data (versi baru Streamlit)
@st.cache_data
def load_data():
    # Pastikan file CSV berada di direktori yang sama atau atur path-nya sesuai kebutuhan
    orders = pd.read_csv("../dataset/orders_dataset.csv")
    order_reviews = pd.read_csv("../dataset/order_reviews_dataset.csv")
    
    # Cleaning Data: Hapus missing values dan konversi kolom tanggal
    orders.dropna(inplace=True)
    orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
    orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'])
    orders['order_estimated_delivery_date'] = pd.to_datetime(orders['order_estimated_delivery_date'])
    
    # Buat kolom untuk menghitung keterlambatan
    orders['delivery_delay'] = (orders['order_delivered_customer_date'] - orders['order_estimated_delivery_date']).dt.days
    orders['is_late'] = orders['delivery_delay'] > 0
    
    # Merge data orders dan order_reviews berdasarkan 'order_id'
    merged_df = pd.merge(orders, order_reviews, on='order_id', how='inner')
    return orders, merged_df

# Load data
orders, merged_df = load_data()

# Sidebar untuk filter waktu (waktu tertentu) dan pilihan visualisasi
st.sidebar.title("E-Commerce Dataset")
st.sidebar.write("Filter Data Berdasarkan Tahun Pembelian:")

# Ambil tahun dari kolom order_purchase_timestamp
years = orders['order_purchase_timestamp'].dt.year.unique()
year_selected = st.sidebar.multiselect("Pilih Tahun:", options=sorted(years), default=sorted(years))

# Filter data berdasarkan tahun yang dipilih
if year_selected:
    orders = orders[orders['order_purchase_timestamp'].dt.year.isin(year_selected)]
    merged_df = merged_df[merged_df['order_purchase_timestamp'].dt.year.isin(year_selected)]

# Pilihan jenis visualisasi
chart_option = st.sidebar.radio("Pilih Visualisasi:", 
                                ("Boxplot Rating", "Barplot Rating Buruk (<3)", "Histogram Rating", "Heatmap Korelasi"))

# Judul Dashboard
st.title("Analisis Pengaruh Keterlambatan Pengiriman terhadap Rating Pelanggan")
st.write("""
Dashboard ini membantu Anda mengeksplorasi bagaimana keterlambatan pengiriman berpengaruh terhadap rating yang diberikan pelanggan. 
Gunakan filter di sidebar untuk memilih tahun dan visualisasi yang diinginkan.
""")

# Visualisasi Berdasarkan Pilihan
if chart_option == "Boxplot Rating":
    st.subheader("Boxplot: Perbandingan Rating Pesanan Terlambat vs Tepat Waktu")
    fig, ax = plt.subplots(figsize=(8,6))
    sns.boxplot(x=merged_df['is_late'], y=merged_df['review_score'], ax=ax)
    ax.set_xlabel("Apakah Pengiriman Terlambat?")
    ax.set_ylabel("Rating Pelanggan")
    ax.set_title("Perbandingan Rating: Terlambat vs Tepat Waktu")
    st.pyplot(fig)
    
elif chart_option == "Barplot Rating Buruk (<3)":
    st.subheader("Barplot: Proporsi Rating Buruk (<3)")
    fig, ax = plt.subplots(figsize=(8,6))
    sns.barplot(x=merged_df['is_late'], y=(merged_df['review_score'] < 3).astype(int), ax=ax)
    ax.set_xlabel("Apakah Pengiriman Terlambat?")
    ax.set_ylabel("Proporsi Rating Buruk")
    ax.set_title("Kemungkinan Mendapatkan Rating Buruk (<3)")
    st.pyplot(fig)
    
elif chart_option == "Histogram Rating":
    st.subheader("Histogram: Distribusi Rating Pelanggan")
    fig, ax = plt.subplots(figsize=(8,6))
    sns.histplot(merged_df['review_score'], bins=10, kde=True, ax=ax, color="purple")
    ax.set_xlabel("Rating")
    ax.set_ylabel("Frekuensi")
    ax.set_title("Distribusi Rating Pelanggan")
    st.pyplot(fig)
    
elif chart_option == "Heatmap Korelasi":
    st.subheader("Heatmap: Korelasi antara Delivery Delay dan Rating")
    fig, ax = plt.subplots(figsize=(8,6))
    sns.heatmap(merged_df[['delivery_delay', 'review_score']].corr(), annot=True, cmap='coolwarm', ax=ax)
    ax.set_title("Korelasi antara Lama Keterlambatan dan Rating")
    st.pyplot(fig)

# Menambahkan Insight untuk masing-masing visualisasi
st.subheader("Insight dari Visualisasi")
if chart_option == "Boxplot Rating":
    st.write("""
    - Pesanan yang terlambat cenderung memiliki rating yang lebih rendah dibandingkan dengan pesanan tepat waktu.
    - Variasi pada rating menunjukkan adanya perbedaan signifikan antara kedua kelompok, yang mengindikasikan bahwa keterlambatan berdampak negatif pada kepuasan pelanggan.
    """)
elif chart_option == "Barplot Rating Buruk (<3)":
    st.write("""
    - Pesanan yang terlambat memiliki proporsi yang lebih tinggi untuk mendapatkan rating buruk (< 3).
    - Hal ini menandakan bahwa keterlambatan pengiriman meningkatkan risiko penurunan kepuasan pelanggan.
    """)
elif chart_option == "Histogram Rating":
    st.write("""
    - Histogram menunjukkan distribusi keseluruhan rating pelanggan, memberikan gambaran umum tentang kepuasan pelanggan.
    - Dengan adanya distribusi ini, kita dapat melihat apakah sebagian besar pelanggan memberikan rating tinggi atau rendah.
    """)
elif chart_option == "Heatmap Korelasi":
    st.write("""
    - Heatmap menunjukkan korelasi negatif antara lama keterlambatan (delivery_delay) dan rating pelanggan.
    - Semakin lama keterlambatan, cenderung semakin rendah rating yang diberikan, menguatkan hipotesis bahwa waktu pengiriman berpengaruh pada kepuasan pelanggan.
    """)
