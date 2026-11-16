from mahasiswa import Mahasiswa


mhs1 = Mahasiswa("REVANKA", 19, "14012500041", "UNIVERSITAS BINA BANGSA")
mhs2 = Mahasiswa("ARRAZY", 21, "14012500040", "ILMU KOMPUTER")
mhs3 = Mahasiswa("QOIS", 25, "14012500039", "SISTEM INFORMASI")

print(mhs1.perkenalan())
print(mhs2.perkenalan())
print(mhs3.perkenalan())
print(f"NIM REVANKA: {mhs1.nim}")
print(f"Umur REVANKA: {mhs1.umur}")
print(f"NIM ARRAZY: {mhs2.nim}")
print(f"Umur ARRAZY: {mhs2.umur}")
print(f"NIM QOIS: {mhs3.nim}")
print(f"Umur QOIS: {mhs3.umur}")


print(Mahasiswa.info_kampus())
print(f"Nilai 80: {Mahasiswa.cek_lulus(80)}")
print(f"Nilai 50: {Mahasiswa.cek_lulus(50)}")