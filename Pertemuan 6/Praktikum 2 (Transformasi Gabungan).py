
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Polygon, Circle, Ellipse
import numpy as np

# ==========================================
# PRAKTIKUM 2: TRANSFORMASI GABUNGAN
# Objek: Rumah Kartun 2D
# ==========================================

fig, ax = plt.subplots(figsize=(11, 7))

fig.patch.set_facecolor('#FFF1F5')
ax.set_facecolor('#DDF3FF')

ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.set_aspect('equal')

ax.set_title(
    'ANIMASI TRANSFORMASI GEOMETRI 2D',
    fontsize=16,
    fontweight='bold',
    color='#936B91',
    pad=15
)

ax.axis('off')

# ==========================================
# LATAR BELAKANG
# ==========================================

# Rumput
ax.axhspan(0, 0.8, color='#C7E8B5')

# Bukit
bukit1 = Ellipse(
    (2, 0.7), 5, 1.3,
    color='#B2DCA7'
)
bukit2 = Ellipse(
    (8, 0.7), 5, 1.3,
    color='#A5D69B'
)

ax.add_patch(bukit1)
ax.add_patch(bukit2)

# Matahari
ax.add_patch(Circle(
    (8.8, 5), 0.45,
    color='#FFE28A'
))

# Awan
for x, y in [(1, 4.9), (6, 5.2)]:
    for dx, dy, r in [
        (0, 0, 0.22),
        (0.25, 0.1, 0.28),
        (0.5, 0, 0.22)
    ]:
        ax.add_patch(Circle(
            (x + dx, y + dy), r,
            color='white'
        ))

# ==========================================
# BENTUK DASAR RUMAH
# ==========================================

# Semua titik rumah menggunakan koordinat X dan Y

house_parts = [
    # 0. Cerobong
    (
        [[2.8, 3.7], [3.25, 3.7],
         [3.25, 4.5], [2.8, 4.5]],
        '#B97857'
    ),

    # 1. Dinding rumah
    (
        [[2.5, 1.3], [4.5, 1.3],
         [4.5, 3.3], [2.5, 3.3]],
        '#FFE1A8'
    ),

    # 2. Atap
    (
        [[2.2, 3.25], [3.5, 4.5],
         [4.8, 3.25]],
        '#F26B65'
    ),

    # 3. Jendela kiri
    (
        [[2.7, 2.1], [3.35, 2.1],
         [3.35, 2.8], [2.7, 2.8]],
        '#73C7E8'
    ),

    # 4. Garis jendela vertikal
    (
        [[3.0, 2.1], [3.06, 2.1],
         [3.06, 2.8], [3.0, 2.8]],
        'white'
    ),

    # 5. Garis jendela horizontal
    (
        [[2.7, 2.42], [3.35, 2.42],
         [3.35, 2.48], [2.7, 2.48]],
        'white'
    ),

    # 6. Pintu
    (
        [[3.7, 1.3], [4.3, 1.3],
         [4.3, 2.65], [3.7, 2.65]],
        '#A96D50'
    ),

    # 7. Atap pintu
    (
        [[3.6, 2.65], [4.4, 2.65],
         [4.3, 2.8], [3.7, 2.8]],
        '#8E5949'
    ),

    # 8. Gagang pintu
    (
        [[4.17, 1.95], [4.23, 1.95],
         [4.23, 2.01], [4.17, 2.01]],
        '#FFD166'
    )
]

# Membuat objek rumah
house_patches = []

for points, color in house_parts:
    patch = Polygon(
        points,
        closed=True,
        facecolor=color,
        edgecolor='#684D52',
        linewidth=1.8,
        joinstyle='round'
    )

    ax.add_patch(patch)
    house_patches.append(patch)

# Bayangan rumah
shadow = Ellipse(
    (3.5, 1.05),
    2.5, 0.25,
    color='#728A9A',
    alpha=0.25
)
ax.add_patch(shadow)

# ==========================================
# TRANSFORMASI GEOMETRI
# ==========================================

# Titik pusat rumah
center = np.array([3.5, 2.6])

def transformasi(points, scale, angle, dx, dy):

    points = np.array(points, dtype=float)

    # Menggeser titik ke pusat koordinat
    points = points - center

    # 1. SCALLING
    points = points * scale

    # 2. ROTASI
    theta = np.deg2rad(angle)

    R = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])

    points = points @ R.T

    # Mengembalikan ke koordinat semula
    points = points + center

    # 3. TRANSLASI
    points[:, 0] += dx
    points[:, 1] += dy

    return points

# ==========================================
# FUNGSI UPDATE ANIMASI
# ==========================================

status = ax.text(
    5, 0.25,
    '',
    ha='center',
    fontsize=12,
    fontweight='bold',
    color='#765B88'
)

def update(frame):

    # Tahap 1: Scaling (0 - 20)
    if frame <= 20:

        scale = 1 - 0.2 * frame / 20
        angle = 0
        dx, dy = 0, 0

        status.set_text(
            'TAHAP 1: SCALING - Ukuran rumah menjadi 0.8 kali'
        )

    # Tahap 2: Rotasi (21 - 40)
    elif frame <= 40:

        scale = 0.8
        angle = 30 * (frame - 20) / 20
        dx, dy = 0, 0

        status.set_text(
            'TAHAP 2: ROTASI - Rumah berputar 30 derajat'
        )

    # Tahap 3: Translasi (41 - 60)
    else:

        scale = 0.8
        angle = 30

        progress = min((frame - 40) / 20, 1)

        dx = 3 * progress
        dy = 1 * progress

        status.set_text(
            'TAHAP 3: TRANSLASI - Rumah bergeser (+3, +1)'
        )

    # Memperbarui semua bagian rumah
    for patch, (points, color) in zip(
        house_patches, house_parts
    ):

        new_points = transformasi(
            points, scale, angle, dx, dy
        )

        patch.set_xy(new_points)

    # Memperbarui bayangan
    shadow.center = (
        center[0] + dx,
        1.05 + dy
    )

    shadow.width = 2.5 * scale

    return house_patches + [shadow, status]

# ==========================================
# MENJALANKAN ANIMASI
# ==========================================

ani = animation.FuncAnimation(
    fig,
    update,
    frames=91,
    interval=40,
    blit=False,
    repeat=True
)

# Menyimpan hasil animasi
ani.save(
    'praktikum2_transformasi_gabungan.gif',
    writer=animation.PillowWriter(fps=25)
)

plt.tight_layout()
plt.show()
