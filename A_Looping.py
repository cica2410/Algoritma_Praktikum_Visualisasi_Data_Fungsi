import matplotlib.pyplot as plt

# Parameter gerak benda
kecepatan = 20 # kecepata konstan dalam meter per detik
waktu_total = 300 # waktu total dalam detik

# Variabel untuk menyimpan data waktu dan posisi
posisi = []
waktu = []

# Loop untuk menghitung posisi setiap detik
for t in range(waktu_total + 1):
    x = kecepatan * t # posisi benda pada waktu t
    posisi.append(x)
    waktu.append(t)

# Plot grafik posisi terhadap waktu
plt.plot(waktu, posisi, marker='o', color='b', linestyle='-')
plt.title('Grafik Gerak Benda dengan Kecepatan Konstan')
plt.xlabel('waktu (detik)')
plt.ylabel('posisi (meter)')
plt.show()