
import matplotlib.pyplot as plt

# Fungsi menggambar poligon
def gambar_poligon(ax, vertex, judul, warna, warna_garis):
    x = [p[0] for p in vertex]
    y = [p[1] for p in vertex]

    # Mengisi area poligon
    ax.fill(x, y, color=warna, alpha=0.8)

    # Menggambar garis dan titik sudut
    ax.plot(x + [x[0]], y + [y[0]],
            color=warna_garis,
            marker='o',
            markerfacecolor=warna_garis,
            linewidth=2.5,
            markersize=7)

    ax.set_title(judul, fontsize=13, fontweight='bold')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 6)
    ax.set_xticks(range(7))
    ax.set_yticks(range(7))
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.4)


# Daftar titik poligon
segitiga = [(1, 1), (3, 4), (5, 1)]

persegi = [(1, 1), (1, 5), (5, 5), (5, 1)]

segi_lima = [(2, 1), (4, 1), (5, 3), (3, 5), (1, 3)]

segi_enam = [
    (1, 3),
    (2, 5),
    (4, 5),
    (5, 3),
    (4, 1),
    (2, 1)
]


# Membuat tampilan grafik
fig, axes = plt.subplots(2, 2, figsize=(10, 10))

# Menggambar setiap poligon dengan warna berbeda
gambar_poligon(
    axes[0, 0], segitiga, 'Segitiga',
    '#FFB5D8', '#E75480'
)

gambar_poligon(
    axes[0, 1], persegi, 'Persegi',
    '#B7E4C7', '#40916C'
)

gambar_poligon(
    axes[1, 0], segi_lima, 'Segi Lima',
    '#D8C4F1', '#8055B5'
)

gambar_poligon(
    axes[1, 1], segi_enam, 'Segi Enam',
    '#FFE8A3', '#D69E27'
)

plt.suptitle(
    'Menggambar Poligon dengan Python',
    fontsize=17,
    fontweight='bold'
)

plt.tight_layout(rect=[0, 0, 1, 0.95])

# Menyimpan hasil gambar
plt.savefig('hasil_poligon.png', dpi=300, bbox_inches='tight')

plt.show()
