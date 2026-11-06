
import math
import matplotlib.pyplot as plt

# Исходные данные — вариант 20
m = 0.60
D = 0.08
v0 = 22.7
alpha = 56

Cw = 0.25
rho = 1.29
g = 9.81
dt = 0.001

S = math.pi * (D / 2) ** 2
k = 0.5 * Cw * rho * S


def flight_with_air(angle):
    angle = math.radians(angle)

    x, y = 0.0, 0.0
    vx = v0 * math.cos(angle)
    vy = v0 * math.sin(angle)

    t = 0.0
    xs, ys = [x], [y]

    max_height = 0.0
    t_up = None

    while True:
        v = math.hypot(vx, vy)

        ax = -(k / m) * v * vx
        ay = -g - (k / m) * v * vy

        # Метод Эйлера
        new_x = x + vx * dt
        new_y = y + vy * dt
        new_vx = vx + ax * dt
        new_vy = vy + ay * dt

        if t_up is None and new_vy <= 0:
            fraction = vy / (vy - new_vy)
            t_up = t + fraction * dt

        if new_y > max_height:
            max_height = new_y

        # Определяем момент пересечения земли
        if new_y <= 0:
            fraction = y / (y - new_y)

            x = x + fraction * (new_x - x)
            y = 0.0
            vx = vx + fraction * (new_vx - vx)
            vy = vy + fraction * (new_vy - vy)
            t += fraction * dt

            xs.append(x)
            ys.append(y)
            break

        x, y = new_x, new_y
        vx, vy = new_vx, new_vy
        t += dt

        xs.append(x)
        ys.append(y)

    return {
        "x": xs,
        "y": ys,
        "L": x,
        "H": max_height,
        "T": t,
        "v_end": math.hypot(vx, vy),
        "t_up": t_up,
        "t_down": t - t_up
    }


def flight_vacuum(angle):
    angle = math.radians(angle)

    T = 2 * v0 * math.sin(angle) / g
    L = v0**2 * math.sin(2 * angle) / g
    H = (v0 * math.sin(angle))**2 / (2 * g)

    times = [T * i / 500 for i in range(501)]

    xs = [v0 * math.cos(angle) * t for t in times]
    ys = [
        v0 * math.sin(angle) * t - 0.5 * g * t**2
        for t in times
    ]

    return {
        "x": xs,
        "y": ys,
        "L": L,
        "H": H,
        "T": T,
        "v_end": v0,
        "t_up": T / 2,
        "t_down": T / 2
    }


# Расчёт для исходного угла
air = flight_with_air(alpha)
vacuum = flight_vacuum(alpha)

print("Лабораторная работа №1 — вариант 20")
print(f"Начальный угол: {alpha}°\n")

print(f"{'Параметр':<22}{'С воздухом':>15}{'В вакууме':>15}")
print("-" * 52)

for name, key, unit in [
    ("Дальность", "L", "м"),
    ("Максимальная высота", "H", "м"),
    ("Время полёта", "T", "с"),
    ("Конечная скорость", "v_end", "м/с")
]:
    print(
        f"{name:<22}"
        f"{air[key]:>12.3f} {unit:<3}"
        f"{vacuum[key]:>12.3f} {unit}"
    )

# График №1 — траектории
plt.figure(figsize=(10, 6))
plt.plot(air["x"], air["y"], label="С сопротивлением воздуха")
plt.plot(vacuum["x"], vacuum["y"], "--", label="Без сопротивления")
plt.xlabel("Дальность x, м")
plt.ylabel("Высота y, м")
plt.title("Траектории полёта мяча")
plt.grid(True)
plt.legend()
plt.tight_layout()
# plt.savefig("trajectory.png", dpi=300)

# Поиск оптимального угла
angles = list(range(10, 81))
distances = [flight_with_air(a)["L"] for a in angles]

best_index = distances.index(max(distances))
best_angle = angles[best_index]

print(f"\nОптимальный угол с воздухом: {best_angle}°")
print(f"Максимальная дальность: {distances[best_index]:.3f} м")
print("Оптимальный угол в вакууме: 45°")

# График №2 — дальность от угла
plt.figure(figsize=(10, 6))
plt.plot(angles, distances, label="С сопротивлением воздуха")
plt.axvline(best_angle, color="red", linestyle="--",
            label=f"Оптимальный угол: {best_angle}°")
plt.axvline(45, color="green", linestyle=":",
            label="Вакуум: 45°")
plt.xlabel("Угол броска, градусы")
plt.ylabel("Дальность полёта, м")
plt.title("Зависимость дальности от угла броска")
plt.grid(True)
plt.legend()
plt.tight_layout()
# plt.savefig("angles.png", dpi=300)

# Время подъёма и спуска
print("\nС сопротивлением воздуха:")
print(f"Время подъёма: {air['t_up']:.4f} с")
print(f"Время спуска:  {air['t_down']:.4f} с")

print("\nВ вакууме:")
print(f"Время подъёма: {vacuum['t_up']:.4f} с")
print(f"Время спуска:  {vacuum['t_down']:.4f} с")

print("\nГрафики сохранены: trajectory.png и angles.png")

plt.show()
