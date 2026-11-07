
# Kho hang
def hien_thi_kho(kho):
    """Hien thi danh sach san pham va gia tien trong kho."""
    print("Kho hien co:", list(kho.keys()))

# Them mon vao gio hang
def them_mon(kho):
    """Cho khach nhap ten mon va them vao gio hang."""
    gio = []

    while True:
        pick = input("Mua gi? (go 'xong' de dung): ")
        if pick == "xong":
            break

        gia = kho.get(pick)
        if gia != None:
            gio.append(pick)
            print(f"Da them: {pick}")
        else:
            print(f"San pham {pick} khong ton tai!")
    return gio

# Tinh tien
def tinh_tien(kho, gio):
    """Tinh tong tien cac mon hang trong gio"""
    tong = 0
    for ten in gio:
        tong += kho.get(ten)
    return tong

# Ham chinh
def chinh(kho):
    """Dieu khien chuong trinh mua hang."""
    hien_thi_kho(kho)
    gio = them_mon(kho)
    print("Gio hang:", gio)
    tong = tinh_tien(kho, gio)
    print("Tong tien:", tong)
