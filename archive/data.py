import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
import seaborn as sns

# Membuka dialog file
Tk().withdraw()  # Menyembunyikan jendela utama tkinter
file_path = askopenfilename(title="Pilih file")

# Membaca file
data = pd.read_csv(file_path, delimiter=";")

# Periksa nama kolom
print(data.columns)

# Konversi kolom ke angka (jika diperlukan)
data["Persentase Penduduk Miskin (P0) Menurut Kabupaten/Kota (Persen)"] = pd.to_numeric(
    data["Persentase Penduduk Miskin (P0) Menurut Kabupaten/Kota (Persen)"], errors="coerce"
)
data["Pengeluaran per Kapita Disesuaikan (Ribu Rupiah/Orang/Tahun)"] = pd.to_numeric(
    data["Pengeluaran per Kapita Disesuaikan (Ribu Rupiah/Orang/Tahun)"], errors="coerce"
)
data["Indeks Pembangunan Manusia"] = pd.to_numeric(
    data["Indeks Pembangunan Manusia"], errors="coerce"
)

# 1. Histogram untuk distribusi Persentase Penduduk Miskin
plt.figure(figsize=(8, 5))
data["Persentase Penduduk Miskin (P0) Menurut Kabupaten/Kota (Persen)"].plot.hist(
    bins=20, color="skyblue", edgecolor="black"
)
plt.title("Distribusi Persentase Penduduk Miskin")
plt.xlabel("Persentase Penduduk Miskin")
plt.ylabel("Frekuensi")
plt.show()

# 2. Scatter plot untuk Pengeluaran per Kapita vs Indeks Pembangunan Manusia
plt.figure(figsize=(8, 5))
sns.scatterplot(
    x="Pengeluaran per Kapita Disesuaikan (Ribu Rupiah/Orang/Tahun)",
    y="Indeks Pembangunan Manusia",
    data=data,
    color="orange"
)
plt.title("Hubungan Pengeluaran per Kapita vs Indeks Pembangunan Manusia")
plt.xlabel("Pengeluaran per Kapita (Ribu Rupiah/Orang/Tahun)")
plt.ylabel("Indeks Pembangunan Manusia")
plt.show()

# 3. Boxplot untuk memahami persebaran Pengeluaran per Kapita
plt.figure(figsize=(8, 5))
sns.boxplot(data=data["Pengeluaran per Kapita Disesuaikan (Ribu Rupiah/Orang/Tahun)"])
plt.title("Boxplot Pengeluaran per Kapita")
plt.show()

# Lihat 5 baris pertama
print(data.head(10))
