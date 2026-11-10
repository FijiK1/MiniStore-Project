
# DU AN - BAI 9
from san_pham import SanPham


def tao_kho():
    """Tao danh sach san pham cua cua hang."""
    kho = [
        SanPham("sua tuoi", 25000),
        SanPham("banh mi", 15000),
        SanPham("trung ga", 35000)
    ]
    return kho


def hien_thi_kho(kho):
    """Hien thi danh sach san pham va gia tien."""
    print("Danh sach san pham:")

    for i in range(len(kho)):
        print(f"{i+1}. {kho[i]}")


def mua_hang(kho):
    """Cho khach chon san pham, nhap so luong va luu vao gio."""
    gio = []
    soluong = []

    while True:
        pick = input("Mua gi? (go 'xong' de dung): ")

        if pick == "xong":
            break

        tim_thay = False

        for i in range(len(kho)):
            if pick == kho[i].ten:
                gio.append(kho[i])

                ask = int(input("So luong muon mua: "))
                soluong.append(ask)

                print(f"Da them: {pick}")
                tim_thay = True
                break

        if tim_thay == False:
            print("San pham khong ton tai!")

    return gio, soluong


def tinh_tien(gio, soluong):
    """Tinh tong tien bang phuong thuc tinh_gia cua tung san pham."""
    tong = 0

    for i in range(len(gio)):
        tong += gio[i].tinh_gia() * soluong[i]

    return tong


def ghi_hoa_don(gio, soluong, tong):
    """Ghi tung san pham va tong tien vao tep don_hang.txt."""
    with open("don_hang.txt", "w", encoding="utf-8") as file:
        for i in range(len(gio)):
            tien = gio[i].tinh_gia() * soluong[i]

            file.write(
                f"{gio[i].ten}, So luong: {soluong[i]}, "
                f"Don gia: {gio[i].tinh_gia():.0f}, "
                f"Thanh tien: {tien:.0f}\n"
            )

        file.write(f"Tong cong: {tong:.0f}\n")


def doc_hoa_don():
    """Mo tep don_hang.txt va doc lai noi dung hoa don."""
    with open("don_hang.txt", "r", encoding="utf-8") as file:
        print("\nNoi dung hoa don:")
        print(file.read())


def chinh():
    """Dieu phoi toan bo chuong trinh mua hang va thanh toan."""
    kho = tao_kho()

    hien_thi_kho(kho)

    gio, soluong = mua_hang(kho)

    tong = tinh_tien(gio, soluong)

    print("\nGio hang:")
    for i in range(len(gio)):
        print(f"{gio[i].ten}, So luong: {soluong[i]}")

    print(f"Tong tien: {tong:.0f} d")

    ghi_hoa_don(gio, soluong, tong)

    doc_hoa_don()
