total_belanja = int (input("Masukkan total belanja: "))
ongkir = int (input("Masukkan ongkir: "))
member = input("Member lu: (Y/N) ")
hari = input("Hari transaksi: (Senin sampai Minggu) ")


#_____________________
#hitung dulu diskon ongkir 
#_____________________

if total_belanja >= 400000:
    diskon_ongkir = 1.0 
elif total_belanja >= 250000:
    diskon_ongkir = 0.75 
elif total_belanja >= 150000:
    diskon_ongkir = 0.5        
else:
    diskon_ongkir = 0

ongkir_diskon = ongkir * (1 - diskon_ongkir)

#_____________________
#itung cashback nyah 
#_____________________

if total_belanja >= 300000:
    cashback = 0.10
elif total_belanja >= 200000:
    cashback = 0.07 
elif total_belanja >= 100000:        
    cashback = 0.05
else :
     cashback = 0

#tambah cashback 
if member == "Y":
    cashback  += 0.05
if hari.lower() == "sabtu": 
    cashback += 0.03

# batas maksimal cashback 
if cashback > 0.15:
    cashback = 0.15

jumlah_cashback = total_belanja * cashback

print ("ongkir yang dibayar: ", ongkir_diskon)
print ("cashback yang didapat: ", jumlah_cashback)





