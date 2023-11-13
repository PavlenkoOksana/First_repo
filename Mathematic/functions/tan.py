import matplotlib.pyplot as plt
import numpy as np

# .linspace arguments are (start, end, number_of_steps)
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = np.tan(x)

# This operation inserts a NaN where the difference between successive points is negative
# NaN means "Not a Number" and NaNs are not plotted or connected
# I found this by doing a search for "How to plot tan(x) in matplotlib without the connecting lines between asymtotes"
y[:-1][np.diff(y) < 0] = np.nan

# show grid
plt.grid()

plt.xlabel("x")
plt.ylabel("$tan(x)$")

# Set the x and y axis cutoffs
plt.ylim(-10,10)
plt.xlim(-2 * np.pi, 2 * np.pi)

# x_labels in radians
# For a more programmatic approach to radians, see https://matplotlib.org/3.1.1/gallery/units/radian_demo.html
radian_multiples = [-2, -3/2, -1, -1/2, 0, 1/2, 1, 3/2, 2]
radians = [n * np.pi for n in radian_multiples]
radian_labels = ['$-2\pi$', '$-3\pi/2$', '$\pi$', '$-\pi/2$', '0', '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$']

plt.xticks(radians, radian_labels)

plt.title("$y = tan(x)$", fontsize=14)
plt.plot(x, y)
plt.show()