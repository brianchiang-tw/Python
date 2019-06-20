import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace( -3, 3, 50 )
y1 = 2*x + 1
y2 = x ** 2


plt.figure()
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

# render range of x direction
plt.xlim( (-1, 2) )

# render range of y direction
plt.ylim( (-2, 3) )


# define new linspace for x

new_ticks = np.linspace(-1, 2, 5)
plt.xticks( new_ticks )
plt.yticks([-2, -1.8, -1, 1.22, 3],['$too\ bad$', '$bad$', '$nomral$', '$good$', '$very\ good$'])



# Get coordinate axis information
ax = plt.gca()

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# plt.show()



# Set x axis
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position( ('data', 0) )
# plt.show()



# Set y axis
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position( ('data', 0) )
plt.show()
