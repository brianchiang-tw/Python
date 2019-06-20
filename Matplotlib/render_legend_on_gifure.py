import matplotlib.pyplot as plt 
import numpy as np 



x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x ** 2



# Create a figure
plt.figure()

plt.xlim( (-1, 2) )
plt.ylim( (-2, 3) )



# Set new sticks
new_sticks = np.linspace(-1, 2, 5)
plt.xticks( new_sticks )

# Set tick labels
plt.yticks( [-2, -1.8, -1, 1.22, 3], 
            [ r'$too\ bad$', r'$bad$', r'$normal$', r'$good$', r'$very good$'] )


# Set line style
line_1 = plt.plot(x, y1, label='linear line')
line_2 = plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--', label='square line')



# Set legend render mode
plt.legend(loc='upper right')


# render figure
plt.show()
