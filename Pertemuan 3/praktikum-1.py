
import matplotlib.pyplot as plt

# Daftar titik: nama, koordinat x, koordinat y, warna
titik = [
    ('A', 1, 2, 'red'),
    ('B', 3, 4, 'blue'),
    ('C', 5, 1, 'green'),
    ('D', 4, 3, 'orange'),
    ('E', 2, 5, 'purple')
]

# Membuat bidang koordinat
plt.figure(figsize=(8, 5))

# Menggambar setiap titik dan labelnya
for nama, x, y, warna in titik:
    plt.scatter(x, y, color=warna, s=100)
    plt.annotate(
        f'{nama}({x}, {y})',
        (x, y),
        xytext=(5, 5),
        textcoords='offset points'
    )

# Mengatur tampilan grafik
plt.xlim(0, 6)
plt.ylim(0, 6)
plt.xticks(range(0, 7))
plt.yticks(range(0, 7))
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Visualisasi Beberapa Titik pada Bidang Koordinat')
plt.grid(True, linestyle='--', alpha=0.5)

plt.savefig('praktikum1.png', dpi=300, bbox_inches='tight')
plt.show()
