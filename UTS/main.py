import pygame
import sys
import math

# =========================================================
# PENJAGA TERUMBU - MISI MENYELAMATKAN KARANG
# Materi: koordinat 2D, Bresenham, Midpoint Circle, poligon,
# translasi, rotasi, scaling, animasi, dan layering.
# =========================================================

pygame.init()

WIDTH, HEIGHT = 960, 600
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Penjaga Terumbu - Misi Menyelamatkan Karang")
clock = pygame.time.Clock()

# Warna
WHITE = (240, 250, 250)
NAVY = (7, 34, 67)
BLUE = (10, 86, 125)
LIGHT_BLUE = (90, 205, 222)
CORAL = (248, 112, 107)
YELLOW = (255, 208, 105)
GREEN = (74, 190, 145)
DARK_GREEN = (29, 123, 109)
SAND = (194, 158, 105)
DARK = (24, 71, 91)
GREY = (105, 110, 115)

font_title = pygame.font.SysFont("arial", 42, bold=True)
font_large = pygame.font.SysFont("arial", 28, bold=True)
font = pygame.font.SysFont("arial", 20, bold=True)
small_font = pygame.font.SysFont("arial", 15)


# =========================================================
# TRANSFORMASI GEOMETRI 2D
# =========================================================
def translate_point(x, y, tx, ty):
    """Translasi: memindahkan titik sejauh tx dan ty."""
    return x + tx, y + ty


def rotate_point(x, y, angle_degrees, center_x=0, center_y=0):
    """Rotasi titik terhadap titik pusat tertentu."""
    angle = math.radians(angle_degrees)
    x -= center_x
    y -= center_y
    new_x = x * math.cos(angle) - y * math.sin(angle)
    new_y = x * math.sin(angle) + y * math.cos(angle)
    return new_x + center_x, new_y + center_y


def scale_point(x, y, scale, center_x=0, center_y=0):
    """Scaling: mengubah ukuran/jarak titik dari titik pusat."""
    return (
        center_x + (x - center_x) * scale,
        center_y + (y - center_y) * scale
    )


# =========================================================
# ALGORITMA BRESENHAM
# =========================================================
def put_pixel(surface, x, y, color):
    x, y = int(round(x)), int(round(y))
    if 0 <= x < surface.get_width() and 0 <= y < surface.get_height():
        surface.set_at((x, y), color)


def bresenham(surface, x0, y0, x1, y1, color):
    x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    error = dx - dy

    while True:
        put_pixel(surface, x0, y0, color)
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * error
        if e2 > -dy:
            error -= dy
            x0 += sx
        if e2 < dx:
            error += dx
            y0 += sy


# =========================================================
# ALGORITMA MIDPOINT CIRCLE
# =========================================================
def midpoint_circle(surface, cx, cy, radius, color, fill=False):
    cx, cy, radius = int(cx), int(cy), max(1, int(radius))
    x, y = 0, radius
    decision = 1 - radius

    while x <= y:
        if fill:
            pygame.draw.line(surface, color, (cx - x, cy + y), (cx + x, cy + y))
            pygame.draw.line(surface, color, (cx - x, cy - y), (cx + x, cy - y))
            pygame.draw.line(surface, color, (cx - y, cy + x), (cx + y, cy + x))
            pygame.draw.line(surface, color, (cx - y, cy - x), (cx + y, cy - x))
        else:
            points = [
                (x, y), (y, x), (-x, y), (-y, x),
                (x, -y), (y, -x), (-x, -y), (-y, -x)
            ]
            for px, py in points:
                put_pixel(surface, cx + px, cy + py, color)

        x += 1
        if decision < 0:
            decision += 2 * x + 1
        else:
            y -= 1
            decision += 2 * (x - y) + 1


# =========================================================
# POLIGON
# =========================================================
def draw_polygon(surface, points, color):
    points = [(int(x), int(y)) for x, y in points]
    if len(points) < 3:
        return
    pygame.draw.polygon(surface, color, points)
    for i in range(len(points)):
        a = points[i]
        b = points[(i + 1) % len(points)]
        bresenham(surface, a[0], a[1], b[0], b[1], color)


