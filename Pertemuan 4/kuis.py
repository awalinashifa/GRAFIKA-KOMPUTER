
import matplotlib.pyplot as plt

# Titik awal dan titik akhir
x1, y1 = 1, 1
x2, y2 = 8, 5

# Menghitung selisih koordinat
dx = x2 - x1
dy = y2 - y1

# Parameter awal Bresenham
p = 2 * dy - dx

# Menyimpan koordinat piksel
x_points = [x1]
y_points = [y1]

x, y = x1, y1

# Algoritma Bresenham
while x < x2:
    x += 1

    if p < 0:
        p = p + 2 * dy
    else:
        y += 1
        p = p + 2 * dy - 2 * dx

    x_points.append(x)
    y_points.append(y)

# Menggambar garis
plt.figure(figsize=(9, 6))

plt.plot(
    x_points, y_points,
    color="blue",
    marker="s",
    markersize=8,
    linewidth=2,
    label="Garis Bresenham"
)

# Memberi label koordinat setiap piksel
for x, y in zip(x_points, y_points):
    plt.text(x, y + 0.15, f"({x},{y})",
             ha="center", fontsize=9)

# Mengatur tampilan grafik
plt.title("Ilustrasi Garis Algoritma Bresenham")
plt.xlabel("Koordinat X")
plt.ylabel("Koordinat Y")
plt.xticks(range(0, 10))
plt.yticks(range(0, 8))
plt.xlim(0, 9)
plt.ylim(0, 7)
plt.grid(True)
plt.legend()
plt.gca().set_aspect("equal", adjustable="box")

plt.show()
