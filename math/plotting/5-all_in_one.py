#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec

# create a grid with 3 rows and 2 columns,
# where the last plot takes up two columns
gs = gridspec.GridSpec(3, 2, width_ratios=[1, 1], height_ratios=[1, 1, 2])
gs.update(wspace=0.4, hspace=0.4)  # set the spacing between subplots

# Graph 1
y0 = np.arange(0, 11) ** 3
plt.subplot(gs[0, 0])
plt.plot(y0, 'r-')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph 1', fontsize='x-small')

# Graph 2
mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180
plt.subplot(gs[0, 1])
plt.scatter(x1, y1, c='m', marker='.')
plt.xlabel('Height (in)', fontsize='x-small')
plt.ylabel('Weight (lbs)', fontsize='x-small')
plt.title("Men's Height vs Weight", fontsize='x-small')

# Graph 3
x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)
plt.subplot(gs[1, 0])
plt.semilogy(x2, y2)
plt.xlabel('Time (years)', fontsize='x-small')
plt.ylabel('Fraction Remaining', fontsize='x-small')
plt.title('Exponential Decay of C-14', fontsize='x-small')

# Graph 4
x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)
plt.subplot(gs[1, 1])
plt.plot(x3, y31, 'r--', label='C-14')
plt.plot(x3, y32, 'g-', label='Ra-226')
plt.xlabel('Time (years)', fontsize='x-small')
plt.ylabel('Fraction Remaining', fontsize='x-small')
plt.title('Exponential Decay of Radioactive Elements', fontsize='x-small')
plt.legend(loc='upper right', fontsize='x-small')

# Graph 5
np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)
plt.subplot(gs[2, :])  # span the last plot across two columns
plt.hist(student_grades, bins=range(0, 101, 10), edgecolor='black')
plt.xlabel('Grades', fontsize='x-small')
plt.ylabel('Number of Students', fontsize='x-small')
plt.title('Project A', fontsize='x-small')

# Figure title
plt.suptitle('All in One')
plt.show()
