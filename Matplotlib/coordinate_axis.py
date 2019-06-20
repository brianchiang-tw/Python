import matplotlib.pyplot as plt
import numpy as np

x = np.linspace( -50, 50, 100 )

y1 = x + 3
y2 = x ** 2

plt.figure()

plt.plot(x, y2)
# plt.plot(x, y1, color='green', linewidth=1.0,linestyle='--')
plt.plot(x, y1)

# x range
plt.xlim( (-50,50) )

# y range
plt.ylim( (-50,50) )

plt.xlabel("X axis")
plt.ylabel("Y axis")


plt.yticks([-40, -20, 0, 20, 40],[r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])


plt.show()