import numpy as np
import matplotlib.pyplot as plt

# Начальные параметры
x_init = 40       # Начальная численность жертв
y_init = 9        # Начальная численность хищников
alpha = 0.1       # Скорость размножения жертв
beta = 0.02       # Коэффициент взаимодействия
delta = 0.01      # Эффективность преобразования еды в потомство
gamma = 0.1       # Скорость смертности хищников
r_x = 5           # Пополнение популяции жертв
x_max = 100       # Максимальный размер популяции жертв
y_max = 50        # Максимальный размер популяции хищников
t_max = 200       # Время моделирования
dt = 0.1          # Шаг времени

# Функция для моделирования
def simulate_predator_prey(x_init, y_init, alpha, beta, delta, gamma, r_x, x_max, y_max, t_max, dt):
    t = np.arange(0, t_max, dt)
    x = np.zeros_like(t)
    y = np.zeros_like(t)
    x[0] = x_init
    y[0] = y_init

    for i in range(1, len(t)):
        dx = alpha * x[i-1] - beta * x[i-1] * y[i-1] + r_x
        dy = delta * x[i-1] * y[i-1] - gamma * y[i-1]

        # Обновление численностей с учётом максимального значения
        x[i] = min(x[i-1] + dx * dt, x_max)
        y[i] = min(y[i-1] + dy * dt, y_max)

        # Если численность падает ниже нуля, устанавливаем её в ноль
        if x[i] < 0: x[i] = 0
        if y[i] < 0: y[i] = 0

    return t, x, y

# Запуск симуляции
t, x, y = simulate_predator_prey(x_init, y_init, alpha, beta, delta, gamma, r_x, x_max, y_max, t_max, dt)

# Графики численностей жертв и хищников
plt.figure(figsize=(10, 6))
plt.plot(t, x, label='Prey Population (x)', color='green')
plt.plot(t, y, label='Predator Population (y)', color='red')
plt.xlabel('Time')
plt.ylabel('Population Size')
plt.legend()
plt.title('Volterra-Lotka Model')
plt.grid()
plt.show()

# Фазовая траектория
plt.figure(figsize=(8, 8))
plt.plot(x, y, color='purple')
plt.xlabel('Prey Population (x)')
plt.ylabel('Predator Population (y)')
plt.title('Phase Trajectory of Predator-Prey Dynamics')
plt.grid()
plt.show()
