# Bike Sharing Dashboard 🚲

## Setup Environment

### Menggunakan Anaconda
```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

### Menggunakan Pip & Virtualenv
```bash
python -m venv bike-env
source bike-env/bin/activate  # Linux/macOS
bike-env\Scripts\activate     # Windows
pip install -r requirements.txt
```

## Struktur Direktori
```
bike-dashboard/
├── dashboard/
│   ├── dashboard.py
│   └── requirements.txt
├── dataset/
│   ├── day.csv
│   └── hour.csv
└── README.md
```

## Requirements
Berikut adalah package yang dibutuhkan:
```
streamlit==1.31.0
pandas==2.1.4
numpy==1.24.3
matplotlib==3.7.1
seaborn==0.12.2
```

## Cara Menjalankan Dashboard

1. Pastikan Anda sudah berada di direktori yang benar
```bash
cd dashboard
```

2. Jalankan aplikasi Streamlit
```bash
streamlit run dashboard.py
```

3. Aplikasi akan terbuka di browser dengan alamat:
```
Local URL: http://localhost:8501
Network URL: http://192.168.1.1:8501
```


## Sumber Data
Dataset yang digunakan berasal dari Capital Bikeshare System dengan periode data dari 2011 hingga 2012.

## Contributor
- Ghani Husna Darmawan
- ghanihusna96@gmail.com
- www.linkedin.com/in/ghani-husna-0b0464261
