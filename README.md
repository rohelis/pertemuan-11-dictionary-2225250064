# Pertemuan 11 - Dictionary/Map
Nama: Rohelis
NIM: 2225250064
Kelas: 3B

## Tujuan
Memodelkan data pendidikan menggunakan dictionary dan pasangan key-value.

## Struktur Data
Key utama menggunakan NIM mahasiswa (tipe data string, contoh: `"A001"`). Setiap value berupa dictionary yang menyimpan atribut `nama` (string), `kelas` (string), dan `nilai` (integer).

## Cara Menjalankan
python3 praktik/data_mahasiswa.py

## Test Case
| Input/Aksi | Hasil yang Diharapkan | Hasil Aktual | Status |
| :--- | :--- | :--- | :--- |
| Pencarian A003 | Data Citra ditampilkan | Data Citra ditampilkan | Lulus |
| Pencarian A999 | Pesan 'Data tidak ditemukan' | Pesan 'Data tidak ditemukan' | Lulus |
| Pembaruan nilai A002 menjadi 82 | Nilai A002 berubah menjadi 82 | Nilai A002 berubah menjadi 82 | Lulus |
| Penambahan data A006 | Key A006 tersedia setelah ditambahkan | Key A006 tersedia | Lulus |
| Rekap items() | Semua NIM dan data tampil | Semua NIM dan data tampil | Lulus |

## Refleksi
Kesalahan akses key yang sering terjadi adalah menggunakan akses langsung (`data[nim]`) pada key yang tidak tersedia, sehingga memicu error `KeyError`. Hal ini diatasi dengan menggunakan metode `get()` agar program lebih aman dan menampilkan pesan penanganan yang jelas.