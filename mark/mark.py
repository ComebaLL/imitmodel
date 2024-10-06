import numpy as np
import matplotlib.pyplot as plt

# Определение матрицы переходов
transition_matrix = np.array([
    [0, 0.5, 0.3, 0.2, 0],   # Пропал без вести
    [0, 1.0, 0, 0, 0],       # Зарезали в Москве (поглощающее состояние)
    [0, 0, 0.5, 0.5, 0],     # Улетел на Кубу
    [0, 0, 0, 0, 1.0],       # Нелегально пробрался в США
    [0, 0, 0, 0, 1.0]        # В плену в наркокартеле (поглощающее состояние)
])

class MarkovChainSimulator:
    def __init__(self, transition_matrix):
        self.transition_matrix = transition_matrix
        self.num_states = transition_matrix.shape[0]

    def step(self, current_state):
        """Выполняет один шаг симуляции Марковской цепи."""
        new_state = np.random.choice(self.num_states, p=self.transition_matrix[current_state])
        return new_state

    def simulate(self, start_state, num_simulations=10000):
        """Запускает симуляцию цепи Маркова."""
        times_to_absorption = []
        absorbing_states = []

        for _ in range(num_simulations):
            current_state = start_state
            time_steps = 0

            while current_state not in [1, 4]:  # Поглощающие состояния
                current_state = self.step(current_state)
                time_steps += 1

            times_to_absorption.append(time_steps)
            absorbing_states.append(current_state)

        return times_to_absorption, absorbing_states

# Функция для запуска симуляции и визуализации результатов
def run_and_visualize(start_state, transition_matrix):
    simulator = MarkovChainSimulator(transition_matrix)
    
    times, absorbing_states = simulator.simulate(start_state)

    # Вычисляем среднее время до поглощения
    average_time = np.mean(times)
    print(f"Среднее время до поглощения (начальное состояние {start_state}): {average_time:.2f} шага")
    
    # Вероятности достижения каждого поглощающего состояния
    prob_to_state_1 = absorbing_states.count(1) / len(absorbing_states)
    prob_to_state_4 = absorbing_states.count(4) / len(absorbing_states)
    print(f"Вероятность достичь состояния 'Зарезали в Москве': {prob_to_state_1:.2f}")
    print(f"Вероятность достичь состояния 'В плену в наркокартеле': {prob_to_state_4:.2f}")

    # Построение гистограммы времени до поглощения
    plt.hist(times, bins=30, color='skyblue', edgecolor='black')
    plt.title(f"Гистограмма времени до поглощения (начальное состояние {start_state})")
    plt.xlabel("Число шагов до поглощения")
    plt.ylabel("Частота")
    plt.show()

# Запуск симуляции для начальных состояний "Пропал без вести" и "Улетел на Кубу"
run_and_visualize(0, transition_matrix)
run_and_visualize(2, transition_matrix)


