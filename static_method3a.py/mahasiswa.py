from abc import ABC, abstractmethod

# 1. ABSTRACTION + ENCAPSULATION
# ABC = class yang tidak bisa dibuat objek langsung, harus diturunkan
class Person(ABC):
    def __init__(self, nama, umur):
        self.nama = nama
        self._umur = umur  # _ = protected, masih bisa diakses anaknya
        self.__nim = None  # __ = private, tidak bisa diakses dari luar

    # 2. ABSTRACT METHOD - wajib ada di anaknya
    @abstractmethod
    def perkenalan(self):
        pass

    # 3. PROPERTY - cara aman akses private
    @property
    def umur(self):
        return self._umur

    @umur.setter
    def umur(self, nilai_baru):
        if nilai_baru > 0:
            self._umur = nilai_baru

# 4. INHERITANCE - Mahasiswa mewarisi Person
class Mahasiswa(Person):
    jumlah_mahasiswa = 0  # Class Attribute

    def __init__(self, nama, umur, nim, jurusan):
        super().__init__(nama, umur) # panggil __init__ parent
        self.__nim = nim
        self.jurusan = jurusan
        Mahasiswa.jumlah_mahasiswa += 1

    # 5. POLYMORPHISM - method yang sama, isi beda dari parent
    def perkenalan(self):
        return f"Halo, saya {self.nama} dari {self.jurusan}"

    # 6. PROPERTY untuk NIM
    @property
    def nim(self):
        return self.__nim

    # 7. CLASS METHOD - bisa dipanggil tanpa buat objek
    @classmethod
    def info_kampus(cls):
        return f"Total mahasiswa: {cls.jumlah_mahasiswa}"

    # 8. STATIC METHOD - fungsi biasa tapi nempel di class
    @staticmethod
    def cek_lulus(nilai):
        return "Lulus" if nilai >= 60 else "Tidak Lulus"

# 9. INHERITANCE LAGI + POLYMORPHISM
class Dosen(Person):
    def perkenalan(self):
        return f"Halo, saya Dosen {self.nama}"