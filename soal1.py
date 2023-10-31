#soal1
import numpy as np

# Membuat dua matriks 3x3 menggunakan NumPy
matriks1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

matriks2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("Matriks penjumlahan dan pengurangan")
# Operasi penjumlahan matriks
hasil_penjumlahan = np.add(matriks1, matriks2)

# Operasi pengurangan matriks
hasil_pengurangan = np.subtract(matriks1, matriks2)

# Cetak hasil penjumlahan
print(hasil_penjumlahan)

# Cetak hasil pengurangan
print(hasil_pengurangan)
print()

      
#soal2
import numpy as np

matriks1 =np.array([[2, 6], [4, 7]])
matriks2 =np.array([[7, 9], [4, 8]])

print("====Perkalian====")
print(np.dot(matriks1, matriks2))
print()

#soal3
import numpy as np

matriks1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("====Transpose Matriks====")
print(np.transpose(matriks1))
print()

#soal4
# Invers matriks
print("====Invers matriks====")
matriks1 = np.array([[4, -2, 1], [5, 0, 3], [-1, 2, 6]])

print(np.linalg.inv(matriks1))
print()

#soal5
import numpy as np

matriks_identitas = np.eye(4)
print("====Matriks identitas====")
print(matriks_identitas)
print()

#soal6
import numpy as np

matriks = np.array([[1, 2, 3, 4], [5, 6, 7,8], [9, 10, 11, 12], [13, 14, 15, 16]])

matriks_reshape = np.reshape(matriks, (2, 8))

print("====Reshape Matriks====")
print(matriks_reshape)
print()