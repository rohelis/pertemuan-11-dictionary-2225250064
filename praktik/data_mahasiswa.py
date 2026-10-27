def cari_mahasiswa(data, nim):
    return data.get(nim, "Data tidak ditemukan")

def rata_rata_nilai(data):
    if not data:
        return 0
    total = sum(mhs["nilai"] for mhs in data.values())
    return total / len(data)

data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}

print("Pencarian A003:", cari_mahasiswa(data_mahasiswa, "A003"))
print("Pencarian A999:", cari_mahasiswa(data_mahasiswa, "A999"))

data_mahasiswa["A006"] = {"nama": "Fani", "kelas": "B", "nilai": 90}
data_mahasiswa["A002"]["nilai"] = 82

print("\nRekap Data Mahasiswa:")
for nim, info in data_mahasiswa.items():
    print(f"{nim} -> Nama: {info['nama']}, Kelas: {info['kelas']}, Nilai: {info['nilai']}")

print(f"\nRata-rata Nilai: {rata_rata_nilai(data_mahasiswa)}")