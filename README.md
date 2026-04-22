# 🧠 Prediksi Kekuatan Tekan Beton Menggunakan Algoritma CatBoost Regressor

Aplikasi ini merupakan implementasi model Machine Learning untuk memprediksi **Kekuatan Tekan Beton (Concrete Compressive Strength)** berdasarkan komposisi material penyusunnya.

Aplikasi ini dibangun menggunakan **Streamlit** dan dapat diakses secara online.

---

## 🚀 Demo Aplikasi

🔗 [https://prediksi-kekuatan-beton-catboost-saskya.streamlit.app/](https://prediksi-kekuatan-beton-catboost-saskya.streamlit.app/)

---

## 📊 Deskripsi Proyek

Proyek ini bertujuan untuk:

* Menganalisis dataset kekuatan tekan beton
* Membangun model prediksi menggunakan beberapa algoritma Machine Learning
* Membandingkan performa model
* Melakukan tuning untuk meningkatkan akurasi
* Mendeploy model dalam bentuk aplikasi web interaktif

---

## 🧩 Dataset

Dataset yang digunakan adalah:

* **Concrete Compressive Strength Dataset**
* Target: `Concrete compressive strength (MPa)`
* Fitur:

  * Cement
  * Blast Furnace Slag
  * Fly Ash
  * Water
  * Superplasticizer
  * Coarse Aggregate
  * Fine Aggregate
  * Age

---

## ⚙️ Tahapan Machine Learning

### 1. Data Understanding

* Analisis fitur dan target
* Statistik deskriptif

### 2. Data Preprocessing

* Standarisasi menggunakan `StandardScaler`
* Penanganan data

### 3. Exploratory Data Analysis (EDA)

* Visualisasi distribusi data
* Analisis korelasi antar fitur

### 4. Data Splitting

Menggunakan beberapa rasio:

* 50:50
* 60:40
* 70:30
* 80:20
* 90:10

### 5. Model Building

Menggunakan 3 algoritma:

* CatBoost Regressor
* XGBoost Regressor
* LightGBM Regressor

### 6. Hyperparameter Tuning

* Menggunakan `RandomizedSearchCV`

### 🔧 Optimasi Model Lanjutan

Untuk meningkatkan performa model, dilakukan teknik optimasi lanjutan pada algoritma CatBoost, yaitu:

* **Early Stopping**
  Menghentikan proses training lebih awal jika performa model tidak lagi meningkat pada data validasi, sehingga mencegah overfitting.

* **Over-Iteration (peningkatan jumlah iterasi)**
  Jumlah iterasi dinaikkan untuk memberikan kesempatan model belajar lebih dalam, dengan tetap dikontrol oleh early stopping.

Teknik ini berhasil meningkatkan performa model dari:

* R² ≈ 0.946 → R² ≈ 0.950

Sehingga model memenuhi target performa yang ditentukan (R² ≥ 0.95).

### 7. Model Evaluation

Menggunakan metrik:

* MAE
* MSE
* RMSE
* R² Score

### 8. Model Comparison

* Perbandingan performa tiap model dan tiap data split

---

## 🏆 Hasil Terbaik

Model terbaik:

* **Algoritma**: CatBoost Regressor
* **Data Split**: 80% Training – 20% Testing
* **R² Score**: **0.9504** ✅

Model berhasil memenuhi ketentuan:

* ≥ 95% akurasi (R² ≥ 0.95)

---

## ▶️ Cara Menjalankan Aplikasi Secara Lokal

### 1. Clone Repository

```bash
git clone https://github.com/username/prediksi-kekuatan-beton.git
cd nama-repository
```

### 2. Buat Virtual Environment (Opsional tetapi Disarankan)

```bash
python -m venv venv
```

Aktifkan virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### 3. Install Semua Dependency

```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi Streamlit

```bash
streamlit run app.py
```

### 5. Buka di Browser

Setelah berhasil dijalankan, Streamlit akan menampilkan alamat seperti berikut:

```bash
Local URL: http://localhost:8501
```

Buka alamat tersebut di browser untuk menggunakan aplikasi.

---

## 📁 Struktur File yang Dibutuhkan

```text
├── app.py
├── catboost_model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
└── Concrete_Data.xls (opsional)
```

Keterangan:

* `app.py` → file utama aplikasi Streamlit
* `catboost_model.pkl` → model CatBoost yang sudah dilatih
* `scaler.pkl` → objek StandardScaler yang digunakan saat training
* `requirements.txt` → daftar library yang harus diinstall
* `Concrete_Data.xls` → dataset asli, opsional jika ingin melakukan training ulang

---

## 🖥️ Teknologi yang Digunakan

* Python
* Streamlit
* Scikit-learn
* CatBoost
* Pandas
* NumPy
* Joblib

---
