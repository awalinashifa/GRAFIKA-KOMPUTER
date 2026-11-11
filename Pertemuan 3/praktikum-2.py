
import matplotlib.pyplot as plt

# Koordinat setiap poligon
segitiga = [(1, 1), (4, 1), (2.5, 3.5), (1, 1)]
persegi = [(6, 1), (8, 1), (8, 3), (6, 3), (6, 1)]
segi_lima = [(1, 5), (2, 7), (4, 7), (5, 5), (3, 4), (1, 5)]

def gambar_poligon(titik, warna, nama, posisi_label):
    x = [p[0] for p in titik]
    y = [p[1] for p in titik]

    plt.fill(x, y, color=warna, alpha=0.3)
    plt.plot(x, y, color=warna, linewidth=2, marker='o')
    plt.text(
        posisi_label[0], posisi_label[1],
        nama, color=warna, ha='center'
    )

plt.figure(figsize=(8, 6))

# Menggambar tiga bentuk
gambar_poligon(segitiga, 'red', 'Segitiga', (2.5, 3.7))
gambar_poligon(persegi, 'blue', 'Persegi', (7, 3.3))
gambar_poligon(segi_lima, 'green', 'Segi Lima', (3, 7.3))

# Mengatur bidang koordinat
plt.xlim(0, 9)
plt.ylim(0, 8)
plt.xticks(range(0, 10))
plt.yticks(range(0, 9))
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Visualisasi Poligon dengan Python')
plt.grid(True, linestyle='--', alpha=0.5)

plt.savefig('praktikum2.png', dpi=300, bbox_inches='tight')
plt.show()
