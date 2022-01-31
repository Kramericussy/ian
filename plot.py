import numpy as np
import matplotlib.pyplot as plt

x = np.array(range(10))
y = x**2

for i in range(5): 
    y *= 2

plt.plot(x,y)
plt.show()