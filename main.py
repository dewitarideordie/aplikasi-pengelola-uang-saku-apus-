import json
import os

saldo = 0
riwayat = []
FILE_DATA = "data.json"

def simpan_data():
    global saldo, riwayat
    data = {"saldo": saldo, "riwayat": riwayat}
    with open(FILE_DATA, "w") as file:
        json.dump(data, file)

def muat_data():
    global saldo, riwayat
    if os.path.exists(FILE_DATA):
        with open(FILE_DATA, "r") as file:
            data = json.load(file)
            saldo = data.get("saldo", 0)
            riwayat = data.get("riwayat", [])
        return saldo, riwayat
    return 0, []

def tambah_pemasukan():
    global saldo, riwayat
    jumlah = int(input("Masukkan jumlah pemasukan: "))
    saldo = saldo + jumlah
    riwayat.append({"tipe": "Pemasukan", "jumlah": jumlah})
    simpan_data()
    print(f"Pemasukan sebesar {jumlah} berhasil ditambahkan!")

def tambah_pengeluaran():
    global saldo, riwayat
    jumlah = int(input("Masukkan jumlah pengeluaran: "))
    if jumlah > saldo:
        print("Saldo tidak cukup!")
    else:
        saldo = saldo - jumlah
        riwayat.append({"tipe": "Pengeluaran", "jumlah": jumlah})
        simpan_data()
        print(f"Pengeluaran sebesar {jumlah} berhasil dicatat!")

def lihat_saldo():
    print("\n" + "="*40)
    print("SALDO SAAT INI".center(40))
    print("="*40)
    print(f"{'Saldo':<20} | Rp. {saldo:>10,}".replace(",", "."))
    print("="*40 + "\n")

def lihat_tabel_lengkap():
    print("\n" + "="*66)
    print("TABEL LENGKAP TRANSAKSI".center(66))
    print("="*66)
    print(f"{'No':<5} | {'Tipe':<18} | {'Jumlah':>15} | {'Saldo Sisa':>15}")
    print("-"*66)

    if not riwayat:
        print("Tidak ada transaksi.".center(66))
        print("-"*66)
        print(f"{'':<5} | {'':<18} | {'SALDO SISA':<15} | Rp. {saldo:>10,}".replace(",", "."))
        print("="*66 + "\n")
        return

    total_saldo = 0
    for i, transaksi in enumerate(riwayat, 1):
        tipe = transaksi["tipe"]
        jumlah = transaksi["jumlah"]
        if tipe == "Pemasukan":
            total_saldo += jumlah
        else:
            total_saldo -= jumlah

        print(f"{i:<5} | {tipe:<18} | Rp. {jumlah:>12,} | Rp. {total_saldo:>12,}".replace(",", "."))

    print("-"*66)
    # Pastikan total saldo akhir sama dengan saldo sisa (running total)
    print(f"{'':<5} | {'TOTAL':<18} | {'':>15} | Rp. {total_saldo:>12,}".replace(",", "."))
    print("="*66 + "\n")

def menu():
    print("=== Aplikasi Pengelola Uang Saku ===")
    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat saldo")
    print("4. Lihat tabel lengkap")
    print("5. Keluar")

saldo, riwayat = muat_data()

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
        lihat_tabel_lengkap()
    elif pilihan == "5":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid")