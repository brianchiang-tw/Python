import matplotlib.pyplot as plt
import numpy as np

x = np.linspace( -5, 5, 100 )
y1 = 3*x + 2
y2 = x ** 2 


# Create a figure panel
plt.figure()
plt.plot(x, y1)
plt.show()


plt.figure()
plt.plot(x, y2)
plt.plot(x, y1, color='green', linewidth=1.0, linestyle='--')
plt.show()