# For image output to bmp file
import os

import numpy as np

# For math function curve rendering
import matplotlib.pyplot as plt

ouput_directory_path = './output_of_mAiLab005/'

name_of_x_axis = "X axis"
name_of_y_axis = "Y axis"



# common visual output setting of figure
def visual_ouput_setting( plt_handle, name_of_figure ):

        # name of x axis
    plt.xlabel( name_of_x_axis )

        # name of y axis
    plt.ylabel( name_of_y_axis )

        # name of figure
    plt.title( name_of_figure )

        # get axes of current figure
    ax = plt.gca() 

        # Hide right boundary line
    ax.spines['right'].set_color('none')

        # Hide top boundary line
    ax.spines['top'].set_color('none')


        # Set x axis on the bottom
    ax.xaxis.set_ticks_position('bottom')

        # Make x-axis aligned with y = 0
    ax.spines['bottom'].set_position( ('data', 0) )

        # Set y axis on the left
    ax.yaxis.set_ticks_position('left')

        # Make y-axis aligned with x = 0
    ax.spines['left'].set_position( ('data', 0) )

    return



# f(x) : activation function
# g(x) = f'(x)
# render y1 = f(x) and y2 = g(x) = f'(x)
def render_figure(x,y1,y2, func_name):

        # Set layout of figure as h x w (i.e., h = 1, w = 2)
        # Draw first figure on index 1 position (left hand side)
    plt.subplot(121)

    visual_ouput_setting( plt_handle = plt, name_of_figure = "activation function\n" + func_name )

        # render activation function, y1 = f(x)
    plt.plot(x, y1)


        # Set layout of figure as h x w (i.e., h = 1, w = 2)
        # Draw second figure on index 2 position (right hand side)
    plt.subplot(122)

    visual_ouput_setting( plt_handle = plt, name_of_figure = "derivative of activation function")

        # render derivative of activation function, y2 = g(x) = f'(x)
    plt.plot(x, y2)


        # Output and save figure to png file
        # Note: plt.savefig must be executed before plt.show() in order to save the current figure.
    plt.savefig( ouput_directory_path + str(func_name) + ".png" )

        # render figure on GUI windows
    plt.show(block=False)

        # keep each figure on screen for 3 seconds
    plt.pause(3)

        # auto close after 3 seconds
    plt.close()



# For invliad activation function exception handling
class ActFunctionTypeError(Exception):
    pass



# Activation function, y1 = f(x)
def functions(func_name,x):

    if 'Sigmoid' == func_name:
        return (1 / (1 + np.exp(-x)))

    elif 'tanh' == func_name:
        return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

    elif 'ReLU' == func_name:
        return np.where(x > 0, x, 0)

    elif 'Leaky ReLU' == func_name:    
        return np.where(x > 0.01 * x, x, 0.01 * x)

    elif 'ELU' == func_name: 
        alpha=0.09
        return np.where(x > 0, x, alpha * (np.exp(x) - 1))    

    else: 
        raise ActFunctionTypeError("Invalid activation function type.")


# Derivative of activation function, y2 = g(x) = f'(x)
def derivative_funs(func_name,x):
    
    if 'Sigmoid' == func_name:
        return (functions('Sigmoid',x) * (1 - functions('Sigmoid',x)))

    elif 'tanh' == func_name:
        return (1 - np.square(functions('tanh',x)))

    elif 'ReLU' == func_name:
        return np.where(x > 0, 1, 0)

    elif 'Leaky ReLU' == func_name:    
        return np.where(x > 0.01 * x, 1, 0.01)

    elif 'ELU' == func_name: 
        alpha=0.09
        return np.where(x > 0, 1, functions('ELU',x) + alpha)

    else: 
        raise ActFunctionTypeError("Invalid activation function type.")

# Entry point of program
def main():


    # Create output directory for edge image
    if not os.path.isdir(ouput_directory_path):
        os.mkdir(ouput_directory_path)


    # define the domain of x: 
    # -10 <= x <= 10
    # precision scale = 200
    x=np.linspace(-10, 10, 200)

    activation_functions=['Sigmoid','tanh','ReLU','Leaky ReLU','ELU']

   

###     1. Output each activation and corresponding derivative as following.
#
#           1-a. Sigmoid
#           1-b. tanh
#           1-c. ReLU
#           1-d. Leaky ReLU
#           1-e. ELU

    for act_func in activation_functions:

            # assign formula expression of specified activation_function
        y1 = functions(act_func, x)

            # assign formula expression of specified derivative of activation function
        y2 = derivative_funs(act_func, x)

            # render each activation function as well as its corresponding derivative
        render_figure(x, y1, y2, act_func)
  

if __name__=='__main__':
    main()    



'''

Example output:

Activation function and corresponding derivative is output and saved in sub-directory ./output_of_mAiLab005


./output_of_mAiLab005
    ELU.png
    Leaky ReLU.png
    ReLU.png
    Sigmoid.png
    tanh.png


'''