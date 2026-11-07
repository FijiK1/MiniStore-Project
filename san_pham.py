class SanPham:
    """Lop mo ta mot san pham trong cua hang."""

    def __init__(self, ten, gia, giam_gia=0):
        self.ten = ten
        self.gia = gia
        self.giam_gia = giam_gia

    def tinh_gia(self):
        """Tinh gia san pham sau khi giam gia."""
        return self.gia * (1 - self.giam_gia)

    def __str__(self):
        """Tra ve thong tin san pham dang chuoi."""
        return f"{self.ten}: {self.tinh_gia():.0f} d"