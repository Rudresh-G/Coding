import random
import numpy as np
import matplotlib.pyplot as plt

stages = 100
samples = 10000
distribution = np.zeros((stages + 1,), dtype=int)
init_block = stages/2


def flick():
    return random.choice([-0.5, 0.5])


i = 0
while i < samples:
    j = 0
    pos = init_block
    while j < stages:
        pos += flick()
        j += 1
    pos = int(pos)
    distribution[pos] += 1
    i += 1
print(distribution)


labels = np.arange(1, stages+2, 1)
fig, ax = plt.subplots()

ax.plot(labels, distribution)
ax.set(xlabel='containers', ylabel='samples', title='Galton Board')
plt.show()
