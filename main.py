import json
import os

saldo = 0
FILE_DATA = "data.json"

def simpan_data():
    global saldo
    data = {"saldo": saldo}
    with open(FILE_DATA, "w") as file:
        json.dump(data, file)

def muat_data():
    global saldo
    if os.path.exists(FILE_DATA):
        with open(FILE_DATA, "r") as file:
            data = json.load(file)
            saldo = data.get("saldo", 0)
        return saldo
    return 0

def tambah_pemasukan():
    global saldo
    jumlah = int(input("Masukkan jumlah pemasukan: "))
    saldo = saldo + jumlah
    simpan_data()
    print(f"Pemasukan sebesar {jumlah} berhasil ditambahkan!")

def tambah_pengeluaran():
    global saldo
    jumlah = int(input("Masukkan jumlah pengeluaran: "))
    if jumlah > saldo:
        print("Saldo tidak cukup!")
    else:
        saldo = saldo - jumlah
        simpan_data()
        print(f"Pengeluaran sebesar {jumlah} berhasil dicatat!")

def lihat_saldo():
    print("\n" + "="*40)
    print("SALDO SAAT INI".center(40))
    print("="*40)
    print(f"{'Saldo':<20} | Rp. {saldo:>10,}".replace(",", "."))
    print("="*40 + "\n")

def menu():
    print("=== Aplikasi Pengelola Uang Saku ===")
    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat saldo")
    print("4. Keluar")

saldo = muat_data()

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_pemasukan()
    elif pilihan == "2":
        tambah_pengeluaran()
    elif pilihan == "3":
        lihat_saldo()
    elif pilihan == "4":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid")