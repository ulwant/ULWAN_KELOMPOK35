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
