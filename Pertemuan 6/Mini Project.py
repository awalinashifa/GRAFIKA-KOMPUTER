
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Polygon, Circle
import numpy as np

# ==========================================
# MINI PROJECT: HOT AIR BALLOON
# Transformasi: Translasi dan Rotasi
# FPS: 60
# Durasi: 6 detik
# ==========================================

fig, ax = plt.subplots(figsize=(12, 7))

fig.patch.set_facecolor('#DDF2FF')
ax.set_facecolor('#BDE5FF')

ax.set_xlim(0, 12)
ax.set_ylim(0, 7)
ax.set_aspect('equal')
ax.axis('off')

ax.set_title(
    'HOT AIR BALLOON',
    fontsize=23,
    fontweight='bold',
    color='#816A9E',
    pad=18
)

# ==========================================
# 1. BACKGROUND DAN AWAN
# ==========================================

def buat_awan(x, y, scale=1):

    awan = []

    for dx, dy, r in [
        (0, 0, 0.3),
        (0.3, 0.15, 0.38),
        (0.7, 0.05, 0.3),
        (1.0, 0, 0.23)
    ]:

        lingkaran = Circle(
            (x + dx * scale, y + dy * scale),
            r * scale,
            color='white',
            zorder=2
        )

        ax.add_patch(lingkaran)
        awan.append(lingkaran)

    return awan


awan1 = buat_awan(0.5, 5.5, 0.9)
awan2 = buat_awan(4.8, 5.9, 0.7)
awan3 = buat_awan(8.8, 3.5, 0.7)
awan4 = buat_awan(1.5, 1.2, 0.65)

cloud_groups = [
    (awan1, 0.5),
    (awan2, 4.8),
    (awan3, 8.8),
    (awan4, 1.5)
]

# Simpan posisi awal setiap lingkaran awan
cloud_original_positions = []

for group, start_x in cloud_groups:

    positions = []

    for cloud in group:
        positions.append(cloud.center)

    cloud_original_positions.append(
        (group, start_x, positions)
    )


# Bintang dekorasi
np.random.seed(10)

for i in range(30):

    x = np.random.uniform(0.3, 11.7)
    y = np.random.uniform(1.5, 6.5)

    ax.scatter(
        x, y,
        marker='*',
        s=np.random.uniform(15, 40),
        color='#FFF3B0',
        alpha=0.8,
        zorder=2
    )


# Tulisan dekorasi
ax.text(
    6, 0.35,
    'Enjoy the journey and touch the sky!',
    ha='center',
    fontsize=12,
    color='#6786A6',
    style='italic'
)


# ==========================================
# 2. MEMBUAT BALON UDARA
# ==========================================

parts = []

def buat_bagian(points, color, edge='white',
                linewidth=1.8, zorder=5):

    patch = Polygon(
        points,
        closed=True,
        facecolor=color,
        edgecolor=edge,
        linewidth=linewidth,
        joinstyle='round',
        zorder=zorder
    )

    ax.add_patch(patch)

    parts.append(
        (patch, np.array(points, dtype=float))
    )


# Bentuk utama balon
buat_bagian(
    [
        [-0.9, -0.15],
        [-1.05, 0.35],
        [-1.0, 0.9],
        [-0.8, 1.45],
        [-0.4, 1.8],
        [0, 1.95],
        [0.4, 1.8],
        [0.8, 1.45],
        [1.0, 0.9],
        [1.05, 0.35],
        [0.9, -0.15]
    ],
    '#FF91B8',
    edge='#FFFFFF',
    linewidth=2.5,
    zorder=5
)


# Panel warna kiri
buat_bagian(
    [
        [-0.9, -0.15],
        [-1.05, 0.35],
        [-1.0, 0.9],
        [-0.8, 1.45],
        [-0.4, 1.8],
        [-0.25, 1.7],
        [-0.4, 1.3],
        [-0.45, 0.8],
        [-0.4, 0.2],
        [-0.35, -0.15]
    ],
    '#C9A5E8',
    zorder=6
)


# Panel warna kanan
buat_bagian(
    [
        [0.35, -0.15],
        [0.4, 0.2],
        [0.45, 0.8],
        [0.4, 1.3],
        [0.25, 1.7],
        [0.4, 1.8],
        [0.8, 1.45],
        [1.0, 0.9],
        [1.05, 0.35],
        [0.9, -0.15]
    ],
    '#8BC9EA',
    zorder=6
)


# Panel tengah
buat_bagian(
    [
        [-0.35, -0.15],
        [-0.4, 0.2],
        [-0.45, 0.8],
        [-0.4, 1.3],
        [-0.25, 1.7],
        [0, 1.95],
        [0.25, 1.7],
        [0.4, 1.3],
        [0.45, 0.8],
        [0.4, 0.2],
        [0.35, -0.15]
    ],
    '#FFD166',
    zorder=7
)


# Hiasan garis dekorasi pada balon
buat_bagian(
    [
        [-0.95, 0.15],
        [0.95, 0.15],
        [0.97, 0.28],
        [-0.97, 0.28]
    ],
    '#FFF0B5',
    zorder=8
)


