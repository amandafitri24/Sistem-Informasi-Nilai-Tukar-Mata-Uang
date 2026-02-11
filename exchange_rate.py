from currency import Currency          # Mengimpor class induk Currency

class ExchangeRate(Currency):
    """
    Class ExchangeRate
    Turunan dari Currency
    Menerapkan INHERITANCE
    """

    def __init__(self, kode, nilai, rate_idr):
        # Constructor class ExchangeRate
        # kode     : kode mata uang (USD, EUR, JPY)
        # nilai    : nilai tukar mata uang terhadap USD
        # rate_idr : nilai tukar USD ke Rupiah
        super().__init__(kode)          # Memanggil constructor class induk
        self.__nilai = nilai            # Atribut private (ENCAPSULATION)
        self.__rate_idr = rate_idr      # Atribut private (ENCAPSULATION)

    def tampilkan_info(self):
        """
        Menampilkan informasi nilai tukar mata uang
        Mengimplementasikan method abstrak (POLYMORPHISM)
        """
        # Menghitung nilai mata uang ke dalam Rupiah
        nilai_rupiah = self.__nilai * self.__rate_idr

        # Mengembalikan hasil dengan format angka penting
        return (
            f"Mata Uang: {self._kode}, "                     # Kode mata uang
            f"Nilai Tukar: {self.__nilai:.2f} "              # Nilai tukar (2 desimal)
            f"menjadi rupiah = {nilai_rupiah:,.2f}"          # Hasil konversi Rupiah
        )