# Proyek Analisis Data E-Commerce

## Deskripsi Proyek

Proyek ini merupakan **analisis data e-commerce** menggunakan dataset publik yang berisi informasi transaksi penjualan online. Analisis bertujuan untuk memahami **kinerja penjualan, perilaku pelanggan, dan hubungan antar entitas dataset** melalui eksplorasi data, visualisasi, dan penggabungan beberapa tabel sumber.

Notebook ini dibuat oleh:

* **Nama:** Ghani Husna Darmawan
* **Email:** [ghanihusna96@gmail.com](mailto:ghanihusna96@gmail.com)
* **ID Dicoding:** ghanihd

---

## Tujuan Analisis

Secara garis besar, proyek ini bertujuan untuk menjawab pertanyaan-pertanyaan bisnis seperti:

1. **Bagaimana struktur data penjualan e-commerce dan relasi antar dataset?**
2. **Apa insight yang dapat diperoleh dari pelanggan, produk, pembayaran, dan ulasan?**
3. **Bagaimana keterlambatan pengiriman mempengaruhi rating pelanggan?**

Pertanyaan-pertanyaan ini membantu untuk memahami faktor-faktor yang memengaruhi kinerja penjualan dan kepuasan pelanggan secara data-driven.

---

## Dataset Sumber

Dataset terdiri dari **beberapa file CSV** yang saling terhubung:

| File                                    | Deskripsi                          |
| --------------------------------------- | ---------------------------------- |
| `customers_dataset.csv`                 | Informasi pelanggan                |
| `geolocation_dataset.csv`               | Lokasi geografis wilayah pelanggan |
| `orders_dataset.csv`                    | Daftar pesanan                     |
| `order_items_dataset.csv`               | Detail item per pesanan            |
| `order_payments_dataset.csv`            | Informasi pembayaran               |
| `order_reviews_dataset.csv`             | Ulasan dan rating pelanggan        |
| `products_dataset.csv`                  | Data produk                        |
| `product_category_name_translation.csv` | Nama kategori terjemahan           |
| `sellers_dataset.csv`                   | Informasi penjual                  |

Semua dataset digabungkan untuk membentuk pandangan menyeluruh atas transaksi e-commerce. ([GitHub][1])

---

## Tools & Library

Analisis dilakukan menggunakan:

* **Python**
* Pandas & NumPy → manipulasi data
* Matplotlib & Seaborn → visualisasi
* Google Colab → lingkungan pemrograman interaktif ([GitHub][1])

---

## Tahapan Analisis

### 1. **Import & Loading Data**

Semua dataset diimpor dari Google Drive untuk kemudian dianalisis bersama. ([GitHub][1])

### 2. **Eksplorasi Dasar**

Menampilkan **head** dari setiap tabel untuk memahami struktur, tipe data, dan konten awal. Ini membantu dalam menentukan langkah preprocessing selanjutnya. ([GitHub][1])

### 3. **Data Wrangling**

Dataset yang awalnya terpisah-pisah kemudian digabungkan untuk analisis relasional — seperti menghubungkan pelanggan dengan pesanan, produk, dan rating mereka.

### 4. **Analisis Pertanyaan Bisnis**

Hal utama yang dianalisis dalam notebook:

* Hubungan antara **waktu pengiriman dan rating pelanggan**
* Distribusi nilai ulasan / rating
* Pola pembayaran vs kategori produk
* Hubungan lokasi pelanggan dengan produk yang dibeli

---

## Insight & Temuan Utama

Berikut adalah insight utama dari analisis (ringkasan karena notebook berisi beberapa grafik dan tabel):

- **Struktur dataset sangat relasional** — setiap entitas terkait, memungkinkan analisis kompleks seperti:

* pelanggan → pesanan → ulasan → produk. ([GitHub][1])

- **Rating pelanggan dipengaruhi oleh faktor pengiriman**
Analisis awal menunjukkan bahwa keterlambatan pengiriman memilik efek terhadap rating yang diberikan oleh pelanggan.

- **Beberapa hubungan penting di data:**

* Produk tertentu memiliki rating rata-rata lebih tinggi
* Kategori pembayaran tertentu dapat berkorelasi dengan nilai ulasan
* Pelanggan dari lokasi tertentu cenderung memberi rating tertentu

---

## Struktur Repository

```
E-commerce/
├── data/                            # Dataset CSV yang digunakan
├── Analisis_Data_Ecommerce.ipynb    # Notebook analisis
├── visuals/                         # Visualisasi & grafik output
├── README.md                        # Dokumentasi proyek
```

---

##  Visualisasi Contoh

Visualisasi yang dihasilkan dalam notebook mencakup:

* **Distribusi rating pelanggan**
* **Frekuensi keterlambatan pengiriman vs rating rendah**
* **Top produk & kategori berdasarkan jumlah penjualan**
* **Peta lokasi pelanggan (jika dibuat)**

(Grafik-grafik ini ada di dalam notebook sebagai bagian dari visualisasi eksplorasi.)

---

## Rekomendasi Selanjutnya

Berdasarkan temuan dari analisis ini, langkah lanjutan yang bisa dikembangkan:

1. **Segmentasi pelanggan** untuk strategi pemasaran
2. **Model prediksi rating** berdasarkan fitur order/payments
3. **Analisis churn pelanggan**
4. **Dashboard interaktif** menggunakan Power BI / Tableau

---

## Penulis

**Ghani Husna Darmawan**
Data Analyst • Mahasiswa Informatika
Email: [ghanihusna96@gmail.com](mailto:ghanihusna96@gmail.com)
