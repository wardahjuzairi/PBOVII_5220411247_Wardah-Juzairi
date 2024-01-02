class kuliner:
    def __init__(self, nama, harga):
        self.nama = nama  # modifier public
        self.harga = harga  # modifier public

    def get_nama(self):
        return self.nama

    def get_harga(self):
        return self.harga

class makanan(kuliner):
    def __init__(self, nama, harga, menu=None):
        super().__init__(nama, harga)
        self._menu = menu  # modifier protected

    def get_menu(self):
        return self._menu

class dessert(makanan):
    def __init__(self, nama, harga, topping=None):
        super().__init__(nama, harga)
        self._topping = topping  # modifier protected

    def get_topping(self):
        return self._topping

    def get_nama(self): # overriding
        return f"Desert: {self.nama}"

class minuman(kuliner):
    def __init__(self, nama, harga, size):
        super().__init__(nama, harga)
        self._size = size  # modifier protected

    def get_size(self):
        return self._size

# list menu makanan dan dessert
menu_list = [
    makanan("Nasi Goreng", 15000, "Ayam"),
    makanan("Mie Goreng", 12000, "Telur"),
    dessert("Es Krim", 8000, "Coklat"),
    dessert("Pudding", 6000, "Buah"),
]

# list menu minuman
minuman_list = [
    minuman("Es Teh Manis", 5000, "Medium"),
    minuman("Jus Jeruk", 7000, "Large"),
    minuman("Kopi", 8000, "Medium"),
]

pilih = ""
total_harga = 0
total_pesanan = 0

while pilih != "3":
    print("\n===============")
    print("== MENU UTAMA ==")
    print("1. Makanan")
    print("2. Minuman")
    print("3. Keluar")
    print("===============")
    pilih = input("Pilihan Anda: ")

    if pilih == "1":
        print("\n==================")
        print("== MENU MAKANAN ==")
        for index, menu in enumerate(menu_list):
            print(f"{index + 1}. {menu.get_nama()} ({menu.get_menu()}) - Rp.{menu.get_harga()}")
        print("==================")
        pilih_menu = input("Pilihan Anda: ")
        print("\n")

        print(f"== DETAIL MAKANAN ==\nNama: {menu_list[int(pilih_menu) - 1].get_nama()}")
        if isinstance(menu_list[int(pilih_menu) - 1], makanan):
            print(f"Menu: {menu_list[int(pilih_menu) - 1].get_menu()}")
        elif isinstance(menu_list[int(pilih_menu) - 1], dessert):
            print(f"Topping: {menu_list[int(pilih_menu) - 1].get_topping()}")
        print(f"Harga: Rp.{menu_list[int(pilih_menu) - 1].get_harga()}")

        if isinstance(menu_list[int(pilih_menu) - 1], dessert):
            topping = input("Pilih Topping: ")
            menu_list[int(pilih_menu) - 1]._topping = topping  # menggunakan modifier protected

        banyak = input("Jumlah pesan? ")
        total_pesanan += int(banyak)
        print(f"\nAnda memesan {menu_list[int(pilih_menu) - 1].get_nama()} sebanyak {banyak} porsi, total harga: Rp.{menu_list[int(pilih_menu) - 1].get_harga() * int(banyak)}")
        total_harga += menu_list[int(pilih_menu) - 1].get_harga() * int(banyak)

    elif pilih == "2":
        print("\n==================")
        print("== MENU MINUMAN ==")
        for index, minum in enumerate(minuman_list):
            print(f"{index + 1}. {minum.get_nama()} ({minum.get_size()}) - Rp.{minum.get_harga()}")
        print("==================")
        pilih_minum = input("Pilihan Anda: ")
        print("\n")

        print(f"== DETAIL MINUMAN ==\nNama: {minuman_list[int(pilih_minum) - 1].get_nama()}")
        print(f"Size: {minuman_list[int(pilih_minum) - 1].get_size()}")
        print(f"Harga: Rp.{minuman_list[int(pilih_minum) - 1].get_harga()}")

        banyak = input("Jumlah pesan? ")
        total_pesanan += int(banyak)
        print(
            f"\nAnda memesan {minuman_list[int(pilih_minum) - 1].get_nama()} ({minuman_list[int(pilih_minum) - 1].get_size()}) sebanyak {banyak}, total harga: Rp.{minuman_list[int(pilih_minum) - 1].get_harga() * int(banyak)}")
        total_harga += minuman_list[int(pilih_minum) - 1].get_harga() * int(banyak)

    elif pilih == "3":
        print("Terima kasih sudah memesan di cafe starascella")
    else:
        print("Menu tidak tersedia. Silahkan coba lagi.")

print(f"Total pesanan: {total_pesanan}")
print(f"Total harga yang harus dibayar: Rp.{total_harga}")
