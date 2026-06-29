# import matplotlib.pyplot as plt
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]
# plt.plot(x, y)
# plt.xlabel("X values")
# plt.ylabel("Y values")
# plt.title("Simple Line Plot")
# plt.grid(True) # Adds a grid
# plt.show()

import numpy as np
x = np.arange(4)
y1 = [10, 15, 7, 12]
y2 = [8, 14, 9, 10]
width = 0.35
plt.bar(x - width/2, y1, width, label='Group 1')
plt.bar(x + width/2, y2, width, label='Group 2')
plt.xticks(x, ['A', 'B', 'C', 'D'])
plt.xlabel("Categories")
plt.ylabel("Values")
plt.legend()
plt.show()