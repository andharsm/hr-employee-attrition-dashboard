# **Model Prediksi & Dashboard Employee Attrition**

## **Business Understanding**

Employee attrition, atau tingkat pengunduran diri karyawan, merupakan isu penting yang dihadapi banyak organisasi di berbagai industri. Tingginya tingkat pengunduran diri dapat mengakibatkan peningkatan biaya rekrutmen dan pelatihan, penurunan produktivitas, serta hilangnya pengetahuan dan keterampilan yang berharga. Oleh karena itu, memahami faktor-faktor yang mempengaruhi employee attrition dan mengembangkan model prediksi yang efektif menjadi sangat krusial bagi keberlanjutan dan kesuksesan organisasi.

Model prediksi employee attrition dapat membantu organisasi mengidentifikasi karyawan yang berisiko tinggi untuk meninggalkan perusahaan. Dengan menggunakan pendekatan berbasis data dan machine learning, organisasi dapat mengambil tindakan preventif yang tepat, seperti menyediakan program retensi, menawarkan insentif, atau melakukan intervensi lainnya yang dapat mengurangi tingkat pengunduran diri. Prediksi yang akurat juga memungkinkan manajemen sumber daya manusia untuk membuat keputusan yang lebih baik dalam hal perencanaan tenaga kerja dan pengelolaan bakat.

Dashboard employee attrition merupakan alat visualisasi yang penting untuk menyajikan data dan hasil prediksi dengan cara yang mudah dipahami oleh para pengambil keputusan. Dengan menggunakan dashboard, manajer HR dapat memantau tren attrition secara real-time, mengevaluasi efektivitas strategi retensi, serta mengidentifikasi area yang memerlukan perhatian lebih lanjut. Dashboard yang interaktif dan user-friendly memungkinkan pengguna untuk melakukan analisis mendalam dan eksplorasi data secara mandiri, sehingga mendukung pengambilan keputusan yang lebih cepat dan berbasis data.

Penelitian ini bertujuan untuk mengembangkan model prediksi employee attrition yang akurat dan membangun dashboard interaktif untuk memantau dan menganalisis tingkat pengunduran diri karyawan. Proses pengembangan model akan mencakup eksplorasi dan analisis data karyawan, seleksi fitur yang relevan, penerapan algoritma machine learning, serta evaluasi kinerja model. Sementara itu, pembuatan dashboard akan melibatkan desain dan implementasi visualisasi data yang intuitif dan informatif.

### Permasalahan Bisnis

Beberapa masalah yang dapat ditimbulkan akbiat rasio attrition yang tinggi, seperti:
* Penurunan produktivitas selama masa transisi dan adaptasi karyawan baru
* Terhambatnya proyek akibat pergantian personel, beban kerja tambahan pada karyawan yang tersisa.
* Secara sosial akan berdampak pada reputasi perusahaan, persepsi negatif dari calon karyawan potensial serta potensi penurunan kepercayaan pelanggan dan mitra bisnis

### Cakupan Proyek

* Analisis dan prediksi employee attrition
* Pengembangan model machine learning untuk memprediksi attrition
* Evaluasi dan pemilihan model terbaik
* Prediksi attrition untuk data yang belum berlabel
* Persiapan data untuk pembuatan dashboard
* Analisa Dashboard

## **Penerapan Prediksi dengan Machine Learning**

