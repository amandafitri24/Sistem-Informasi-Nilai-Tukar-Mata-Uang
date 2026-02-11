class CurrencyManager:
    """
    Class CurrencyManager
    Mengelola dan menyimpan data nilai tukar mata uang
    """

    def __init__(self):
        # Menyimpan daftar objek mata uang
        # Menggunakan atribut private (ENCAPSULATION)
        self.__daftar_mata_uang = []

    def tambah_mata_uang(self, mata_uang):
        """
        Menambahkan objek mata uang ke dalam daftar
        """
        self.__daftar_mata_uang.append(mata_uang)  # Menyimpan objek ke list

    def tampilkan_semua(self):
        """
        Menampilkan seluruh data mata uang
        Menerapkan POLYMORPHISM
        """
        for mata_uang in self.__daftar_mata_uang:
            # Memanggil method tampilkan_info dari masing-masing objek
            print(mata_uang.tampilkan_info())