import numpy as np

def generate_random_symbols(N):
    # Generate N random symbols (-1 or 1) with equal probability
    TR = np.random.choice([-1, 1], size=N)
    return TR

N = int(input("Enter the number of samples (N): "))
TR = generate_random_symbols(N)
print("Generated array TR:", TR)
