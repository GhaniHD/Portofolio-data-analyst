import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Setup tampilan
st.set_page_config(page_title="Bike Rental Analysis", layout="wide")

# CSS sederhana
st.markdown("""
    <style>
    .main { padding: 20px; }
    h1 { color: #2c3e50; text-align: center; padding: 20px; }
    h2 { color: #34495e; padding: 10px 0; }
    </style>
""", unsafe_allow_html=True)

# Judul
st.title('Analisis Penyewaan Sepeda 🚲')
st.markdown('---')

# Load data
@st.cache_data
def load_data():
    try:
        day_df = pd.read_csv('../dataset/day.csv')
        hour_df = pd.read_csv('../dataset/hour.csv')
        day_df['dteday'] = pd.to_datetime(day_df['dteday'])
        hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
        return day_df, hour_df
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None, None

day_df, hour_df = load_data()

if day_df is not None and hour_df is not None:
    # Filter musim di sidebar
    st.sidebar.header('Filter Data')
    seasons = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
    selected_season = st.sidebar.selectbox(
        'Pilih Musim',
        options=list(seasons.keys()),
        format_func=lambda x: seasons[x]
    )
    
    # Filter data
    filtered_day_df = day_df[day_df['season'] == selected_season]
    
    # Visualisasi baris 1
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader('Tren Penyewaan Harian')
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(data=filtered_day_df, x='dteday', y='cnt', ax=ax)
        plt.xticks(rotation=45)
        plt.title(f'Tren Penyewaan Sepeda - {seasons[selected_season]}')
        plt.xlabel('Tanggal')
        plt.ylabel('Jumlah Penyewaan')
        st.pyplot(fig)
        plt.close()

    with col2:
        st.subheader('Pengaruh Temperatur')
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(data=filtered_day_df, x='temp', y='cnt', ax=ax)
        plt.title('Hubungan Temperatur dan Jumlah Penyewaan')
        plt.xlabel('Temperatur (Normalisasi)')
        plt.ylabel('Jumlah Penyewaan')
        st.pyplot(fig)
        plt.close()

    # Visualisasi baris 2
    st.markdown('---')
    col3, col4 = st.columns(2)

    with col3:
        st.subheader('Pola Penyewaan per Hari')
        daily_avg = hour_df.groupby('weekday')['cnt'].mean().reset_index()
        daily_avg['weekday'] = daily_avg['weekday'].map({
            0: 'Sen', 1: 'Sel', 2: 'Rab', 3: 'Kam',
            4: 'Jum', 5: 'Sab', 6: 'Min'
        })
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(data=daily_avg, x='weekday', y='cnt', ax=ax)
        plt.title('Rata-rata Penyewaan per Hari')
        plt.xlabel('Hari')
        plt.ylabel('Rata-rata Penyewaan')
        st.pyplot(fig)
        plt.close()

    with col4:
        st.subheader('Pengaruh Cuaca')
        weather_map = {1: 'Cerah', 2: 'Berawan', 3: 'Hujan Ringan', 4: 'Hujan Lebat'}
        day_df['weather_label'] = day_df['weathersit'].map(weather_map)
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(data=day_df, x='weather_label', y='cnt', ax=ax)
        plt.title('Distribusi Penyewaan Berdasarkan Cuaca')
        plt.xlabel('Kondisi Cuaca')
        plt.ylabel('Jumlah Penyewaan')
        plt.xticks(rotation=45)
        st.pyplot(fig)
        plt.close()

    # Metrik-metrik
    st.markdown('---')
    st.subheader('Metrik Utama')
    col5, col6, col7, col8 = st.columns(4)

    with col5:
        st.metric("Total Penyewaan", f"{filtered_day_df['cnt'].sum():,}")
    with col6:
        st.metric("Rata-rata Harian", f"{filtered_day_df['cnt'].mean():.0f}")
    with col7:
        st.metric("Penyewaan Tertinggi", f"{filtered_day_df['cnt'].max():,}")
    with col8:
        growth = ((filtered_day_df['cnt'].iloc[-1] - filtered_day_df['cnt'].iloc[0]) / 
                 filtered_day_df['cnt'].iloc[0] * 100)
        st.metric("Pertumbuhan", f"{growth:.1f}%")

    # Pola per jam
    st.markdown('---')
    st.subheader('Pola Penyewaan per Jam')
    hourly_pattern = hour_df.groupby('hr')['cnt'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(15, 6))
    sns.lineplot(data=hourly_pattern, x='hr', y='cnt', ax=ax)
    plt.title('Rata-rata Penyewaan per Jam')
    plt.xlabel('Jam')
    plt.ylabel('Rata-rata Penyewaan')
    st.pyplot(fig)
    plt.close()

    # Insights
    st.markdown('---')
    st.subheader('Insights Utama')
    col9, col10 = st.columns(2)

    with col9:
        st.markdown("""
        #### Pola Temporal:
        - Jam tersibuk adalah saat jam berangkat (8-9) dan pulang kerja (17-18)
        - Akhir pekan memiliki pola penyewaan yang berbeda dengan hari kerja
        - Musim panas menunjukkan tingkat penyewaan tertinggi
        """)

    with col10:
        st.markdown("""
        #### Faktor Pengaruh:
        - Cuaca cerah berkorelasi dengan tingkat penyewaan yang lebih tinggi
        - Temperatur memiliki pengaruh positif terhadap jumlah penyewaan
        - Hari libur cenderung memiliki pola penyewaan yang berbeda
        """)

else:
    st.error("Gagal memuat data. Pastikan file dataset tersedia di path yang benar.")