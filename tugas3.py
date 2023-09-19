class Biodata:
    def __init__(self, nama, umur, tinggi_badan, berat_badan):
        self.nama = nama
        self.umur = umur
        self.tinggi_badan = tinggi_badan
        self.berat_badan = berat_badan

    def __str__(self):
        return f"{self.nama} (Umur: {self.umur} tahun, Tinggi Badan: {self.tinggi_badan} cm, Berat Badan: {self.berat_badan} kg)"


def filter_biodata(biodata_list, kriteria, nilai_min, nilai_max):
   
    hasil_filter = []
    for biodata in biodata_list:
        if kriteria == 'tinggi' and nilai_min <= biodata.tinggi_badan <= nilai_max:
            hasil_filter.append(biodata)
        elif kriteria == 'umur' and nilai_min <= biodata.umur <= nilai_max:
            hasil_filter.append(biodata)
        elif kriteria == 'berat' and nilai_min <= biodata.berat_badan <= nilai_max:
            hasil_filter.append(biodata)
    return hasil_filter


# penggunaan
biodata1 = Biodata("aka", 30, 180, 75)
biodata2 = Biodata("iki", 25, 165, 60)
biodata3 = Biodata("aki", 35, 185, 80)
biodata4 = Biodata("ika", 28, 170, 68)

biodata_list = [biodata1, biodata2, biodata3, biodata4]

# Menampilkan menu
print("Menu:")
print("1. Filter berdasarkan tinggi badan")
print("2. Filter berdasarkan umur")
print("3. Filter berdasarkan berat badan")

# input
menu = int(input("Pilih menu (1/2/3): "))

# input nilai minimum dan maksimum
nilai_min = float(input("Masukkan nilai minimum: "))
nilai_max = float(input("Masukkan nilai maksimum: "))

# Menentukan kriteria berdasarkan menu
if menu == 1:
    kriteria = 'tinggi'
elif menu == 2:
    kriteria = 'umur'
elif menu == 3:
    kriteria = 'berat'
else:
    print("Menu tidak valid.")
    exit()

# Melakukan filtering
hasil_filter = filter_biodata(biodata_list, kriteria, nilai_min, nilai_max)

# Menampilkan hasil filtering
print("Hasil filtering berdasarkan kriteria:")
for biodata in hasil_filter:
    print(biodata)
