import numpy as np
import matplotlib.pyplot as plt

# Time variable: 0 to 2π, with 1000 samples
x = np.linspace(0, 2 * np.pi, 1000)

# Sine and Cosine waves
y_sin = np.sin(x)
y_cos = np.cos(x)

# Create the plot
plt.figure(figsize=(10, 5))

# Plot sine wave
plt.plot(x, y_sin, label='Sine wave', color='blue')

# Plot cosine wave
plt.plot(x, y_cos, label='Cosine wave', color='orange', linestyle='--')

# Add title and subtitle
plt.title('Sine and Cosine Waves\nA Basic Visualization of Trigonometric Functions')

# Add axis labels
plt.xlabel('x (radians)')
plt.ylabel('Amplitude')

# Add grid, legend, and clean layout
plt.grid(True)
plt.legend()
plt.tight_layout()

# Show plot
plt.show()