#### Sumber Data
Dataset yang digunakan adalah data employee attrition yang disediakan oleh Dicoding pada learning path Data Science kelas [Belajar Penerapan Data Science](https://www.dicoding.com/academies/590-belajar-penerapan-data-science).

#### Setup Environment
##### 1. Setup Environment di Lokal:
a. Pastikan Python sudah terinstal di komputer Anda (disarankan Python 3.7+).
b. Buat virtual environment (opsional tapi direkomendasikan):
```
python -m venv myenv
source myenv/bin/activate  # Untuk Unix atau MacOS
myenv\Scripts\activate  # Untuk Windows
```
c. Instalasi requirements:
Buat file requirements.txt dengan konten berikut:
```
pandas
numpy
matplotlib
seaborn
scikit-learn
xgboost
```
Kemudian jalankan:
```
pip install -r requirements.txt
```
Kemudian install library yang dibutuhkan

##### 2. Setup Environment di Google Colab:
Google Colab sudah menyediakan sebagian besar library yang dibutuhkan. Namun, untuk memastikan semua library tersedia dan up-to-date:
Di cell pertama notebook Colab, jalankan:
```
!pip install --upgrade pandas numpy matplotlib seaborn scikit-learn xgboost
```
Kemudian install library yang dibutuhkan

### Membuat Model Machine Learning
#### Persiapan Data
- Mengimpor dan memuat dataset employee attrition dari sumber yang disediakan.
- Memeriksa informasi umum dataset dan melakukan deskripsi data numerik serta kategorikal.
- Mengidentifikasi dan menangani data duplikat serta nilai yang hilang (missing values).

#### Analisis Data Eksploratif (EDA):
- Analisis univariat dan multivariat untuk mengidentifikasi faktor-faktor kunci yang berkontribusi pada attrition karyawan.
- Visualisasi data untuk mendapatkan insight yang lebih mendalam tentang hubungan antara variabel-variabel dalam dataset.

 #### Prapemrosesan Data
   - Memisahkan dataset menjadi data train, test, dan validation. Data validation adalah data dengan attrition = null, data akan digunakan untuk model inference dan mendapatkan prediksi dan menggantikan missing value.
   - Melakukan encoding pada kolom kategori.
   - Melakukan feature selection menggunakan Random Forest untuk memilih fitur yang relevan.
   - Membuat 2 kombinasi dataset, data original dan data feature selected.

#### Pembangunan Model
   - Melatih model menggunakan beberapa algoritma seperti RandomForest, DecisionTree, dan XGBoost.
   - Melakukan tuning hyperparameter dengan GridSearchCV.
   - Mengevaluasi kinerja model menggunakan metrik seperti accuracy, precision, recall, f1-score, dan confusion matrix.

#### Prediksi
- Menggunakan model terbaik (XGBoost dengan dataset original) untuk memprediksi attrition pada data validasi


#### Persiapan data untuk dashboard
- Menggabungkan data train, test, dan validasi yang sudah diprediksi
- Mengkonversi kembali label-encoded data ke format aslinya
- Menyimpan dataset final dalam format CSV untuk digunakan dalam pembuatan dashboard

## **Business Dashboard**

Dashboard dibuat pada platform Looker Studio, dan dapat diakses pada [Dashboard HR Employee Attrition](https://lookerstudio.google.com/reporting/f5dc6f92-f031-450f-8537-dc27e4ec2907)

### Overview
* Attrition Rate: Menunjukkan persentase karyawan yang meninggalkan perusahaan dalam periode tertentu. Dalam dashboard ini, attrition rate adalah 15,58%.
* Total Attrition: Jumlah total karyawan yang telah meninggalkan perusahaan, yaitu 229 orang.
* Current Employee: Jumlah karyawan yang masih aktif bekerja di perusahaan, yaitu 1.470 orang.

### Department
* R&D, HR, Sales: Visualisasi ini menunjukkan jumlah karyawan yang tetap (No) dan yang pergi (Yes) dalam setiap departemen. Misalnya, dalam departemen R&D, terdapat 154 karyawan yang pergi dari total 827 karyawan.

### Job Role
* Visualisasi batang ini menunjukkan jumlah karyawan yang tetap (No) dan yang pergi (Yes) berdasarkan peran pekerjaan mereka. Contohnya, dalam posisi Sales Executive, terdapat 50 karyawan yang pergi dan 276 yang tetap.

### Demographics
* Gender: Menampilkan perbandingan jumlah karyawan yang tetap dan pergi berdasarkan gender. Contoh, 740 laki-laki tetap dan 501 perempuan tetap.
* Age: Menunjukkan jumlah karyawan yang tetap dan pergi berdasarkan kelompok usia. Misalnya, kelompok usia 30-40 tahun memiliki 338 karyawan tetap dan 81 karyawan yang pergi.
* Education: Menunjukkan jumlah karyawan yang tetap dan pergi berdasarkan tingkat pendidikan. Misalnya, tingkat pendidikan Bachelor memiliki 475 karyawan tetap dan 97 yang pergi.

### Feature Importance
* Monthly Income: Visualisasi batang yang menunjukkan pendapatan bulanan rata-rata karyawan yang tetap dan yang pergi. Karyawan yang tetap memiliki pendapatan rata-rata sekitar 6.842,85 sedangkan yang pergi memiliki pendapatan rata-rata sekitar 4.660,83.
* Total Working Years: Grafik ini menunjukkan distribusi jumlah tahun kerja total karyawan yang tetap dan yang pergi.
* Stock Option Level: Menampilkan jumlah karyawan yang tetap dan pergi berdasarkan level opsi saham mereka. Misalnya, pada level 0 terdapat 471 karyawan tetap dan 160 yang pergi.

## **Conclusion**

* **Pemahaman yang Lebih Baik tentang Faktor Attrition:** Proyek ini memberikan pemahaman yang lebih dalam tentang faktor-faktor yang mempengaruhi keputusan karyawan untuk meninggalkan perusahaan. Analisis data dan model prediksi menunjukkan bahwa pendapatan bulanan, peran pekerjaan, dan demografi karyawan adalah faktor kunci yang mempengaruhi attrition.
* **Alat untuk Mengantisipasi dan Mengurangi Attrition:** Model prediksi dan dashboard interaktif yang dikembangkan memberikan alat yang efektif bagi manajemen untuk mengantisipasi dan mengurangi attrition. Dengan memprediksi karyawan yang berisiko tinggi untuk meninggalkan perusahaan, manajemen dapat mengambil tindakan proaktif untuk meningkatkan kepuasan dan keterlibatan karyawan.
* **Wawasan untuk Pengambilan Keputusan Strategis:** Dashboard interaktif menyediakan wawasan yang mudah dipahami dan dapat diambil tindakan, yang membantu manajemen dalam membuat keputusan strategis untuk meningkatkan retensi karyawan dan mengurangi biaya yang terkait dengan pergantian karyawan.
* **Secara keseluruhan**, proyek ini memberikan kontribusi yang signifikan dalam membantu perusahaan memahami dan mengelola attrition karyawan, serta meningkatkan efektivitas strategi retensi karyawan.

## **Rekomendasi Action Items**

#### Fokus pada Departemen dengan Tingkat Attrition Tinggi
* Analisis menunjukkan bahwa departemen tertentu seperti Sales dan Research memiliki tingkat attrition yang tinggi.
* Prioritaskan tindakan retensi di departemen-departemen ini dengan langkah-langkah khusus seperti program mentoring, kenaikan gaji, dan peningkatan fasilitas kerja.

#### Mengatasi Kelompok Demografis yang Berisiko Tinggi
* Data menunjukkan bahwa kelompok usia 30-40 tahun dan karyawan dengan pendapatan bulanan yang lebih rendah memiliki risiko attrition yang lebih tinggi.
* Berikan perhatian khusus pada kelompok-kelompok ini dengan menawarkan program pengembangan karir, insentif finansial, dan fleksibilitas kerja yang lebih besar.

#### Mengatsi Kelompok Pada Feature Importance yang Berisiko Tinggi
* Tingkatkan program bonus dan insentif berdasarkan kinerja untuk memotivasi karyawan dan meningkatkan kepuasan kerja.
* Buat program penghargaan untuk karyawan yang telah bekerja selama periode waktu tertentu, seperti 5, 10, dan 15 tahun, untuk mengapresiasi loyalitas mereka.
* Adakan seminar atau workshop keuangan yang menjelaskan tentang perencanaan keuangan jangka panjang, investasi, dan manfaat memiliki saham. Sediakan layanan konsultasi keuangan pribadi bagi karyawan yang ingin lebih memahami opsi saham mereka.