# =========================================================
# BACKGROUND LAUT
# =========================================================
def draw_background(t):
    for y in range(HEIGHT):
        factor = y / HEIGHT
        color = (
            int(6 + 5 * factor),
            int(43 + 47 * factor),
            int(83 + 39 * factor)
        )
        pygame.draw.line(screen, color, (0, y), (WIDTH, y))

    # Sinar matahari: layer transparan di belakang semua objek
    light_layer = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    for i in range(4):
        x = 100 + i * 210 + math.sin(t * 0.5 + i) * 18
        pygame.draw.polygon(
            light_layer, (106, 220, 225, 22),
            [(x, 0), (x + 80, 0), (x + 230, HEIGHT), (x + 130, HEIGHT)]
        )
    screen.blit(light_layer, (0, 0))

    pygame.draw.rect(screen, SAND, (0, 500, WIDTH, 100))

    for i in range(25):
        x = (i * 47 + 20) % WIDTH
        bresenham(screen, x, 500, x + 12, 493 - (i % 3) * 3, (225, 185, 125))

    # Gelembung latar bergerak naik (translasi)
    for i in range(15):
        x = (i * 91 + int(t * 12)) % WIDTH
        y = 80 + (i * 57 - int(t * 20)) % 390
        midpoint_circle(screen, x, y, 2 + (i % 3), LIGHT_BLUE)


# =========================================================
# OBJEK KARANG
# =========================================================
def draw_coral(surface, x, base_y, scale=1.0, healthy=True):
    color = CORAL if healthy else GREY
    height = int(58 * scale)

    bresenham(surface, x, base_y, x, base_y - height, color)

    branches = [(-22, -27), (20, -38), (-15, -50), (17, -59)]
    for j, (dx, dy) in enumerate(branches):
        bx = int(x + dx * scale)
        by = int(base_y + dy * scale)
        start_y = base_y - int((j + 1) * 10 * scale)
        bresenham(surface, x, start_y, bx, by, color)
        midpoint_circle(surface, bx, by, max(2, int(5 * scale)), color, True)

    midpoint_circle(surface, x, base_y - height, max(2, int(6 * scale)), color, True)

    if healthy:
        midpoint_circle(
            surface, int(x - 10 * scale),
            int(base_y - height - 7 * scale), 2, YELLOW, True
        )


# =========================================================
# OBJEK IKAN - ROTASI DITERAPKAN PADA TITIK-TITIK POLIGON
# =========================================================
def draw_fish(x, y, scale, direction, t):
    # Ekor bergerak naik-turun
    wiggle = math.sin(t * 7 + x * 0.01) * 5
    tail_local = [
        (-30, 0),
        (-50, -13 + wiggle),
        (-50, 13 - wiggle)
    ]

    # Ikan sedikit mengangguk (rotasi), mengikuti gelombang vertikal
    angle = math.sin(t * 2 + x * 0.01) * 7

    def transform(local_x, local_y):
        # Scaling ukuran ikan, lalu rotasi, lalu translasi ke posisi layar.
        sx, sy = scale_point(local_x, local_y, scale)
        rx, ry = rotate_point(sx, sy, angle)
        return int(x + direction * rx), int(y + ry)

    tail = [transform(px, py) for px, py in tail_local]
    draw_polygon(screen, tail, CORAL)

    # Badan ikan sebagai elips pada layer transparan, lalu diputar
    fish_surface = pygame.Surface((90, 60), pygame.SRCALPHA)
    pygame.draw.ellipse(fish_surface, YELLOW, (14, 13, 62, 34))
    pygame.draw.circle(fish_surface, NAVY, (65, 24), 3)
    scaled_surface = pygame.transform.smoothscale(
        fish_surface,
        (max(1, int(fish_surface.get_width() * scale)),
         max(1, int(fish_surface.get_height() * scale)))
    )
    rotated = pygame.transform.rotate(scaled_surface, -angle * direction)
    rect = rotated.get_rect(center=(int(x), int(y)))
    screen.blit(rotated, rect)


