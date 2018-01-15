import os
import csv

def menupertama():
    print("")
    print("""     PROGRAM PEMBAYARAN UANG KULIAH TUNGGAL
DI FAKULTAS MATEMATIKA DAN ILMU PENGETAHUAN ALAM
           UNIVERSITAS TANJUNGPURA
          PONTIANAK KALIMANTAN BARAT""")
    print("")

    print("""Apa yang akan anda pilih ?
           1. Bayar
           2. Keluar""")
    pilihan = int(input("Masukkan Pilihan Anda [1/2] : "))  
    if (pilihan == 1):
        nama = input("Masukkan Nama Mahasiswa : ").upper()
        nim = input("Masukkan NIM Mahasiswa  : ").upper()
    else:
	    exit() 
    print ("""Pilih Program Studi 
					   1. Matematika
					   2. Statistika
					   3. Fisika
					   4. Geofisika
					   5. Sistem Informasi
					   6. Ilmu Kelautan
					   7. Biologi
					   8. Sistem Komputer
					   9. Kimia""")
					   
    prodi = int(input("Masukkan Program Studi Mahasiswa : "))
    print ("""Pilihan UKT : 
					   1. UKT 1
					   2. UKT 2
					   3. UKT 3
					   4. UKT 4
					   5. UKT 5""")
    if (prodi == 1):
        kategori = "Matematika"
        biaya = [500000,1000000,2050000,2550000,2750000];
        ukt = int(input("Anda UKT Berapa : "))    
        if (ukt == 1):
            biaya2 = biaya[0]
        elif (ukt == 2):
            biaya2 = biaya[1]
        elif (ukt == 3):
            biaya2 = biaya[2]
        elif (ukt == 4):
            biaya2 = biaya[3]
        elif (ukt == 5):
            biaya2 = biaya[4]	
        print("")
    elif (prodi == 2):
        kategori = "Statistika"
        biaya = [500000,1000000,2250000,2850000,3050000];
        ukt = int(input("Anda UKT Berapa : "))    
        if (ukt == 1):
            biaya2 = biaya[0]
        elif (ukt == 2):
            biaya2 = biaya[1]
        elif (ukt == 3):
            biaya2 = biaya[2]
        elif (ukt == 4):
            biaya2 = biaya[3]
        elif (ukt == 5):
            biaya2 = biaya[4]
    elif (prodi == 3):
        kategori = "Fisika"
        biaya = [500000,1000000,2050000,2550000,2750000]
        ukt = int(input("Anda UKT Berapa : "))    
        if (ukt == 1):
            biaya2 = biaya[0]
        elif (ukt == 2):
            biaya2 = biaya[1]
        elif (ukt == 3):
            biaya2 = biaya[2]
        elif (ukt == 4):
            biaya2 = biaya[3]
        elif (ukt == 5):
            biaya2 = biaya[4]
    elif (prodi == 4):
        kategori = "Geofisika"
        biaya = [500000,1000000,2250000,2850000,3050000]
        ukt = int(input("Anda UKT Berapa : "))    
        if (ukt == 1):
            biaya2 = biaya[0]
        elif (ukt == 2):
            biaya2 = biaya[1]
        elif (ukt == 3):
            biaya2 = biaya[2]
        elif (ukt == 4):
            biaya2 = biaya[3]
        elif (ukt == 5):
            biaya2 = biaya[4]
    elif (prodi == 5):
        kategori = "Sistem Informasi"
        biaya = (500000,1000000,4350000,4550000,4850000)
        ukt = int(input("Anda UKT Berapa : "))    
        if (ukt == 1):
            biaya2 = biaya[0]
        elif (ukt == 2):
            biaya2 = biaya[1]
        elif (ukt == 3):
            biaya2 = biaya[2]
        elif (ukt == 4):
            biaya2 = biaya[3]
        elif (ukt == 5):
            biaya2 = biaya[4]
    elif (prodi == 6):
        kategori = "Ilmu Kelautan"
        biaya = (500000,1000000,2850000,3550000,3850000)
        ukt = int(input("Anda UKT Berapa : "))    
        if (ukt == 1):
            biaya2 = biaya[0]
        elif (ukt == 2):
            biaya2 = biaya[1]
        elif (ukt == 3):
            biaya2 = biaya[2]
        elif (ukt == 4):
            biaya2 = biaya[3]
        elif (ukt == 5):
            biaya2 = biaya[4]
    elif (prodi == 7):
        kategori = "Biologi"
        biaya = (500000,1000000,2250000,2850000,3050000)
        ukt = int(input("Anda UKT Berapa : "))    
        if (ukt == 1):
            biaya2 = biaya[0]
        elif (ukt == 2):
            biaya2 = biaya[1]
        elif (ukt == 3):
            biaya2 = biaya[2]
        elif (ukt == 4):
            biaya2 = biaya[3]
        elif (ukt == 5):
            biaya2 = biaya[4]
    elif (prodi == 8):
        kategori = "Sistem Komputer"
        biaya = (500000,1000000,4350000,4550000,4850000)
        ukt = int(input("Anda UKT Berapa : "))    
        if (ukt == 1):
            biaya2 = biaya[0]
        elif (ukt == 2):
            biaya2 = biaya[1]
        elif (ukt == 3):
            biaya2 = biaya[2]
        elif (ukt == 4):
            biaya2 = biaya[3]
        elif (ukt == 5):
            biaya2 = biaya[4]
    elif (prodi == 9):
        kategori = "Kimia"
        biaya = (500000,1000000,1550000,1650000,1750000)
        ukt = int(input("Anda UKT Berapa : "))    
        if (ukt == 1):
            biaya2 = biaya[0]
        elif (ukt == 2):
            biaya2 = biaya[1]
        elif (ukt == 3):
            biaya2 = biaya[2]
        elif (ukt == 4):
            biaya2 = biaya[3]
        elif (ukt == 5):
            biaya2 = biaya[4]
    #membuka dan menambahkan record
    with open('finalproject.csv', 'a', newline='') as csvfile:
        myFields = ['nama', 'nim', 'kategori', 'ukt', 'biaya2']
        writer = csv.DictWriter(csvfile, fieldnames=myFields, delimiter=';')
        writer.writerow({'nama' : (nama), 'nim': (nim), 'kategori': (kategori), 'ukt': (ukt), 'biaya2': (biaya2)})    
    print("_____________________________________________")
    print("HASIL PEMBAYARAN UKT FMIPA UNIVERSITAS TANJUNGPURA")
    print("Nama Mahasiswa         : "+str(nama))
    print("Nim Mahasiswa          : "+str(nim))
    print("Program Studi          : "+str(kategori))
    print("UKT                    : "+str(ukt))
    print("_____________________________________________")
    print("Biaya UKT yang dibayar : ","Rp. "+str(biaya2))
    print("_____________________________________________")
    print("TERIMA KASIH ATAS PEMBAYARAN UKT FMIPA UNIVERSITAS TANJUNGPURA")    
    print("_____________________________________________")
    if(input("Mau Lanjut ? [Y/N]: ") == "N" or "n"):
        exit()
    else:
        os.system('cls')	    
       
loop = True

while loop:    

    menupertama()
