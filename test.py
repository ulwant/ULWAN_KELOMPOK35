# kode pembuatan nama akun pengguna
nama_user = input("\nbuat nama akun anda: ")

while nama_user == "":
    nama_user = input("buat dulu nama akun anda: ")

# mengimpor modul random agar posisi tupai dapat menjadi random
import random

# method untuk membuat kata sambutan kepada pengguna
class method:
    def __init__(self, nama, departemen):
        self.nama = nama
        self.departemen = departemen
    
    def intro(self):
        style = "=" * (len(self.nama) + len(self.departemen) + 32)
        print(style)
        print("GAMES MENEBAK POSISI TUPAI".center(len(style)))
        print(f"Selamat datang {self.nama} dari departemen {self.departemen}")
        print(style)

obj = method(input("Masukkan nama anda :"), input("Masukkan Departemen anda :"))

obj.intro()

# kode inti permainan menebak posisi tupai
while True:
    # kode pendefinisian dan pembukaan permainan
    bentuk_goa = "|_|"
    goa_kosong = [bentuk_goa] * 4
    
    tupai_position = random.randint(1, 4)

    goa = goa_kosong.copy()
    goa[tupai_position - 1] = "|0_0|"

    goa_kosong = ' '.join(goa_kosong)
    goa = ' '.join(goa)
    print("")
    print("=" * (len(nama_user) + 38))
    print(f"Halo {nama_user}! Coba perhatikan goa dibawah ini\n{goa_kosong}\n")

# kode yang menyatakan apakah pengguna menang atau kalah
    pilihan_user = int(input("Menurut kamu di goa nomor berapa si tupai berada? [1 / 2 / 3 / 4]: "))
   
    if pilihan_user == tupai_position:
            print(f"\n{goa}\n\nSelamat Kamu Menang 🏆")
    else:
            print(f"\n{goa}\n\nUncchhh kamu kalah 🙊")

    # kode untuk mengulagi permainan
    play_again = input("\napakah ingin melanjutkan gamenya lagi? [y/n]")
    if play_again == "n":
        break

# function untuk membuat respon pengguna terhadap permainan
def respon_user():
    respon = int(input("\nApakah anda suka dengan program ini? [1-10] : "))

    if respon < 7 :
        return print("\nTerimakasih telah menilai, Kami akan selalu meningkatkan kinerja game ini")
    else:
        return print("\nTerimakasih telah menilai, Kami akan selalu menjaga kinerja game ini")
    
respon_user()

# menginformasikan kepada user bahwa program telah selesai
print("\nPROGRAM SELESAI\nTerimakasih telah memainkan game kami\n")