# ==========================================
# 3. TALI DAN KERANJANG
# ==========================================

rope_left, = ax.plot(
    [], [],
    color='#A87955',
    linewidth=2.5,
    zorder=8
)

rope_right, = ax.plot(
    [], [],
    color='#A87955',
    linewidth=2.5,
    zorder=8
)


# Keranjang
buat_bagian(
    [
        [-0.48, -1.15],
        [0.48, -1.15],
        [0.36, -0.55],
        [-0.36, -0.55]
    ],
    '#B98257',
    edge='#79543D',
    linewidth=2,
    zorder=9
)


# Garis anyaman keranjang
basket_lines = []

for y in [-1.0, -0.85, -0.7]:

    line, = ax.plot(
        [], [],
        color='#E6BB87',
        linewidth=2,
        zorder=10
    )

    basket_lines.append((line, y))


# ==========================================
# 4. API PEMANAS BALON
# ==========================================

flame = Polygon(
    [
        [-0.12, -0.45],
        [0, -0.12],
        [0.12, -0.45]
    ],
    closed=True,
    facecolor='#FFB347',
    edgecolor='#FF8B42',
    linewidth=1.5,
    zorder=11
)

ax.add_patch(flame)


inner_flame = Polygon(
    [
        [-0.06, -0.44],
        [0, -0.25],
        [0.06, -0.44]
    ],
    closed=True,
    facecolor='#FFF1A8',
    edgecolor='none',
    zorder=12
)

ax.add_patch(inner_flame)


# ==========================================
# 5. FUNGSI TRANSFORMASI
# ==========================================

def transform(points, angle, tx, ty):

    theta = np.deg2rad(angle)

    R = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])

    result = points @ R.T

    result[:, 0] += tx
    result[:, 1] += ty

    return result


# ==========================================
# 6. FUNGSI ANIMASI
# ==========================================

def update(frame):

    progress = frame / 359

    # --------------------------------------
    # GERAKAN AWAN
    # Awan bergerak dari kanan ke kiri
    # --------------------------------------

    cloud_speed = 0.025
    cloud_shift = (frame * cloud_speed) % 15.5

    for group, start_x, positions in cloud_original_positions:

        offset = -cloud_shift

        # Awan muncul kembali dari sisi kanan
        if start_x + offset < -1.5:
            offset += 15.5

        for cloud, (original_x, original_y) in zip(group, positions):

            cloud.center = (
                original_x + offset,
                original_y
            )

    # --------------------------------------
    # GERAKAN BALON
    # --------------------------------------

    # TRANSLASI: bergerak dari kiri ke kanan
    tx = 1.8 + progress * 8.3

    # Gerakan naik dan turun
    ty = 3.9 + 0.35 * np.sin(
        progress * 4 * np.pi
    )

    # ROTASI: balon sedikit miring
    angle = 5 * np.sin(
        progress * 2 * np.pi
    )

    # Memindahkan seluruh bagian balon
    for patch, original_points in parts:

        new_points = transform(
            original_points,
            angle,
            tx,
            ty
        )

        patch.set_xy(new_points)

    # Tali balon
    ropes = transform(
        np.array([
            [-0.32, -0.15],
            [0.32, -0.15]
        ]),
        angle,
        tx,
        ty
    )

    basket = transform(
        np.array([
            [-0.36, -0.55],
            [0.36, -0.55]
        ]),
        angle,
        tx,
        ty
    )

    rope_left.set_data(
        [ropes[0, 0], basket[0, 0]],
        [ropes[0, 1], basket[0, 1]]
    )

    rope_right.set_data(
        [ropes[1, 0], basket[1, 0]],
        [ropes[1, 1], basket[1, 1]]
    )

    # Garis anyaman keranjang
    for line, y in basket_lines:

        points = transform(
            np.array([
                [-0.4, y],
                [0.4, y]
            ]),
            angle,
            tx,
            ty
        )

        line.set_data(
            points[:, 0],
            points[:, 1]
        )

    # Api pemanas
    api = transform(
        np.array([
            [-0.12, -0.45],
            [0, -0.12],
            [0.12, -0.45]
        ]),
        angle,
        tx,
        ty
    )

    flame.set_xy(api)

    api_dalam = transform(
        np.array([
            [-0.06, -0.44],
            [0, -0.25],
            [0.06, -0.44]
        ]),
        angle,
        tx,
        ty
    )

    inner_flame.set_xy(api_dalam)

    return (
        [patch for patch, _ in parts]
        + [
            rope_left,
            rope_right,
            flame,
            inner_flame
        ]
        + [line for line, _ in basket_lines]
        + [
            cloud
            for group, _, _ in cloud_original_positions
            for cloud in group
        ]
    )


# ==========================================
# 7. MENJALANKAN ANIMASI
# ==========================================

ani = animation.FuncAnimation(
    fig,
    update,
    frames=360,
    interval=1000/60,
    blit=False,
    repeat=True
)


# Simpan animasi GIF dengan 60 FPS
ani.save(
    'mini_project_baloon_udara.gif',
    writer=animation.PillowWriter(fps=60)
)

plt.tight_layout()
plt.show()
