#test import cua hang
gio = ["banh mi"]
bang_gia = {"banh mi":15000}

#C1: Nhap full module
import cua_hang
cua_hang.tinh_tien(gio, bang_gia)

#C2: nhap full module, nhap bi danh
import cua_hang as ch
ch.tinh_tien(gio, bang_gia)

#C3: nhap thang mot ham
from cua_hang import tinh_tien
tinh_tien(gio, bang_gia)

#C4: nhap mot ham va dat bi danh
from cua_hang import tinh_tien
tinh_tien(gio, bang_gia)
