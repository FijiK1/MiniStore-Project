#Du An 6
ten = ["SSD 512GB SATA III", "GeForce RTX 5090 Super", "Logitech MX Master 3s", "Asus ROG 20th Anniversary PC Kit", "Ram Kingston Fury Beast 16GB"]
gia = [1750000,200000000,2200000,520000000,2600000]
gio = []
soluong = []
#in list sp
for i in range (len(ten)):
    print(f"Danh sach mat hang cua chung toi gom: {ten[i]}, Gia: {gia[i]}")

#dung vong lai de mua hang
ok = True
while ok:
    ask = int(input("Xin chao quy khach, hien quy khach muon mua gi?(chon 1-5): "))
    while ask <1 or ask >5:
        print(f"Mat hang khong ton tai, moi quy khach nhap lai!")
    ask2=int(input(f"Quy khach muon mua bao nhieu {ten[ask-1]}?: "))    
    gio.append(ask-1)
    soluong.append(ask2)
    print(f"Da them {ten[ask]} vao gio")
    print(f"Gio hang cua ban hien tai dang co:{ten[ask-1]}, so luong: {ask2}")     
    pick=input(f"Quy khach co muon tiep tuc mua k?(y/n): ")
    if pick == "n":
        ok = False
        print(f"chuyen sang buoc thanh toan!")
    else:
        ok = True    
       
#in hoa don, gio hang
tong = 0
print(f"Gio hang hien tai ban dang co:\n")

for i in range (len(gio)):
    print(f"{ten[ask]}, so luong: {ask2}")
    tong += gia[gio[i]] * soluong[i]
print(f"Tong thanh tien: {tong}")