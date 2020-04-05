"""
w = write mode / mode menulis dan menghapus file lama, jika file tidak ada maka akan dibuat file baru
r = read mode only / hanya bisa baca
a = appending mode / menambahkan data di akhir baris
r+ = write and read mode /
"""

# Membuat File Text
file = open("data.txt", "w")
file.write("Ini adalah data Text yang dibuat dengan menggunakan python")
file.write("\nini baris baru atau baris ke dua")
file.write("\nini baris baru atau baris ke tiga")
file.write("\nini baris baru atau baris ke empatt")

file.close()

# Membaca File Text
file2 = open("data.txt", "r")
print(file2.read(10))
print(file2.readline())

# Appending Mode
file3 = open("data.txt", 'a')
file3.write("\nBaris ini dibuat dengan menggunakan mode Append")
file3.close()
