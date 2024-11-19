import matplotlib.pyplot as plt

# Parameter gerak benda
kecepatan = 0 # kecepatan awal dalam meter per detik
percepatan = 25 # percepatan dalam meter per detik kuadrat
waktu_total = 120 # waktu total dalam detik

# Variabel untuk menyimpan data waktu dan posisi
posisi = []
waktu = []

# Loop untuk menghitung posisi setiap detik
for t in range(waktu_total + 1):
    x = kecepatan * t + 0.5 * percepatan * t**2 # posisi benda pada waktu t
    waktu.append(t)
    posisi.append(x)

    # Plot grafik posisi terhadap waktu
    plt.plot(waktu, posisi, marker='o', color='b', linestyle='-')
    plt.title('Grafik Gerak Benda dengan Kecepatan dan Percepatan')
    plt.xlabel('Waktu (detik)')
    plt.ylabel('Posisi (meter)')
    plt.show()