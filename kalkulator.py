# kelompok 5
# Harlan Romdon_250511096
# Khoiril Muhammad Nasir_250511072
# kevin Ade Ramdhani_250511099
# Irgi Syaeful Alfarizhi_250511135

def kalkulator():
    print("=== KALKULATOR SEDERHANA ===")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    
    pilihan = input("Pilih menu (1/2/3/4): ")
    
    # Input angka
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    
    # Algoritma Percabangan
    if pilihan == '1':
        hasil = angka1 + angka2
        print(f"Hasil: {angka1} + {angka2} = {hasil}")
    elif pilihan == '2':
        hasil = angka1 - angka2
        print(f"Hasil: {angka1} - {angka2} = {hasil}")
    elif pilihan == '3':
        hasil = angka1 * angka2
        print(f"Hasil: {angka1} * {angka2} = {hasil}")
    elif pilihan == '4':
        if angka2 == 0:
            print("Error: Tidak bisa membagi dengan nol!")
        else:
            hasil = angka1 / angka2
            print(f"Hasil: {angka1} / {angka2} = {hasil}")
    else:
        print("Menu tidak tersedia.")

# Jalankan program
kalkulator()
