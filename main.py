from api_service import CurrencyAPI          # Mengimpor class pengambil data API
from exchange_rate import ExchangeRate       # Mengimpor class ExchangeRate
from currency_manager import CurrencyManager # Mengimpor class pengelola mata uang

def main():
    """
    Fungsi utama sistem informasi nilai tukar mata uang
    """

    api = CurrencyAPI()          # Membuat objek API
    data = api.get_data()        # Mengambil data nilai tukar dari API

    # Validasi data dari API
    if not data or "rates" not in data:
        print("Gagal mengambil data nilai tukar dari API.")
        return

    rates = data["rates"]        # Mengambil data rates dari API

    # Mengambil nilai tukar USD ke Rupiah
    rate_idr = rates["IDR"]

    manager = CurrencyManager()  # Membuat objek pengelola mata uang

    # Memproses beberapa mata uang sebagai contoh
    for kode in ["USD", "EUR", "JPY"]:
        if kode in rates:
            nilai = rates[kode]                             # Nilai tukar terhadap USD
            mata_uang = ExchangeRate(kode, nilai, rate_idr) # Membuat objek mata uang
            manager.tambah_mata_uang(mata_uang)             # Menyimpan ke manager

    # Menampilkan seluruh data nilai tukar
    manager.tampilkan_semua()

# Menjalankan program utama
if __name__ == "__main__":
    main()