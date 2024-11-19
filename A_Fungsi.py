import numpy as np
import matplotlib.pyplot as plt

v = 20 # Kecepatan konstan sebesar 20 m/s
t = 300 # Waktu dalam 5 menit dionversikan menjadi 300 detik

# Definisi fungsi GLB x(t)
def x(t):
    return v*t

# Mendefinisikan rentang data waktu (t)
t = np.arange(0, 600, 1)

# Menghitung nilai y untuk setiap nilai x
y = x(t)

# Menambahkan labe, judul, dan grid
plt.plot(t, y, marker='o', color='b', linestyle='-', label="Grafik GLB")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Grafik GLB")
plt.legend()
plt.grid(True)
plt.show()