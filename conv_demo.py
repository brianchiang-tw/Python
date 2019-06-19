import scipy.signal

from library.image_tool_box import extend_image_array_with_padding
from library.image_tool_box import img_conv_kernel
from library.image_tool_box import print_image_array

image = [[1 , 2 , 3 , 4 , 5 , 6 , 7 ],
         [8 , 9 , 10, 11, 12, 13, 14],
         [15, 16, 17, 18, 19, 20, 21],
         [22, 23, 24, 25, 26, 27, 28],
         [29, 30, 31, 32, 33, 34, 35],
         [36, 37, 38, 39, 40, 41, 42],
         [43, 44, 45, 46, 47, 48, 49]]


filter_kernel_1 = [ [-1, 1, -1],
                    [-2, 3, 1],
                    [2, -6, 0]]



#
print( "Self-made 2D convolution demo:")

img_conv_ker = img_conv_kernel(image, filter_kernel_1)
print_image_array( img_conv_ker , "Decimal")


#
print( "SciPy's 2D convolution demo:")


output_1 = scipy.signal.convolve2d(image, filter_kernel_1, mode='same', boundary='fill', fillvalue=0)
print( output_1 )

'''

Example output:

Self-made 2D convolution demo:
        -2         -8         -7         -6         -5         -4         28
         3         -7        -10        -13        -16        -19         14
       -18        -28        -31        -34        -37        -40          0
       -39        -49        -52        -55        -58        -61        -14
       -60        -70        -73        -76        -79        -82        -28
       -81        -91        -94        -97       -100       -103        -42
      -101        -61        -63        -65        -67        -69        -57


SciPy's 2D convolution demo:
[[  -2   -8   -7   -6   -5   -4   28]
 [   3   -7  -10  -13  -16  -19   14]
 [ -18  -28  -31  -34  -37  -40    0]
 [ -39  -49  -52  -55  -58  -61  -14]
 [ -60  -70  -73  -76  -79  -82  -28]
 [ -81  -91  -94  -97 -100 -103  -42]
 [-101  -61  -63  -65  -67  -69  -57]]

'''