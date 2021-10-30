# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 11:20:56 2021

@author: User
"""

print("===== DERET FIBONACCI =====")

banyak_Bilangan = int(input("Masukkan Jumlah Bilangan : "))
bil_awal = int(input("Masukkan Bilangan Pertama : "))
bil_dua = int(input("Masukkan Bilangan Kedua : "))

for i in range(banyak_Bilangan) :
    print(bil_awal)
    Total = bil_dua + bil_awal
    bil_awal = bil_dua
    bil_dua = Total
    banyak_Bilangan -= 1

    