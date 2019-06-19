import scipy.signal

from library.image_tool_box import extend_image_array_with_padding
from library.image_tool_box import img_conv_kernel
from library.image_tool_box import print_image_array

image = [[1, 2, 3, 4, 5, 6, 7],
         [8, 9, 10, 11, 12, 13, 14],
         [15, 16, 17, 18, 19, 20, 21],
         [22, 23, 24, 25, 26, 27, 28],
         [29, 30, 31, 32, 33, 34, 35],
         [36, 37, 38, 39, 40, 41, 42],
         [43, 44, 45, 46, 47, 48, 49]]


filter_kernel_1 = [[-1, 1, -1],
                 [-2, 3, 1],
                 [2, -6, 0]]


filter_kernel_2 = [[ 0, -6, 2],
                [1, 3, -2],
                [-1, 1, -1]]




print( filter_kernel_2[0][0] )
print( filter_kernel_2[0][1] )
print( filter_kernel_2[0][2] )



extended_image = extend_image_array_with_padding(image, 1, 0x00)
print_image_array( image )

print_image_array( extended_image )



img_conv_ker = img_conv_kernel(image, filter_kernel_1)

print_image_array( img_conv_ker )



print( "SciPy's 2D convolution demo")



output_1 = scipy.signal.convolve2d(image, filter_kernel_1, mode='same', boundary='fill', fillvalue=0)

# output_2 = scipy.signal.convolve2d(image, filter_kernel_2, mode='same', boundary='fill', fillvalue=0)

print( output_1 )
# print( output_2 )
