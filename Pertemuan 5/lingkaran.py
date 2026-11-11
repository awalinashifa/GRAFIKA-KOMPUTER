
import matplotlib.pyplot as plt

# Fungsi menggambar lingkaran menggunakan Midpoint Circle Algorithm
def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    d = 1 - r
    points = []

    while x <= y:
        for px, py in [
            (x, y), (y, x),
            (-x, y), (-y, x),
            (x, -y), (y, -x),
            (-x, -y), (-y, -x)
        ]:
            points.append((xc + px, yc + py))

        if d < 0:
            d = d + 2 * x + 3
        else:
            d = d + 2 * (x - y) + 5
            y -= 1

        x += 1

    return points


# Menggambar lingkaran dengan jari-jari 8
pts = midpoint_circle(0, 0, 8)

x, y = zip(*pts)

plt.figure(figsize=(6, 6))
plt.scatter(x, y, c='red')
plt.axis('equal')
plt.grid(True)
plt.title('Lingkaran (r = 8) - Midpoint Algorithm')
plt.xlabel('X')
plt.ylabel('Y')

# Menyimpan gambar
plt.savefig('lingkaran_r8.png')

plt.show()
