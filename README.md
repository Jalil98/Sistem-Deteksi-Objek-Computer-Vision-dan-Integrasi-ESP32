# Sistem-Deteksi-Objek-Computer-Vision-dan-Integrasi-ESP32

## 1. Gambaran Umum Sistem

Proyek ini mengimplementasikan sistem Computer Vision yang mampu mendeteksi objek secara real-time menggunakan model Machine Learning yang telah dilatih. Sistem ini terintegrasi dengan mikrokontroler ESP32 (disimulasikan) untuk mendemonstrasikan komunikasi antara Computer Vision dan sistem embedded.

Sistem ini mendeteksi dua kelas objek:

* Botol (Bottle)
* Handphone (Mobile Phone)

Ketika objek terdeteksi, sistem Computer Vision akan mengirim sinyal ke ESP32, dan ESP32 akan merespon dengan data sensor (simulasi).

Sistem ini dikembangkan dan diuji menggunakan laptop dan webcam, serta dirancang agar sepenuhnya kompatibel dengan Raspberry Pi 4 dan Raspberry Pi 5.

---

## 2. Arsitektur Sistem

```id="arsitek1"
Webcam
   ↓
Computer Vision (Python + OpenCV + YOLOv8)
   ↓
Deteksi Objek (Bounding Box + Label)
   ↓
Mengirim sinyal ke ESP32 (Simulasi Serial)
   ↓
ESP32 membaca sensor (Simulasi)
   ↓
ESP32 mengirim respon
   ↓
Respon ditampilkan di terminal
```

---

## 3. Dataset

### Sumber Dataset

Dataset dibuat dari rekaman video yang diambil menggunakan kamera smartphone. Video tersebut kemudian dipecah menjadi gambar individual menggunakan Roboflow.

Metode ini memastikan skenario deteksi yang realistis dengan variasi:

* Kondisi pencahayaan
* Sudut objek
* Jarak objek
* Latar belakang yang berbeda

### Ringkasan Dataset

| Deskripsi                      | Nilai                  |
| ------------------------------ | ---------------------- |
| Total gambar dikumpulkan       | 468 gambar             |
| Total gambar berhasil dilabeli | 459 gambar             |
| Jumlah kelas                   | 2 (Bottle, Phone)      |
| Jumlah gambar per kelas        | > 200 gambar per kelas |
| Tool labeling                  | Roboflow               |
| Format anotasi                 | YOLO format            |

### Pembagian Dataset

| Dataset  | Persentase | Perkiraan jumlah |
| -------- | ---------- | ---------------- |
| Training | 70%        | ~321 gambar      |
| Validasi | 10%        | ~46 gambar       |
| Testing  | 20%        | ~92 gambar       |

---

## 4. Proses Labeling Data

Seluruh gambar dilabeli secara manual menggunakan tool anotasi Roboflow.

Setiap objek diberi:

* Bounding box
* Label kelas yang sesuai

Contoh anotasi:

* Bottle → bounding box pada botol
* Phone → bounding box pada handphone

Format anotasi yang digunakan: YOLO format

link dataset: -> [Dataset](https://app.roboflow.com/classify-bottle-and-hp/my-first-project-ibrjv/browse?queryText=&pageSize=50&startingIndex=0&browseQuery=true)

---

## 5. Training Model

### Model yang digunakan

YOLOv8n (Ultralytics)

Alasan pemilihan YOLOv8:

* Ringan dan cepat
* Akurasi tinggi
* Kompatibel dengan Raspberry Pi
* Mendukung deteksi real-time
* Mudah di-deploy

### Konfigurasi Training

| Parameter          | Nilai              |
| ------------------ | ------------------ |
| Model              | YOLOv8n            |
| Epoch              | 20                 |
| Ukuran gambar      | 640                |
| Framework          | Ultralytics YOLOv8 |
| Perangkat training | Laptop             |

### Waktu Training

Training selesai dalam waktu kurang dari 60 menit sesuai requirement.

---

## 6. Performa Model

Hasil training:

| Metric    | Hasil |
| --------- | ----- |
| mAP@50    | 99.6% |
| Precision | 100%  |
| Recall    | 95.4% |

Interpretasi:

* mAP@50 sebesar 99.6% menunjukkan akurasi deteksi yang sangat tinggi
* Precision 100% menunjukkan tidak ada false positive
* Recall 95.4% menunjukkan model mampu mendeteksi hampir semua objek

<img width="1489" height="862" alt="image" src="https://github.com/user-attachments/assets/707e43b7-dbc2-45c0-aacf-cfe406c79b19" />


Model sangat andal dan stabil.

---

## 7. Implementasi Computer Vision

Sistem Computer Vision melakukan:

* Capture video dari webcam secara real-time
* Deteksi objek menggunakan model yang telah dilatih
* Menampilkan bounding box
* Menampilkan label objek
* Mengirim sinyal ke ESP32 simulator

Library yang digunakan:

* Python
* OpenCV
* Ultralytics YOLOv8
* NumPy

---

## 8. Integrasi ESP32

Karena perangkat ESP32 fisik tidak tersedia, ESP32 disimulasikan menggunakan program Python.

ESP32 simulator berfungsi untuk:

* Menerima sinyal dari sistem Computer Vision
* Mensimulasikan pembacaan sensor
* Mengirim respon kembali ke sistem Computer Vision

Metode komunikasi:

Simulasi Serial Communication

Arsitektur ini dapat langsung diterapkan ke ESP32 fisik tanpa perubahan besar.

---

## 9. Kompatibilitas Raspberry Pi

Sistem ini sepenuhnya kompatibel dengan:

* Raspberry Pi 4
* Raspberry Pi 5

Karena menggunakan:

* Python
* OpenCV
* YOLOv8n (model ringan)
* USB Camera atau Pi Camera

Perubahan yang diperlukan sangat minimal.

---

## 10. Cara Menjalankan Program

Buat Environment di bash:

```id="run1"
conda create -n yolo
```
aktifkan Environment yang sudah dibuat di bash:

```id="run1"
conda activate yolo
```

Install python:

```id="run1"
pip install python==3.9
```
Install Python Library:

```id="run1"
pip install ultralytics opencv-python pyserial numpy
```

Install dependency:

```id="run1"
pip install -r requirements.txt
```

Jalankan ESP32 simulator:

```id="run2"
python esp32_simulator.py
```

Jalankan sistem Computer Vision:

```id="run3"
python cv_detect.py
```

Output:


https://github.com/user-attachments/assets/2f6c6c17-e995-40e8-bf80-a46d3ecdd632


---

## 11. Struktur Project

```id="struct1"
project/
│
├── dataset/
├── model/
│   └── best.pt
│
├── cv_detect.py
├── esp32_simulator.py
├── train_model.py
├── requirements.txt
├── README.md
└── demo_video.mp4
```

---

## 12. Kendala dan Solusi

### Kendala

Tidak tersedia perangkat Raspberry Pi dan ESP32 fisik.

### Solusi

Sistem dikembangkan dan diuji menggunakan laptop, webcam, dan ESP32 simulator.

Struktur software dirancang agar dapat langsung dijalankan pada Raspberry Pi dan ESP32 fisik.

---

## 13. Kesimpulan

Proyek ini berhasil mengimplementasikan:

* Pembuatan dataset sendiri
* Pelabelan data secara manual
* Training model Machine Learning
* Deteksi objek secara real-time
* Integrasi Computer Vision dengan sistem embedded
* Arsitektur yang siap deploy ke Raspberry Pi dan ESP32

Model mencapai akurasi yang sangat tinggi dan siap digunakan pada sistem nyata.

---

