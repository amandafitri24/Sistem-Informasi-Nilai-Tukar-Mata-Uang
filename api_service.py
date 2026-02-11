import requests                     # Library untuk melakukan request HTTP ke API
from abc import ABC, abstractmethod # Digunakan untuk membuat class dan method abstrak

class APIService(ABC):
    """
    Class abstrak sebagai kerangka layanan API
    Menerapkan konsep ABSTRACTION
    """

    @abstractmethod
    def get_data(self):
        # Method abstrak yang wajib diimplementasikan oleh class turunan
        pass


class CurrencyAPI(APIService):
    """
    Class turunan untuk mengambil data nilai tukar mata uang
    Menerapkan INHERITANCE dari APIService
    """

    def __init__(self):
        # URL API publik gratis tanpa API key
        # Atribut private untuk menerapkan ENCAPSULATION
        self.__url = "https://open.er-api.com/v6/latest/USD"

    def get_data(self):
        """
        Mengambil data nilai tukar mata uang dari API
        Mengimplementasikan method abstrak (POLYMORPHISM)
        """
        response = requests.get(self.__url)  # Mengirim request ke API
        return response.json()               # Mengembalikan data dalam bentuk JSON