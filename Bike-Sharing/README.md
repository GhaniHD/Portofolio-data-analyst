# Proyek Analisis Data — Bike Sharing Dataset

## Deskripsi Proyek

Analisis ini dilakukan pada **Bike Sharing Dataset** yang berisi data penyewaan sepeda harian dan per jam untuk memahami pola penggunaan sepeda berdasarkan faktor **cuaca, musim, dan waktu**.
Proyek ini menunjukkan kemampuan dalam **eksplorasi data, pembersihan data, dan penarikan insight bisnis** dari dataset nyata. ([GitHub][1])

**Notebook:** `Analisis_Data_Bike_Sharing.ipynb`
**Penulis:** Ghani Husna Darmawan
**Email:** [ghanihusna96@gmail.com](mailto:ghanihusna96@gmail.com)

---

## Pertanyaan Bisnis

Analisis ini berfokus pada menjawab dua pertanyaan utama:

1. **Bagaimana pengaruh kondisi cuaca dan musim terhadap tingkat penyewaan sepeda?**
2. **Apakah ada jam tertentu dalam sehari yang memiliki tingkat penyewaan sepeda tertinggi?** ([GitHub][2])

---

## Tools yang Digunakan

Analisis dilakukan dengan menggunakan:

* **Python**
* `pandas`, `numpy` → manipulasi data
* `matplotlib`, `seaborn` → visualisasi
* Google Colab → lingkungan interaktif untuk notebook ([GitHub][2])

---

## Dataset

Proyek ini menggunakan dua dataset utama dari Bike Sharing Dataset:

| Dataset      | Deskripsi                         |
| ------------ | --------------------------------- |
| **day.csv**  | Data penyewaan sepeda setiap hari |
| **hour.csv** | Data penyewaan sepeda setiap jam  |

Kedua file tersebut berisi informasi seperti tanggal, musim, kondisi cuaca, jumlah penyewaan (total dan menurut jenis pengguna), dan indikator hari libur. ([GitHub][2])

---

## Tahapan Analisis

### 1. **Import Library**

Semua library yang dibutuhkan di-import, termasuk library visualisasi dan manipulasi data. ([GitHub][2])

### 2. **Load Dataset**

Dataset `day.csv` dan `hour.csv` dimuat ke dalam DataFrame pandas dari Google Drive. ([GitHub][2])

### 3. **Exploratory Data Analysis (EDA)**

Analisis awal dilakukan dengan melihat:

* **Informasi struktur data dan tipe kolom**
* **Statistik deskriptif**
* **Pengecekan missing values** yang tidak ditemukan pada kedua dataset ([GitHub][2])

### 4. **Data Wrangling**

* Dataset dibersihkan dari duplikasi
* Tidak ditemukan nilai null → siap lanjut analisis ([GitHub][2])

---

## Insight & Temuan Utama

### Tidak Ada Nilai Kosong

Kedua dataset telah bersih dari nilai null, sehingga siap dianalisis tanpa langkah imputasi ekstra. ([GitHub][2])

### Pola Penyewaan Sepeda

* Pada **dataset harian**, rata-rata total penyewaan sepeda mencapai ribuan per hari.
* Pada **dataset per jam**, jumlah rata-rata penyewaan jauh lebih rendah karena granularitasnya lebih halus. ([GitHub][2])

Ini menunjukkan bahwa tingkat penggunaan sepeda sangat bergantung pada **waktu dan jam tertentu dalam sehari**. ([GitHub][2])

### Komposisi Pengguna

Mayoritas penyewa adalah **pengguna terdaftar (registered)** dibanding pengguna kasual (casual) pada hampir semua periode penyewaan, menunjukkan tingginya keterlibatan pelanggan tetap di sistem bike sharing. ([GitHub][2])

---

## Struktur Repository

```
Bike-Sharing/
├── data/                          # Dataset CSV (day.csv & hour.csv)
├── Analisis_Data_Bike_Sharing.ipynb   # Notebook analisis
└── README.md                     # Dokumentasi proyek
```

---

## Visualisasi yang Dihasilkan

Notebook ini memuat visualisasi seperti:

 - Perbandingan penyewaan sepeda per jam
 - Perbandingan penyewaan berdasarkan musim
 - Distribusi jumlah penyewaan harian vs per jam
 - nalisis durasi & kondisi cuaca terhadap jumlah penyewaan ([GitHub][1])

---

## Kesimpulan

Analisis Bike Sharing Dataset menunjukkan bahwa:

* **Musim dan cuaca mempengaruhi jumlah penyewaan sepeda**
* **Jam sibuk dalam sehari memiliki puncak penyewaan lebih tinggi**
* **Data bersih dan statistik deskriptif memberikan gambaran awal yang kuat tentang pola penggunaan sepeda**

---

## Rekomendasi Selanjutnya

Untuk analisis lanjutan, kamu bisa:

- Membuat **Model Prediksi Jumlah Penyewaan** berdasarkan cuaca dan waktu
- Menambah **Segmentasi Pengguna** berdasarkan jenis pengguna
- Membuat **Dashboard Interaktif** (misalnya dengan Streamlit atau Power BI) untuk visualisasi real-time

---

## Penulis

**Ghani Husna Darmawan**
[ghanihusna96@gmail.com](mailto:ghanihusna96@gmail.com)
