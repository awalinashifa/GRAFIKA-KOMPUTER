
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.patches import Circle, Ellipse

# ==========================================
# PRAKTIKUM 1: TRANSLASI DAN ROTASI
# Tema: Cute Pastel Animation
# ==========================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

fig.patch.set_facecolor('#FFF0F5')
fig.suptitle(
    'TRANSFORMASI GEOMETRI 2D',
    fontsize=17,
    fontweight='bold',
    color='#A66C91'
)

# ==========================================
# BAGIAN 1: ANIMASI TRANSLASI BOLA
# ==========================================

ax1.set_xlim(0, 10)
ax1.set_ylim(0, 5)
ax1.set_facecolor('#E6F5FF')
ax1.set_title('1. TRANSLASI', color='#628DB5',
              fontsize=13, fontweight='bold')
ax1.set_aspect('equal')
ax1.axis('off')

# Awan
for x, y in [(1, 4.3), (7.5, 4.2)]:
    for dx, dy, r in [
        (0, 0, 0.25),
        (0.25, 0.08, 0.3),
        (0.5, 0, 0.23)
    ]:
        ax1.add_patch(Circle(
            (x + dx, y + dy), r,
            color='white'
        ))

# Rumput
ax1.axhspan(0, 0.8, color='#C9EBC5')

# Bayangan bola
shadow = Ellipse(
    (1, 1.05), 1, 0.2,
    color='#A7B8C9', alpha=0.3
)
ax1.add_patch(shadow)

# Badan bola
ball = Circle(
    (1, 2), 0.55,
    color='#FF91B8',
    ec='#E66D9B',
    linewidth=2
)
ax1.add_patch(ball)

# Mata
eye1 = Circle((0.8, 2.15), 0.055, color='#493342')
eye2 = Circle((1.2, 2.15), 0.055, color='#493342')
ax1.add_patch(eye1)
ax1.add_patch(eye2)

# Pipi
cheek1 = Circle((0.68, 1.98), 0.09,
                color='#FFB0C8', alpha=0.8)
cheek2 = Circle((1.32, 1.98), 0.09,
                color='#FFB0C8', alpha=0.8)
ax1.add_patch(cheek1)
ax1.add_patch(cheek2)

# Senyum
smile, = ax1.plot([], [], color='#493342',
                  linewidth=2)

# Teks
label = ax1.text(
    5, 0.3, 'Bola sedang bergerak!',
    ha='center', color='#628DB5',
    fontsize=10
)

# ==========================================
# BAGIAN 2: ANIMASI ROTASI KINCIR
# ==========================================

ax2.set_xlim(0, 10)
ax2.set_ylim(0, 5)
ax2.set_facecolor('#F5E9FF')
ax2.set_title('2. ROTASI', color='#9874B8',
              fontsize=13, fontweight='bold')
ax2.set_aspect('equal')
ax2.axis('off')

# Batang kincir
ax2.plot([5, 5], [0.8, 2.5],
         color='#A58AC7', linewidth=5,
         solid_capstyle='round')

# Pusat kincir
center = (5, 2.8)

# Warna kelopak
colors = [
    '#FF91B8',
    '#FFD166',
    '#A8D8EA',
    '#CDB4DB',
    '#BDE0A8',
    '#FFB4A2'
]

petals = []

# Membuat 6 kelopak
for color in colors:
    petal = Ellipse(
        center,
        width=0.9,
        height=0.42,
        color=color,
        ec='white',
        linewidth=1.5
    )
    ax2.add_patch(petal)
    petals.append(petal)

# Pusat kincir
hub = Circle(
    center, 0.22,
    color='#FFF1A8',
    ec='white',
    linewidth=2,
    zorder=10
)
ax2.add_patch(hub)

ax2.text(
    5, 0.3, 'Kincir sedang berputar!',
    ha='center', color='#9874B8',
    fontsize=10
)

# ==========================================
# FUNGSI ANIMASI
# ==========================================

def update(frame):

    # ---- TRANSLASI ----

    x = 1 + (frame / 179) * 8

    # Memindahkan bola
    ball.center = (x, 2)

    # Memindahkan mata
    eye1.center = (x - 0.2, 2.15)
    eye2.center = (x + 0.2, 2.15)

    # Memindahkan pipi
    cheek1.center = (x - 0.32, 1.98)
    cheek2.center = (x + 0.32, 1.98)

    # Memindahkan senyum
    smile_x = np.linspace(x - 0.13, x + 0.13, 30)
    smile_y = 1.96 - 0.07 * np.sin(
        np.linspace(0, np.pi, 30)
    )
    smile.set_data(smile_x, smile_y)

    # Memindahkan bayangan
    shadow.center = (x, 1.05)

    # ---- ROTASI ----

    angle = np.deg2rad(frame * 6)

    for i, petal in enumerate(petals):

        # Sudut masing-masing kelopak
        theta = angle + i * 2 * np.pi / 6

        # Posisi kelopak mengelilingi pusat
        px = center[0] + 0.48 * np.cos(theta)
        py = center[1] + 0.48 * np.sin(theta)

        petal.center = (px, py)
        petal.angle = np.rad2deg(theta)

    return (
        ball, eye1, eye2,
        cheek1, cheek2, smile,
        shadow, hub, *petals
    )

# ==========================================
# MENJALANKAN ANIMASI
# ==========================================

ani = animation.FuncAnimation(
    fig,
    update,
    frames=180,
    interval=33,
    blit=False
)

# Simpan hasil animasi
ani.save(
    'praktikum1_translasi_rotasi.gif',
    writer=animation.PillowWriter(fps=30)
)

plt.tight_layout()
plt.show()
