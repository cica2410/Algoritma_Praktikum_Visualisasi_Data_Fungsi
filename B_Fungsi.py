import numpy as np
import matplotlib.pyplot as plt

vo = 0 # Kecepatan awal sebesar 0 m/s
a = 30 # percepatan konstan 30 m/s^2
t = 120 # Waktu dalam 2 menit dionversikan ke dalam sekon

# Definisi fungsi GLBB x(t)
def x(t):
    return vo*t + 0.5*a*t**2

# Mendefinisikan rentang data waktu (t)
t = np.arange(0, 600, 1)

# Menghitung nilai y untuk setiap nilai x
y = x(t)

# Menambahkan label, judul, dan grid
plt.plot(t, y, marker='o', color='b', linestyle='-', label="Grafik GLBB")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Grafik GLBB")
plt.legend()
plt.grid(True)
plt.show()