# =========================================================
# OBJEK PENYU
# =========================================================
def draw_turtle(x, y, t):
    wiggle = math.sin(t * 8) * 5

    pygame.draw.ellipse(screen, GREEN, (x - 30, y + 8 + wiggle, 25, 13))
    pygame.draw.ellipse(screen, GREEN, (x - 8, y + 14 - wiggle, 24, 12))

    pygame.draw.ellipse(screen, DARK_GREEN, (x - 39, y - 24, 58, 43))
    pygame.draw.ellipse(screen, GREEN, (x - 31, y - 20, 42, 33))

    for dx in (-18, -2, 13):
        bresenham(screen, x + dx, y - 18, x + dx + 3, y + 8, LIGHT_BLUE)

    pygame.draw.ellipse(screen, GREEN, (x + 13, y - 17, 30, 25))
    midpoint_circle(screen, x + 35, y - 8, 3, NAVY, True)
    pygame.draw.ellipse(screen, GREEN, (x - 8, y + 8 + wiggle, 26, 14))


# =========================================================
# OBJEK SAMPAH
# =========================================================
def draw_trash(x, y, t):
    sway = math.sin(t * 2.5) * 5
    points = [
        (x - 19 + sway, y - 23),
        (x + 15 + sway, y - 20),
        (x + 19 - sway, y + 23),
        (x - 14 - sway, y + 21)
    ]
    draw_polygon(screen, points, (82, 177, 190))
    bresenham(screen, x - 13, y - 10, x + 12, y - 7, BLUE)


# =========================================================
# DATA PERMAINAN
# =========================================================
def reset_game():
    return {
        "time": 0.0,
        "started": False,
        "turtle_x": 110.0,
        "turtle_y": 350.0,
        "score": 0,
        "trash": [True, True],
        "respawn": [None, None],
        # Setiap karang menyimpan posisi dan waktu mulai tumbuh.
        "planted": [],
        "next_plant": 0.0
    }


state = reset_game()
trash_positions = [(690, 398), (790, 455)]


# =========================================================
# PROGRAM UTAMA
# =========================================================
running = True

