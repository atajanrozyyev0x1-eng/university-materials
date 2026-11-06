from builtins import print
from math import sin, cos, radians, hypot, pi
import matplotlib.pyplot as plt

# Вариант 20
m, D, v0, alpha = 0.60, 0.08, 22.7, 56
Cw, rho, g, dt = 0.25, 1.29, 9.81, 0.001
k = 0.5 * Cw * rho * pi * (D / 2)**2


def flight(angle):
    a = radians(angle)
    x = y = t = 0.0
    vx, vy = v0 * cos(a), v0 * sin(a)
    X, Y = [0.0], [0.0]
    H = t_up = None

    while True:
        v = hypot(vx, vy)
        ax, ay = -k / m * v * vx, -g - k / m * v * vy
        xn, yn = x + vx * dt, y + vy * dt
        vxn, vyn = vx + ax * dt, vy + ay * dt

        if vy >= 0 > vyn:
            q = vy / (vy - vyn)
            t_up = t + q * dt
            H = y + vy * q * dt + 0.5 * ay * (q * dt)**2

        if yn <= 0 and t > 0:
            q = y / (y - yn)
            T = t + q * dt
            L = x + q * (xn - x)
            vend = hypot(vx + q * (vxn - vx),
                          vy + q * (vyn - vy))
            X.append(L)
            Y.append(0)
            return X, Y, [L, H, T, vend], t_up, T - t_up

        x, y, vx, vy = xn, yn, vxn, vyn
        t += dt
        X.append(x)
        Y.append(y)


def vacuum(angle):
    a = radians(angle)
    T = 2 * v0 * sin(a) / g
    times = [T * i / 400 for i in range(401)]
    return ([v0 * cos(a) * t for t in times],
            [v0 * sin(a) * t - g * t*t / 2 for t in times],
            [v0*v0 * sin(2*a) / g,
             (v0*sin(a))**2 / (2*g), T, v0])


X, Y, air, t_up, t_down = flight(alpha)
X0, Y0, vac = vacuum(alpha)

print('Вариант 20 — с воздухом / вакуум')
for name, p, q in zip(
    ['L, м', 'H, м', 'T, с', 'v_end, м/с'], air, vac
):
    print(f'{name}: {p:.4f} / {q:.4f}')

print(f'Подъём: {t_up:.4f} с; спуск: {t_down:.4f} с')

angles = list(range(10, 81))
ranges = [flight(a)[2][0] for a in angles]
best = angles[ranges.index(max(ranges))]

fine = [43 + i / 10 for i in range(31)]
fine_ranges = [flight(a)[2][0] for a in fine]
i = fine_ranges.index(max(fine_ranges))

print(f'Оптимум: {best}°, L = {max(ranges):.4f} м')
print(f'Уточнение: {fine[i]:.1f}°, L = {fine_ranges[i]:.4f} м')

plt.figure(figsize=(9, 5))
plt.plot(X, Y, color='teal', label='С сопротивлением')
plt.plot(X0, Y0, '--', color='purple', label='Вакуум')
plt.xlabel('Дальность, м')
plt.ylabel('Высота, м')
plt.title('Траектории полёта — вариант 20')
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig('trajectory.png', dpi=200)

plt.figure(figsize=(9, 5))
plt.plot(angles, ranges, color='teal', label='С сопротивлением')
plt.plot(
    angles,
    [v0*v0*sin(2*radians(a))/g for a in angles],
    '--', color='purple', label='Вакуум'
)
plt.axvline(best, color='gray', linestyle=':',
            label=f'Оптимум: {best}°')
plt.xlabel('Угол броска, °')
plt.ylabel('Дальность, м')
plt.title('Дальность от угла броска — вариант 20')
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig('optimal_angle.png', dpi=200)
plt.show()