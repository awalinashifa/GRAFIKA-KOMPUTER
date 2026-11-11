
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle, Rectangle

# Membuat bidang gambar
fig, ax = plt.subplots(figsize=(10, 6))

# 1. BADAN MOBIL
badan = [
    (1, 2), (1.5, 3.2), (3, 3.2),
    (4, 4.5), (6.5, 4.5), (8, 3.2),
    (9, 3.2), (9.5, 2.5), (9.5, 2),
    (1, 2)
]

ax.add_patch(Polygon(
    badan, closed=True,
    facecolor='red',
    edgecolor='black',
    linewidth=2,
    zorder=2
))

# 2. ATAP MOBIL
atap = [
    (2.7, 3.2),
    (4.1, 4.4),
    (6.4, 4.4),
    (7.6, 3.2)
]

ax.add_patch(Polygon(
    atap, closed=True,
    facecolor='firebrick',
    edgecolor='black',
    linewidth=2,
    zorder=3
))

# 3. JENDELA KIRI
ax.add_patch(Polygon(
    [(3.1, 3.35), (4.25, 4.2),
     (5.0, 4.2), (5.0, 3.35)],
    closed=True,
    facecolor='lightblue',
    edgecolor='black',
    linewidth=1.5,
    zorder=4
))

# 4. JENDELA KANAN
ax.add_patch(Polygon(
    [(5.2, 3.35), (5.2, 4.2),
     (6.3, 4.2), (7.2, 3.35)],
    closed=True,
    facecolor='lightblue',
    edgecolor='black',
    linewidth=1.5,
    zorder=4
))

# 5. GARIS PEMISAH JENDELA
ax.plot([5.1, 5.1], [3.25, 4.35],
        color='black', linewidth=2, zorder=5)

# 6. RODA KIRI
ax.add_patch(Circle(
    (3, 2), 0.75,
    facecolor='black',
    edgecolor='black',
    zorder=5
))

ax.add_patch(Circle(
    (3, 2), 0.38,
    facecolor='silver',
    edgecolor='black',
    linewidth=1.5,
    zorder=6
))

# 7. RODA KANAN
ax.add_patch(Circle(
    (7.5, 2), 0.75,
    facecolor='black',
    edgecolor='black',
    zorder=5
))

ax.add_patch(Circle(
    (7.5, 2), 0.38,
    facecolor='silver',
    edgecolor='black',
    linewidth=1.5,
    zorder=6
))

# 8. LAMPU DEPAN
ax.add_patch(Rectangle(
    (9.15, 2.65), 0.3, 0.3,
    facecolor='yellow',
    edgecolor='black',
    zorder=4
))

# 9. LAMPU BELAKANG
ax.add_patch(Rectangle(
    (1.05, 2.65), 0.3, 0.3,
    facecolor='orange',
    edgecolor='black',
    zorder=4
))

# 10. GAGANG PINTU
ax.plot([5.5, 6.1], [3.0, 3.0],
        color='black', linewidth=2, zorder=5)

# 11. GARIS JALAN
ax.plot([0, 10], [1.1, 1.1],
        color='gray', linewidth=2, zorder=1)

# 12. PENGATURAN GRAFIK
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)

ax.set_xticks(range(0, 11))
ax.set_yticks(range(0, 7))

ax.set_xlabel('X')
ax.set_ylabel('Y')

ax.set_title(
    'Mini Project: Menggambar Mobil dengan Python',
    fontsize=14
)

ax.grid(True, linestyle='--', alpha=0.4)
ax.set_aspect('equal', adjustable='box')

# 13. SIMPAN DAN TAMPILKAN GAMBAR
plt.savefig(
    'mini_project_mobil.png',
    dpi=300,
    bbox_inches='tight'
)

plt.show()
