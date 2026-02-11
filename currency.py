from abc import ABC, abstractmethod   # Digunakan untuk membuat class dan method abstrak

class Currency(ABC):
    """
    Class abstrak sebagai blueprint data mata uang
    Menerapkan konsep ABSTRACTION
    """

    def __init__(self, kode):
        # Menyimpan kode mata uang (contoh: USD, EUR)
        # Atribut protected agar dapat diakses oleh class turunan
        self._kode = kode

    @abstractmethod
    def tampilkan_info(self):
        """
        Method abstrak untuk menampilkan informasi mata uang
        Wajib diimplementasikan oleh class turunan
        """
        pass