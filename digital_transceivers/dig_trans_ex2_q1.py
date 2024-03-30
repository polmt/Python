import numpy as np
import matplotlib.pyplot as plt

# Number of samples
N = [10, 100, 1000]

# Initialize arrays to store results
means_rand = np.zeros(len(N))
vars_rand = np.zeros(len(N))
means_randn = np.zeros(len(N))
vars_randn = np.zeros(len(N))

# Generate random samples and calculate mean and variance
for i in range(len(N)):
    samples_rand = np.random.rand(N[i])
    samples_randn = np.random.randn(N[i])

    # Calculate mean and variance for rand samples
    means_rand[i] = np.mean(samples_rand)
    vars_rand[i] = np.var(samples_rand)

    # Calculate mean and variance for randn samples
    means_randn[i] = np.mean(samples_randn)
    vars_randn[i] = np.var(samples_randn)

# Theoretical mean and variance for rand samples
theoretical_mean_rand = 0.5  # The mean of rand samples is 0.5
theoretical_var_rand = 1 / 12  # The variance of rand samples is 1/12

# Theoretical mean and variance for randn samples
theoretical_mean_randn = 0  # The mean of randn samples is 0
theoretical_var_randn = 1  # The variance of randn samples is 1

# Calculate the differences between practical and theoretical values
mean_diff_rand = np.abs(means_rand - theoretical_mean_rand)
var_diff_rand = np.abs(vars_rand - theoretical_var_rand)
mean_diff_randn = np.abs(means_randn - theoretical_mean_randn)
var_diff_randn = np.abs(vars_randn - theoretical_var_randn)

# Plot the differences
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(N, mean_diff_rand, '-o')
plt.title('Mean Difference for rand Samples')
plt.xlabel('Sample Size (N)')
plt.ylabel('Absolute Difference')

plt.subplot(2, 2, 2)
plt.plot(N, var_diff_rand, '-o')
plt.title('Variance Difference for rand Samples')
plt.xlabel('Sample Size (N)')
plt.ylabel('Absolute Difference')

plt.subplot(2, 2, 3)
plt.plot(N, mean_diff_randn, '-o')
plt.title('Mean Difference for randn Samples')
plt.xlabel('Sample Size (N)')
plt.ylabel('Absolute Difference')

plt.subplot(2, 2, 4)
plt.plot(N, var_diff_randn, '-o')
plt.title('Variance Difference for randn Samples')
plt.xlabel('Sample Size (N)')
plt.ylabel('Absolute Difference')

plt.tight_layout()
plt.show()

# Display the results
print('Means and variances for rand samples:')
for i in range(len(N)):
    print(f'N = {N[i]}: Mean = {means_rand[i]:.4f}, Variance = {vars_rand[i]:.4f}')

print('Means and variances for randn samples:')
for i in range(len(N)):
    print(f'N = {N[i]}: Mean = {means_randn[i]:.4f}, Variance = {vars_randn[i]:.4f}')
