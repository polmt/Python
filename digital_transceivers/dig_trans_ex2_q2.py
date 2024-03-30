import numpy as np

# Number of samples
N = 1000

# Variance values
variance1 = 2
variance2 = 4

# Generate complex Gaussian process with variance 2
real_part1 = np.random.randn(N) * np.sqrt(variance1)
imaginary_part1 = np.random.randn(N) * np.sqrt(variance1)
complex_process1 = real_part1 + 1j * imaginary_part1

# Calculate the variance of the generated process with variance 2
calculated_variance1 = np.var(complex_process1)

# Generate complex Gaussian process with variance 4
real_part2 = np.random.randn(N) * np.sqrt(variance2)
imaginary_part2 = np.random.randn(N) * np.sqrt(variance2)
complex_process2 = real_part2 + 1j * imaginary_part2

# Calculate the variance of the generated process with variance 4
calculated_variance2 = np.var(complex_process2)

# Display the calculated variances
print(f'Variance of the process with variance 2: {calculated_variance1:.4f}')
print(f'Variance of the process with variance 4: {calculated_variance2:.4f}')
