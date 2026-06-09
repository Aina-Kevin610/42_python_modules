#!/usr/bin/env python3
import matplotlib.pyplot as plt

xpoints = [10, 20, 30, 40, 50, 60]
ypoints = [1, 2, 5, 4, 2, 1]

plt.title("TEST", loc = 'left')
plt.xlabel("X axis")
plt.ylabel("Y axis")

# plt.grid(color = 'blue', linestyle = ':', linewidth = 1)
# plt.subplot(1, 3, 1)
# plt.plot(xpoints, ypoints, marker = 'o', linestyle = "dashed")

# plt.grid(color = 'green', linestyle = "solid", linewidth = 0.1)
# plt.subplot(1, 3, 2)
# plt.plot(xpoints, ypoints, marker = 'o', linestyle = "dashed")

# plt.grid(color = 'red', linestyle = '--', linewidth = 0.5)
# plt.subplot(1, 3, 3)
plt.bar(xpoints, ypoints, width=8)

plt.show()