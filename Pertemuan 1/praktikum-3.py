x = int(input("Masukkan nilai x: "))

if x > 0:
    print("Titik di kanan layar")
elif x < 0:
    print("Titik di kiri layar")
else:
    print("Titik di tengah")

for i in range(1, 6):
    print("Iterasi titik:", i)