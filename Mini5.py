#Du An 5
ten = ["sua tuoi","banh mi","trung","ca phe","duong"]
gia = [25000, 15000, 35000, 60000, 20000]
print (ten)
print (gia)

#tong don gia moi mat hang
tong = 0
for i in range (len(ten)):
    tong += gia[i]
print(f"Tong don gia don vi cac mat hang: {tong}")   

#tim sp dat va re nhat
Max= gia[0]
Min= gia[0]
vtmax= 0
vtmin = 0
for i in range (len(ten)):
    if gia[i] > Max:
        Max = gia[i]
        vtmax=i
print(f"San pham co tri gia lon nhat la: {ten[vtmax]}, gia: {Max}")

for i in range (len(ten)):
    if gia[i] < Min:
        Min = gia[i]
        vtmin = i
print(f"San pham co tri gia nho nhat la: {ten[vtmin]}, gia: {Min}")

#Giam gia 10%, in tien
sale = float(input("Moi quy khach nhap voucher de giam gia(Nhap tu 0.1 - 0.99.Không nhận 0%, 100%): "))
while sale <= 0.0 or sale >=1.0:
        print(f"Voucher khong hop le, moi nhap lai")
        sale = float(input("Moi quy khach nhap voucher de giam gia(Không nhận 0%, 100%): "))
tong = tong*(1-sale)
print (f"So tien phai tra sau khi ap voucher giam {str(sale)} la: {float(tong)} VND")