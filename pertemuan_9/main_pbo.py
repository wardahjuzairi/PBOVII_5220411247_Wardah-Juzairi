class Animal:
    def __init__(self, nama, sifat, ukuran, jumlah_kaki):
        self.nama = nama
        self.sifat = sifat
        self._ukuran = ukuran #modifier protected
        self.jumlah_kaki = jumlah_kaki

    def get_info(self):
        return f"Nama:{self.nama}, Sifat: {self.sifat}, Ukuran: {self._ukuran}, Kaki: {self.jumlah_kaki}"


class Mamalia(Animal):
    def __init__(self, nama, sifat, ukuran, jumlah_kaki, bisa_jalan, jenis_mamalia):
        super().__init__(nama, sifat, ukuran, jumlah_kaki)
        self._bisa_jalan = bisa_jalan #modifier protected
        self.jenis_mamalia = jenis_mamalia

    # Overriding
    def get_info(self):  
        return f"{super().get_info()}, Bisa Jalan: {self._bisa_jalan}, Jenis Mamalia: {self.jenis_mamalia}"


class Aves(Animal):
    def __init__(self, nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves):
        super().__init__(nama, sifat, ukuran, jumlah_kaki)
        self.bisa_terbang = bisa_terbang
        self._jenis_aves = jenis_aves #modifier protected
    
    # Overriding
    def get_info(self):  
        return f"{super().get_info()}, Bisa Terbang: {self.bisa_terbang}, Jenis Aves: {self._jenis_aves}"


class Ayam(Aves):
    def __init__(self, nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves, jenis_ayam, bisa_diadu):
        super().__init__(nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves)
        self.jenis_ayam = jenis_ayam
        self._bisa_diadu = bisa_diadu #modifier protected

    # Overriding
    def get_info(self): 
        return f"{super().get_info()}, Jenis Ayam: {self.jenis_ayam}, Bisa Diadu: {self._bisa_diadu}"


class BurungMerpati(Aves):
    def __init__(self, nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves, jenis_burung_merpati):
        super().__init__(nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves)
        self.jenis_burung_merpati = jenis_burung_merpati

    # Overriding
    def get_info(self):  
        return f"{super().get_info()}, Jenis Burung Merpati: {self.jenis_burung_merpati}"

#inisialisasi objek    
hewan1 = Animal("Harimau", "Buas", "42 cm", 2) 
hewan2 = Mamalia("Sheep","Penurut", "90 cm", 4, True, "Kambing")
hewan3 = Aves("Woody", "Agrasif", "30 cm", 2, True, "Burung")
hewan4 = Ayam("Jago", "Garang", "50 cm", 2, "tidak bisa terbang dengan baik", "Ayam", "Ayam bangkok",True)
hewan5 = BurungMerpati("Pigeon", "Kalem", "35 cm", 2, True, "Burung", "Merpati Putih")

info_hewan1 = hewan1.get_info()
info_hewan2 = hewan2.get_info()
info_hewan3 = hewan3.get_info()
info_hewan4 = hewan4.get_info()
info_hewan5 = hewan5.get_info()

print()
print('\t\t\t\t1. KATEGORI ANIMAL')
print(114*'=')
print(f"{info_hewan1}")

print()
print('\t\t\t\t2. KATEGORI MAMALIA')
print(114*'=')
print(f"{info_hewan2}, Bisa Jalan: {hewan2._bisa_jalan}, Jenis Mamalia: {hewan2.jenis_mamalia}")

print()
print('\t\t\t\t3. KATEGORI AVES')
print(114*'=')
print(f"{info_hewan3}, Bisa Terbang: {hewan3.bisa_terbang}, Jenis Aves: {hewan3._jenis_aves}") 

print()
print('\t\t\t\t4. KATEGORI AYAM')
print(114*'=')
print(f"{info_hewan4}, Bisa Terbang: {hewan4.bisa_terbang}, Jenis Aves: {hewan4._jenis_aves}, Jenis Ayam: {hewan4.jenis_ayam}, Bisa Diadu: {hewan4._bisa_diadu}")

print()
print('\t\t\t\t5. KATEGORI BURUNG MERPATI')
print(114*'=')
print(f"{info_hewan5}, Bisa Terbang: {hewan5.bisa_terbang}, Jenis Aves: {hewan5._jenis_aves}, Jenis Burung Merpati: {hewan5.jenis_burung_merpati}")