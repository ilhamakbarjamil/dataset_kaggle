import pandas as pd

# Baca file CSV
file_path = 'D:\\KULIAH\\archive\\Klasifikasi_Tingkat_Kemiskinan_di_Indonesia.csv'
data = pd.read_csv(file_path, delimiter=';')

# Ganti koma menjadi titik di seluruh data
data = data.replace(',', '.', regex=True)

# Ubah kolom yang relevan menjadi tipe numerik
columns_to_numeric = [
    "Persentase Penduduk Miskin (P0) Menurut Kabupaten/Kota (Persen)",
    "Rata-rata Lama Sekolah Penduduk 15+ (Tahun)",
    "Pengeluaran per Kapita Disesuaikan (Ribu Rupiah/Orang/Tahun)",
    "Indeks Pembangunan Manusia",
    "Umur Harapan Hidup (Tahun)",
    "Persentase rumah tangga yang memiliki akses terhadap sanitasi layak",
    "Persentase rumah tangga yang memiliki akses terhadap air minum layak",
    "Tingkat Pengangguran Terbuka",
    "Tingkat Partisipasi Angkatan Kerja",
    "PDRB atas Dasar Harga Konstan menurut Pengeluaran (Rupiah)"
]

for col in columns_to_numeric:
    data[col] = pd.to_numeric(data[col], errors='coerce')

# Cek data yang kosong (missing values)
missing_values = data.isnull().sum()

# Simpan data yang sudah dirapikan
data.to_csv('data_bersih.csv', index=False)

# Tampilkan informasi dan beberapa baris pertama
print("Informasi Data:")
print(data.info())
print("\n5 Baris Pertama Data:")
print(data.head())

print("\nJumlah Nilai Kosong per Kolom:")
print(missing_values)
