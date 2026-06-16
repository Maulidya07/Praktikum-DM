mahasiswa = [
    {
        "nama": "Andi",
        "ipk": 3.1,
        "sks": 144,
        "nilai_terendah": "B",
        "status_skripsi": "Belum"
    },
    {
        "nama": "Budi",
        "ipk": 3.2,
        "sks": 145,
        "nilai_terendah": "D",
        "status_skripsi": "Selesai"
    },
    {
        "nama": "Citra",
        "ipk": 3.8,
        "sks": 140,
        "nilai_terendah": "A",
        "status_skripsi": "Selesai"
    }
]


def evaluasi_kelulusan(data):
    hasil = []

    for mhs in data:
        alasan = []

        if mhs["ipk"] < 3.0:
            alasan.append("IPK kurang dari 3.0")

        if mhs["sks"] < 144:
            alasan.append("Total SKS kurang dari 144")

        if mhs["nilai_terendah"] not in ["A", "B", "C"]:
            alasan.append("Terdapat nilai di bawah C")

        if mhs["status_skripsi"] != "Selesai":
            alasan.append("Status skripsi belum selesai")

        if len(alasan) == 0:
            status = "LULUS"
            alasan.append("Semua syarat kelulusan terpenuhi")
        else:
            status = "TIDAK LULUS"

        hasil.append({
            "nama": mhs["nama"],
            "status": status,
            "alasan": alasan
        })

    return hasil


hasil_evaluasi = evaluasi_kelulusan(mahasiswa)

for hasil in hasil_evaluasi:
    print(f"Nama   : {hasil['nama']}")
    print(f"Status : {hasil['status']}")
    print("Alasan :")
    for alasan in hasil["alasan"]:
        print(f"- {alasan}")
    print()