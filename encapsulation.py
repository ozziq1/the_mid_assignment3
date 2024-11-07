class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.__nama = nama  # private variable
        self.__nim = nim    # private variable
        self.__jurusan = jurusan  # private variable

    # Getter untuk nama
    def get_nama(self):
        return self.__nama

    # Setter untuk nama
    def set_nama(self, nama):
        self.__nama = nama

    # Getter untuk NIM
    def get_nim(self):
        return self.__nim

    # Setter untuk NIM
    def set_nim(self, nim):
        self.__nim = nim

    # Getter untuk jurusan
    def get_jurusan(self):
        return self.__jurusan

    # Setter untuk jurusan
    def set_jurusan(self, jurusan):
        self.__jurusan = jurusan

    # Method untuk menampilkan informasi mahasiswa
    def info(self):
        return f"Nama: {self.__nama}, NIM: {self.__nim}, Jurusan: {self.__jurusan}"


# Membuat objek dari kelas Mahasiswa
mahasiswa1 = Mahasiswa("Andi", "123456", "Teknik Informatika")

# Menampilkan informasi mahasiswa
print(mahasiswa1.info())

# Menggunakan setter untuk mengubah data
mahasiswa1.set_nama("Budi")
mahasiswa1.set_nim("654321")
mahasiswa1.set_jurusan("Sistem Informasi")

# Menampilkan informasi mahasiswa setelah perubahan
print(mahasiswa1.info())

# Menggunakan getter untuk mengakses data
print(f"Nama Mahasiswa: {mahasiswa1.get_nama()}")
print(f"NIM Mahasiswa: {mahasiswa1.get_nim()}")
print(f"Jurusan Mahasiswa: {mahasiswa1.get_jurusan()}")