#Du An 2
ten_cua_hang= "The Most Ordinary Store"
san_pham = ["But chi bac", "But chi kim","Gom","Hop mau sap dau"," But linemaker"]
print(san_pham)
choose = input("Xin chao quy khach, hom nay quy khach muon mua san pham nao?: ")
if  choose in san_pham:
    print(f"Cam on quy khach da mua san pham {choose} tai cua hang {ten_cua_hang} cua chung toi")
if choose not in san_pham:
    print(f"Xin loi quy khach, hien chung toi dang nhap {choose} vao kho san pham, xin quy khach vui long cho doi")
    san_pham.append(choose)
    print(f"San pham {choose} da duoc them vao kho san pham cua cua hang {ten_cua_hang} cua chung toi")
    ask = input("Quy khach co muon mua san pham nay khong? (y/n): ")
    if ask == "y":
        print(f"Cam on quy khach da mua san pham {choose} tai cua hang {ten_cua_hang} cua chung toi")
    else:
        print(f"Cam on quy khach da den voi cua hang {ten_cua_hang} cua chung toi, hen gap lai quy khach lan sau")
        