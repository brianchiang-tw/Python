import matplotlib.pyplot as plt
import numpy as np

x = np.linspace( -5, 5, 100)

y = 3 * x + 2

plt.figure()
plt.plot(x, y)
plt.show()