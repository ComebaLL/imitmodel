import random  

def monte_carlo_sequence(trials):
    
    def generate_sequence():
        sequence = []  
        used_intervals = set()  
        for n in range(1, 1000):  
            interval_size = 1 / n
            x_n = random.uniform(0, 1)
            interval_index = int(x_n // interval_size)

            # Проверка на уникальность индекса интервала для подотрезков
            if interval_index in used_intervals:
                break
            
            used_intervals.add(interval_index)
            sequence.append(x_n)
        
        return sequence
    
    longest_sequence = []
    
    for _ in range(trials):
        sequence = generate_sequence()
        if len(sequence) > len(longest_sequence):
            longest_sequence = sequence
    
    return longest_sequence

longest_sequence = monte_carlo_sequence(10000)

print("Самая длинная последовательность:", longest_sequence)
print("Длина последовательности:", len(longest_sequence))
