#Du An 7
kho = {"sua tuoi": 25000,"banh mi": 15000,"trung ga": 35000,"ca phe":60000,"duong": 20000}

#tra gia theo ten mon
thanhtoan ={}
print(kho)
pick = input("Moi quy khach goi mon: ")
gia=kho.get(pick)

if gia != None:
    print(f"Quy khach da chon: {pick} voi gia: {gia}")
else:
    print(f"Xin loi quy khach, hien da het{pick}, mong quy khach thong cam!")

#in sp theo gia tang dan
print(sorted(kho, key=kho.get)) 

#tong don gia moi hang
tong = 0
for ten,gia in kho.items():
        tong += gia
print(f"Tong hoa don moi mat hang: {tong}")    