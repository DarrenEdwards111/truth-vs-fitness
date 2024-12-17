import numpy as np
import matplotlib.pyplot as plt

# Define the size of the perceptual space (X) from 4 to 100 for visualization
size_perceptual_space = np.arange(4, 101)

# Calculate the probability that Fitness-only strategy strictly dominates Truth strategy based on the FBT Theorem
probability_dominance = (size_perceptual_space - 3) / (size_perceptual_space - 1)

# Create a bar graph with two colors
plt.figure(figsize=(10, 6))
plt.bar(size_perceptual_space - 0.2, probability_dominance, width=0.4, color='royalblue', alpha=0.7, label='Fitness-Only')
plt.bar(size_perceptual_space + 0.2, 1 - probability_dominance, width=0.4, color='gold', alpha=0.7, label='Truth')  # 1 - probability_dominance for Truth strategy

plt.xlabel('Size of Perceptual Space (|X|)')
plt.ylabel('Probability')
plt.title('FBT Theorem: Probability of Fitness-only vs Truth Dominance')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.xticks(size_perceptual_space[::10])  # Show labels for every 10th value on the x-axis
plt.yticks(np.arange(0, 1.1, 0.1))  # Set increments of 0.1 on the y-axis

# Adjust x-axis limits to avoid data points being cut off by bars
plt.xlim(min(size_perceptual_space) - 0.5, max(size_perceptual_space) + 0.5)

plt.tight_layout()
plt.show()