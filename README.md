# Sistem Pakar Diagnosa Penyakit Ayam (Berbasis Kecerdasan Buatan)

Ini adalah aplikasi desktop yang merupakan salah satu implementasi dari **Kecerdasan Buatan (Artificial Intelligence)**, yang dikembangkan menggunakan Python dan Tkinter untuk mendiagnosa penyakit umum pada ayam. Aplikasi ini berfungsi sebagai **sistem pakar (expert system)**, sebuah cabang dari AI, yang dirancang untuk meniru kemampuan seorang ahli (pakar penyakit ternak) dalam mengambil keputusan.

## Deskripsi

Aplikasi ini memiliki antarmuka pengguna grafis (GUI) yang sederhana. Pengguna akan dihadapkan pada serangkaian pertanyaan mengenai gejala yang dialami oleh ayam. Berdasarkan jawaban yang diberikan, sistem akan menggunakan basis pengetahuan dan mesin inferensi (dengan metode **Certainty Factor**) untuk menghitung kemungkinan setiap penyakit. Hasil akhir yang ditampilkan adalah penyakit dengan persentase keyakinan tertinggi, beserta saran penanganan dan pengobatan yang relevan.

## Fitur Utama

- **Aplikasi Kecerdasan Buatan:** Mengimplementasikan konsep AI dalam bentuk sistem pakar untuk meniru kemampuan seorang ahli dalam mendiagnosa penyakit.
- **Antarmuka Grafis (GUI):** Dibangun dengan Tkinter, menyediakan antarmuka yang mudah digunakan dengan tombol dan jendela interaktif.
- **Metode Certainty Factor:** Menggunakan logika sistem pakar dengan metode Certainty Factor untuk mengakomodasi ketidakpastian dalam jawaban pengguna dan menghasilkan diagnosa dengan tingkat keyakinan (dalam persen).
- **Sesi Tanya Jawab Interaktif:** Aplikasi akan mengajukan pertanyaan satu per satu secara dinamis mengenai gejala-gejala yang ada.
- **Basis Pengetahuan (Knowledge Base):** Memiliki basis pengetahuan internal yang mencakup gejala dan aturan untuk mendiagnosa penyakit berikut:
    - Tipus Ayam
    - Berak Darah (Coccidiosis)
    - Salesma Ayam (Snot)
    - Gumboro
    - Mareks
    - Masalah Produksi Telur
- **Rekomendasi & Solusi:** Setelah diagnosa, aplikasi memberikan informasi tentang penyakit yang terdeteksi, serta saran konkret mengenai pencegahan dan pengobatan yang dapat dilakukan.
- **Mandiri:** Tidak memerlukan instalasi pustaka eksternal, karena hanya menggunakan modul standar Python (`tkinter`, `pathlib`, `random`).

## Teknologi yang Digunakan

- **Python 3:** Bahasa pemrograman utama.
- **Tkinter:** Pustaka standar Python untuk membangun antarmuka pengguna grafis (GUI).
