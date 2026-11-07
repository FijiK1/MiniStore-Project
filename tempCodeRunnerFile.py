kho = ["sua tuoi", "banh mi", "trung", "ca phe", "duong"," xoai","com","bobo"]

#chuan hoa ten, ghi de
for i in range(len(kho)):
    print(f"Format san pham truoc khi thay doi: {kho[i]}")

    kho[i] = kho[i].title()
    print(f"Format san pham sau khi thay doi: {kho[i]}")
print(f"List san pham hien tai: {kho}")    

#tao list co san pham dai hon 5 ky tu
lista = []
for i in kho:
    if len(i) > 5:
        lista.append(i)
    print(f"List san pham co dai hon 5 ky tu: {lista}")