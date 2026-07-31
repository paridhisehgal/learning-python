import numpy as np
import matplotlib.pyplot as plt

threshold = 0.5
steepness = 6
x = np.linspace(-1, 2, 500)
y = 1 / (1 + np.exp(-steepness * (x - threshold)))

plt.figure(figsize=(8, 5))
plt.plot(x, y, linewidth=2, label=rf"Sigmoid (threshold = {threshold})")
plt.axhline(0, color="gray", linewidth=0.5)
plt.axhline(1, color="gray", linewidth=0.5)
plt.axvline(threshold, color="red", linestyle="--", alpha=0.7, label=f"x = {threshold}")

plt.ylim(-0.1, 1.1)
plt.xlim(-1, 2)
plt.title("Smooth 0 to 1 Threshold (Sigmoid)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()
