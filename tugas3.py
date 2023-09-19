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
        if kriteria == "tinggi" and nilai_min <= biodata.tinggi_badan <= nilai_max:
            hasil_filter.append(biodata)
        elif kriteria == "umur" and nilai_min <= biodata.umur <= nilai_max:
            hasil_filter.append(biodata)
        elif kriteria == "berat" and nilai_min <= biodata.berat_badan <= nilai_max:
            hasil_filter.append(biodata)
    return hasil_filter    

biodata1 = Biodata("aka", 30, 180, 75)
biodata2 = Biodata("iki", 25, 165, 60)
biodata3 = Biodata("aki", 35, 185, 80)
biodata4 = Biodata("ika", 28, 170, 68)
biodata5 = Biodata("ari", 15, 135, 40)
biodata6 = Biodata("ira", 10, 120, 25)
biodata7 = Biodata("adi", 70, 165, 60)
biodata8 = Biodata("ida", 32, 167, 60)
biodata9 = Biodata("baim", 21, 170, 62)
biodata10 = Biodata("ibam", 17, 165, 54)
biodata11 = Biodata("maman", 33, 187, 90)
biodata12 = Biodata("oliv", 25, 157, 53)
biodata13 = Biodata("nanda", 16, 152, 49)
biodata14 = Biodata("ikram", 28, 157, 53)
biodata15 = Biodata("arif", 16, 135, 40)
biodata16 = Biodata("ika", 13, 140, 50)
biodata17 = Biodata("adit", 20, 155, 50)
biodata18 = Biodata("kiki", 7, 120, 24)
biodata19 = Biodata("bimo", 26, 170, 65)
biodata20 = Biodata("bima", 70, 165, 54)


biodata_list = [biodata1, biodata2, biodata3, biodata4, biodata5, biodata6, biodata7, biodata8, biodata9, biodata10]

while True:

    print("Menu:")
    print("1. Filter berdasarkan tinggi badan")
    print("2. Filter berdasarkan umur")
    print("3. Filter berdasarkan berat badan")

    # Input
    menu = int(input("Pilih menu (1/2/3): "))

    # Input nilai minimum dan maksimum
    nilai_min = float(input("Masukkan nilai minimum: "))
    nilai_max = float(input("Masukkan nilai maksimum: "))

    # kriteria 
    if menu == 1:
        kriteria = "tinggi"
    elif menu == 2:
        kriteria = "umur"
    elif menu == 3:
        kriteria = "berat"
    else:
        print("Menu tidak valid.")
        continue

    hasil_filter = filter_biodata(biodata_list, kriteria, nilai_min, nilai_max)

   
    print("Hasil filtering berdasarkan kriteria:")
    for biodata in hasil_filter:
        print(biodata)

    # input kembali atau keluar
    while True:
        print("\nMenu Lanjutan:")
        print("[1] Input Kembali")
        print("[2] Keluar")
        opsi = input("Pilih opsi: ")

        if opsi == "1":
            break  # Kembali ke menu utama
        elif opsi == "2":
            exit()  # keluar
        else:
            print("Opsi tidak valid. Silakan pilih lagi.")
=======
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
        if kriteria == "tinggi" and nilai_min <= biodata.tinggi_badan <= nilai_max:
            hasil_filter.append(biodata)
        elif kriteria == "umur" and nilai_min <= biodata.umur <= nilai_max:
            hasil_filter.append(biodata)
        elif kriteria == "berat" and nilai_min <= biodata.berat_badan <= nilai_max:
            hasil_filter.append(biodata)
    return hasil_filter    

biodata1 = Biodata("aka", 30, 180, 75)
biodata2 = Biodata("iki", 25, 165, 60)
biodata3 = Biodata("aki", 35, 185, 80)
biodata4 = Biodata("ika", 28, 170, 68)
biodata5 = Biodata("ari", 15, 135, 40)
biodata6 = Biodata("ira", 10, 120, 25)
biodata7 = Biodata("adi", 70, 165, 60)
biodata8 = Biodata("ida", 32, 167, 60)
biodata9 = Biodata("baim", 21, 170, 62)
biodata10 = Biodata("ibam", 17, 165, 54)
biodata11 = Biodata("maman", 33, 187, 90)
biodata12 = Biodata("oliv", 25, 157, 53)
biodata13 = Biodata("nanda", 16, 152, 49)
biodata14 = Biodata("ikram", 28, 157, 53)
biodata15 = Biodata("arif", 16, 135, 40)
biodata16 = Biodata("ika", 13, 140, 50)
biodata17 = Biodata("adit", 20, 155, 50)
biodata18 = Biodata("kiki", 7, 120, 24)
biodata19 = Biodata("bimo", 26, 170, 65)
biodata20 = Biodata("bima", 70, 165, 54)


biodata_list = [biodata1, biodata2, biodata3, biodata4, biodata5, biodata6, biodata7, biodata8, biodata9, biodata10]

while True:

    print("Menu:")
    print("1. Filter berdasarkan tinggi badan")
    print("2. Filter berdasarkan umur")
    print("3. Filter berdasarkan berat badan")

    # Input
    menu = int(input("Pilih menu (1/2/3): "))

    # Input nilai minimum dan maksimum
    nilai_min = float(input("Masukkan nilai minimum: "))
    nilai_max = float(input("Masukkan nilai maksimum: "))

    # kriteria 
    if menu == 1:
        kriteria = "tinggi"
    elif menu == 2:
        kriteria = "umur"
    elif menu == 3:
        kriteria = "berat"
    else:
        print("Menu tidak valid.")
        continue

    hasil_filter = filter_biodata(biodata_list, kriteria, nilai_min, nilai_max)

   
    print("Hasil filtering berdasarkan kriteria:")
    for biodata in hasil_filter:
        print(biodata)

    # input kembali atau keluar
    while True:
        print("\nMenu Lanjutan:")
        print("[1] Input Kembali")
        print("[2] Keluar")
        opsi = input("Pilih opsi: ")

        if opsi == "1":
            break  # Kembali ke menu utama
        elif opsi == "2":
            exit()  # keluar
        else:
            print("Opsi tidak valid. Silakan pilih lagi.")
>>>>>>> fa230562ac1787948ee76b73e479064968f0b09d
