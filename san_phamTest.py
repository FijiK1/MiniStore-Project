from san_pham import SanPham

ao = SanPham("Ao thun", 26000)
den = SanPham("Den ban", 40000)

print(ao)
print(den)

ao.gia = 95000

print("Sau khi sua gia ao:")
print(ao)
print(den)