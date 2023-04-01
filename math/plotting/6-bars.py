#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

fruit_colors = ['red', 'yellow', '#ff8000', '#ffe5b4']
fruit_labels = ['apples', 'bananas', 'oranges', 'peaches']
person_labels = ['Farrah', 'Fred', 'Felicia']

fig, ax = plt.subplots()

for i in range(len(fruit_labels)):
    ax.bar(person_labels, fruit[i],
           bottom=np.sum(fruit[:i], axis=0),
           color=fruit_colors[i],
           label=fruit_labels[i],
           width=0.5)

ax.set_xlabel('Person')
ax.set_ylabel('Quantity of Fruit')
ax.set_title('Number of Fruit per Person')
ax.set_ylim([0, 80])
ax.set_yticks(range(0, 81, 10))
ax.legend()

plt.show()
