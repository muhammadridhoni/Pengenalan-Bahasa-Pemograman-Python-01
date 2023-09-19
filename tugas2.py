def cek_tanda_bilangan(bilangan):
    if bilangan > 0:
        return "Bilangan positif"
    elif bilangan < 0:
        return "Bilangan negatif"
    else:
        return "Nol"

# penggunaan
angka1 = 60
angka2 = -1
angka3 = 0

print(f"{angka1} adalah {cek_tanda_bilangan(angka1)}")
print(f"{angka2} adalah {cek_tanda_bilangan(angka2)}")
print(f"{angka3} adalah {cek_tanda_bilangan(angka3)}")