while running:
    dt = clock.tick(FPS) / 1000.0
    dt = min(dt, 0.05)  # Membatasi lonjakan waktu bila jendela sempat tersendat.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                state["started"] = True
            elif event.key == pygame.K_r:
                state = reset_game()
            elif event.key == pygame.K_e and state["started"]:
                if (
                    state["turtle_y"] >= 430
                    and state["time"] >= state["next_plant"]
                    and len(state["planted"]) < 3
                ):
                    state["planted"].append({
                        "x": state["turtle_x"],
                        "start": state["time"]
                    })
                    state["score"] += 100
                    state["next_plant"] = state["time"] + 0.8

    # UPDATE: translasi penyu menggunakan keyboard.
    if state["started"]:
        state["time"] += dt
        keys = pygame.key.get_pressed()
        speed = 230 * dt

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            state["turtle_x"] -= speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            state["turtle_x"] += speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            state["turtle_y"] -= speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            state["turtle_y"] += speed

        state["turtle_x"] = max(40, min(WIDTH - 60, state["turtle_x"]))
        state["turtle_y"] = max(100, min(465, state["turtle_y"]))

    t = state["time"]

    # Deteksi tabrakan penyu dengan sampah.
    for i, (tx, ty) in enumerate(trash_positions):
        trash_y = ty + math.sin(t * 2 + i) * 7
        distance = math.hypot(state["turtle_x"] - tx, state["turtle_y"] - trash_y)

        if state["started"] and state["trash"][i] and distance < 48:
            state["trash"][i] = False
            state["respawn"][i] = t + 2
            state["score"] += 50

        if (
            state["started"]
            and not state["trash"][i]
            and state["respawn"][i] is not None
            and t >= state["respawn"][i]
        ):
            state["trash"][i] = True
            state["respawn"][i] = None

    # -----------------------------------------------------
    # RENDER / Z-ORDER: latar -> objek jauh -> objek dekat -> UI
    # -----------------------------------------------------
    draw_background(t)

    # Karang alami di dasar laut.
    for i in range(5):
        x = 150 + i * 150
        coral_scale = 0.75 + (i % 3) * 0.12
        draw_coral(screen, x, 500, coral_scale, healthy=True)

    # Karang yang ditanam tumbuh dari kecil ke ukuran normal.
    for coral in state["planted"]:
        age = max(0.0, t - coral["start"])
        growth = min(1.0, age / 1.2)
        # Scaling animasi: ukuran bertambah dari 0.15 menjadi 0.85.
        growing_scale = 0.15 + 0.70 * growth
        draw_coral(screen, int(coral["x"]), 500, growing_scale, healthy=True)

    # Batu dan rumput laut.
    for x in (80, 870):
        midpoint_circle(screen, x, 492, 28, DARK_GREEN, True)
        for k in range(3):
            bresenham(
                screen, x + k * 8 - 8, 495,
                x + k * 7 - 11, 465 - k * 5, GREEN
            )

    # Sampah.
    for i, (tx, ty) in enumerate(trash_positions):
        if state["trash"][i]:
            draw_trash(tx, int(ty + math.sin(t * 2 + i) * 7), t)

    # Ikan berenang. Posisi ikan berubah (translasi) dan badan berotasi.
    for i in range(3):
        fish_speed = 95 + i * 18
        raw = (t * fish_speed + i * 340) % (WIDTH + 130)

        if raw < WIDTH + 65:
            direction = 1
            x = raw - 65
        else:
            direction = -1
            x = WIDTH + 65 - (raw - (WIDTH + 65))

        y = 175 + i * 68 + math.sin(t * 2 + i) * 12
        draw_fish(x, y, 0.72 + i * 0.09, direction, t)

    # Penyu sebagai objek utama yang dikendalikan pemain.
    draw_turtle(int(state["turtle_x"]), int(state["turtle_y"]), t)

    # Gelembung dari penyu.
    if state["started"]:
        for i in range(5):
            bx = int(state["turtle_x"] - 12 + i * 12)
            by = int(state["turtle_y"] - 35 - ((t * 55 + i * 47) % 150))
            midpoint_circle(screen, bx, by, 3 + i % 2, LIGHT_BLUE)

    # UI / informasi permainan.
    screen.blit(font_large.render("PENJAGA TERUMBU", True, WHITE), (24, 18))
    screen.blit(
        small_font.render("Misi: Selamatkan ekosistem laut!", True, LIGHT_BLUE),
        (26, 55)
    )
    screen.blit(
        font.render(f"SKOR: {state['score']}", True, YELLOW),
        (WIDTH - 165, 22)
    )
    screen.blit(
        small_font.render(f"Karang ditanam: {len(state['planted'])}/3", True, WHITE),
        (WIDTH - 180, 55)
    )
    screen.blit(
        small_font.render(
            "WASD/Panah: Gerak | E: Tanam karang | R: Ulangi | ESC: Keluar",
            True, WHITE
        ),
        (24, HEIGHT - 27)
    )

    if len(state["planted"]) >= 3:
        message = font_large.render("TERUMBU BERHASIL DISELAMATKAN!", True, YELLOW)
        screen.blit(message, message.get_rect(center=(WIDTH // 2, 100)))

    # Halaman pembuka.
    if not state["started"]:
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((2, 18, 40, 205))
        screen.blit(overlay, (0, 0))

        heading = font_title.render("PENJAGA TERUMBU", True, WHITE)
        screen.blit(heading, heading.get_rect(center=(WIDTH // 2, 190)))

        subtitle = font.render("Misi Menyelamatkan Ekosistem Laut", True, LIGHT_BLUE)
        screen.blit(subtitle, subtitle.get_rect(center=(WIDTH // 2, 245)))

        instruction = small_font.render(
            "Gerakkan penyu untuk mengumpulkan sampah dan menanam karang.",
            True, WHITE
        )
        screen.blit(instruction, instruction.get_rect(center=(WIDTH // 2, 305)))

        controls = small_font.render(
            "WASD / PANAH = Bergerak     E = Tanam Karang",
            True, YELLOW
        )
        screen.blit(controls, controls.get_rect(center=(WIDTH // 2, 345)))

        start = font_large.render("TEKAN SPACE UNTUK MULAI", True, WHITE)
        screen.blit(start, start.get_rect(center=(WIDTH // 2, 410)))

    pygame.display.flip()


pygame.quit()
sys.exit()
