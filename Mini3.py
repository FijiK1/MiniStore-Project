#Du An 3
san_pham = ["But chi bac", "But chi kim","Gom","Hop mau sap dau"," But linemaker"]
print(f"Ban dau: {san_pham}")

#thay san pham - index
san_pham[2] = "Ge Force RTX 9090 Ti Super"
print(f"Ke hang sau khi thay san pham lan 1: {san_pham}")

#thay san pham - pop
san_pham.pop(0)
print(f"Ke hang sau khi thay san pham lan 2: {san_pham}")

#thay san pham - inset
san_pham.insert(4, "Blue Switch keyboard")
print(f"Ke hang sau khi thay san pham lan 3 : {san_pham}")

#them mat hang khuyen mai o dau
san_pham.insert(0, "Intel Graphics Series")
print(f"San pham khuyen mai cua cua hang hien tai: {san_pham[0]}")
print(f"List san pham hien co: {san_pham}")

#xoa 2 item cuoi bang lenh del
del san_pham[-1:-3:-1]
print(f"List san pham hien co sau khi xoa 2 item cuoi bang lenh del: {san_pham}")