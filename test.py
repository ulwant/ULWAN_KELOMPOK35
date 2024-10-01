# kode pembuatan nama akun pengguna
nama_user = input("\nbuat nama akun anda: ")

while nama_user == "":
    nama_user = input("buat dulu nama akun anda: ")

# mengimpor modul random agar posisi tupai dapat menjadi random
import random

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
