
# DU AN - BAI 9, BAI CUOI

from san_pham import SanPham

def chinh():

    # Can lop SanPham da viet o Bai viet 2.
    kho = [
        SanPham("sua tuoi", 25000),
        SanPham("banh mi", 15000),
        SanPham("trung ga", 35000)
    ]

    # 1) In danh sach san pham
    print("DANH SACH SAN PHAM")
    for i in range(len(kho)):
        print(f"{i+1}. {kho[i]}")

    # 2) Vong lap mua hang, sentinel la "xong"
    gio = []
    soluong = []

    while True:
        pick = input("Chon san pham (nhap xong de dung): ")

        if pick == "xong":
            break

        tim_thay = False

        for i in range(len(kho)):
            if pick == str(i+1):
                ask = int(input("Nhap so luong: "))

                gio.append(kho[i])
                soluong.append(ask)

                print("Da them san pham vao gio hang!")
                tim_thay = True
                break

        if tim_thay == False:
            print("Lua chon khong hop le!")

    # 3) Tinh tong tien
    tong = 0

    print("\nGIO HANG")

    for i in range(len(gio)):
        tien = gio[i].tinh_gia() * soluong[i]
        tong += tien

        print(f"{gio[i].ten} - So luong: {soluong[i]} - Thanh tien: {tien:.0f} d")

    print(f"Tong cong: {tong:.0f} d")

    # 4) Ghi hoa don ra don_hang.txt
    with open("don_hang.txt", "w", encoding="utf-8") as file:

        for i in range(len(gio)):
            tien = gio[i].tinh_gia() * soluong[i]

            file.write(
                f"{gio[i].ten} - So luong: {soluong[i]} - "
                f"Thanh tien: {tien:.0f} d\n"
            )

        file.write(f"Tong cong: {tong:.0f} d\n")

    # Doc lai hoa don de kiem chung
    with open("don_hang.txt", "r", encoding="utf-8") as file:
        print("\nNOI DUNG HOA DON")
        print(file.read())
