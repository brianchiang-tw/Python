# For image output to bmp file
import os

# For image operation
from library.image_tool_box import * 

# For math/statistic operation
from library.math_tool_box import StatMaker
import math


###     1. Downlaod and unpack those 4 test data from MNIST database.

# train-images-idx3-ubyte.gz: training set images (9912422 bytes)
# train-labels-idx1-ubyte.gz: training set labels (28881 bytes)
# t10k-images-idx3-ubyte.gz: test set images (1648877 bytes)
# t10k-labels-idx1-ubyte.gz: test set labels (4542 bytes) 

# MNIST database
# http://yann.lecun.com/exdb/mnist/

# This is is completed, and they're saved in sub-directory "./data_of_mAiLab003"

file_name_of_MNIST_image = 'train-images.idx3-ubyte'
file_name_of_MNIST_label = 'train-labels.idx1-ubyte'
data_directory_path = 'data_of_mAiLab003/'
ouput_directory_path = './output_of_mAiLab004/'
path_of_MNIST_image = data_directory_path + file_name_of_MNIST_image
path_of_MNIST_label = data_directory_path + file_name_of_MNIST_label


kernel_Gx = [[-1, 0, +1],
            [-2, 0, +2],
            [-1, 0, +1]
            ]

kernel_Gy = [[+1, +2, +1],
            [0, 0, 0],
            [-1, -2, -1]
            ]


kernel_Gx_5 = [ [ -5,  -4, 0,  +4,  +5],
                [ -8, -10, 0, +10,  +8],
                [-10, -20, 0, +20, +10],
                [ -8, -10, 0, +10,  +8],
                [ -5,  -4, 0,  +4,  +5],                                                
                ]

kernel_Gy_5 = array_transpose( kernel_Gx_5 )



kernel_Gx_7 = [ [ -5,  -4, 0,  +4,  +5],
                [ -8, -10, 0, +10,  +8],
                [-10, -20, 0, +20, +10],
                [ -8, -10, 0, +10,  +8],
                [ -5,  -4, 0,  +4,  +5],                                                
                ]


# Create output directory for edge image
if not os.path.isdir(ouput_directory_path):
    os.mkdir(ouput_directory_path)


with open(path_of_MNIST_image, 'rb') as file_handle:

    # Read header of MNIST image file
    header_return = get_MNIST_image_header(file_handle)

    if -1 == header_return:
        # Handle End-of-File, or exception
        pass

    else:
        (img_height, img_width) = header_return

        image_container = []
        grad_magnitude_container = []
        edge_img_container = []

        for index in range(5):

            image_return = read_one_MNIST_image(file_handle, img_height, img_width)

            if -2 == image_return:
                # Handle exception
                print("Error occurs in index {:0>2d}".format( index ) )
                break

            else:
                image_matrix = image_return

                    # Push origianl source image into image container
                image_container.append(image_matrix)



                    # Convolve image_matrix with kernel Gx
                Gx_conv_image = img_conv_kernel( image_matrix, kernel_Gx )

                    # Convolve image_matrix with kernel Gy
                Gy_conv_image = img_conv_kernel( image_matrix, kernel_Gy )
        
                    # Compute gradient magnitude from Gx_conv_image and Gy_conv_image
                gradient_magnitude_image = get_Sobel_gradient_magnitude(Gx_conv_image, Gy_conv_image)



                    # Push Gx image, Gy image, and gradient magnitude image into its container
                grad_magnitude_container.append( (Gx_conv_image, Gy_conv_image, gradient_magnitude_image ) )

                    # Compute edge image from gradient magnitude
                edge_image = get_edge_image( gradient_magnitude_image, threshold_factor=0.7 )

                    # Push edge image into its container
                edge_img_container.append( edge_image )



###     2. Output Gx, Gy convolution image for first 5 input image, with extended image size 30 x 30 and zero padding.

for index in range(5):

    serial_number = index+1

        # Source image
    # print("Original source image array_#{}:".format(serial_number) )
    # print_image_array( image_container[index] )


        # Gx edge image
    gx = grad_magnitude_container[index][0]
    gx_abs_image = absolute_value_tranform_of_partial_differential_img( gx )
    gx_edge = get_edge_image( gx_abs_image, 0.1 )

    save_to_bmp(gx_edge, ouput_directory_path+"image_"+ str(serial_number)+"_Gx_edge")


        # Gy edge image
    gy = grad_magnitude_container[index][1]
    gy_abs_image = absolute_value_tranform_of_partial_differential_img( gy )
    gy_edge = get_edge_image( gy_abs_image, 0.1 )

    save_to_bmp(gy_edge, ouput_directory_path+"image_"+ str(serial_number)+"_Gy_edge")

        # Edge image
    edge_image = edge_img_container[index]

    # print("Edge image_#{}:".format(serial_number) )
    # print_image_array( edge_image, "Decimal" )

    save_to_bmp(edge_image, ouput_directory_path+"image_"+str(serial_number)+"_edge")



    # Convolve image_matrix with kernel Gx_5x5
Gx_conv_image = img_conv_kernel( image_container[0], kernel_Gx_5 )
# print(" 5x5 Gx convolution image of image_#1")
# print_image_array( Gx_conv_image, "Decimal" )

    # Convolve image_matrix with kernel Gy_7x7
Gy_conv_image = img_conv_kernel( image_container[0], kernel_Gy_5 )
# print(" 5x5 Gy convolution image of image_#1")
# print_image_array( Gy_conv_image, "Decimal" )








'''

Example output:

###     1. Downlaod and unpack those 4 test data from MNIST database.

# This is is completed, and they're saved in sub-directory "./data_of_mAiLab003"



###     2. Output first image from test file, "train-images.idx3-ubyte", with image size 28 x 28.

First image array:
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 03 12 12 12 7E 88 AF 1A A6 FF F7 7F 00 00 00 00
00 00 00 00 00 00 00 00 1E 24 5E 9A AA FD FD FD FD FD E1 AC FD F2 C3 40 00 00 00 00
00 00 00 00 00 00 00 31 EE FD FD FD FD FD FD FD FD FB 5D 52 52 38 27 00 00 00 00 00
00 00 00 00 00 00 00 12 DB FD FD FD FD FD C6 B6 F7 F1 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 50 9C 6B FD FD CD 0B 00 2B 9A 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 0E 01 9A FD 5A 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 8B FD BE 02 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 0B BE FD 46 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 23 F1 E1 A0 6C 01 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 51 F0 FD FD 77 19 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 2D BA FD FD 96 1B 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 10 5D FC FD BB 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 F9 FD F9 40 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 2E 82 B7 FD FD CF 02 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 27 94 E5 FD FD FD FA B6 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 18 72 DD FD FD FD FD C9 4E 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 17 42 D5 FD FD FD FD C6 51 02 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 12 AB DB FD FD FD FD C3 50 09 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 37 AC E2 FD FD FD FD F4 85 0B 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 88 FD FD FD D4 87 84 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00



###     3. Output the average image (with rounding down to nearest integer) of the first ten from test file 
#          , "train-images.idx3-ubyte", with image size 28 x 28.


Average image array of first ten:
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 0E 19 15 08 0F 19 0F 05 00 00 12 13 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 07 1C 2B 4D 3B 41 4A 5C 4D 42 45 35 1C 00 00 00 00
00 00 00 00 06 08 00 00 03 07 17 26 3B 6D 88 6A 64 6D 78 6B 6B 59 31 0F 00 00 00 00
00 00 00 00 0C 10 00 04 17 2B 32 37 5D A2 AC 8A 7B 73 65 79 80 5F 20 00 00 00 00 00
00 00 00 00 16 10 00 01 15 25 41 65 95 B7 A1 6D 5E 78 6E 7F 7D 50 0A 00 00 00 00 00
00 00 00 00 16 10 00 00 08 1A 31 68 95 A6 68 26 38 56 66 84 77 36 00 00 00 00 00 00
00 00 00 04 18 10 00 00 00 21 4A 5B 7D 78 3D 3B 39 44 62 74 6D 35 05 00 00 00 00 00
00 00 00 0C 19 10 00 00 11 2C 3F 46 4C 61 36 40 42 4E 65 6A 65 1E 10 00 00 00 00 00
00 00 00 0F 19 0C 00 0D 2B 31 2C 20 2D 50 58 5D 55 5E 68 62 49 1B 13 00 00 00 00 00
00 00 00 0F 19 06 01 1C 32 32 28 2C 25 6F 9B 90 7A 6A 64 41 25 19 13 00 00 00 00 00
00 00 00 0F 19 08 02 2D 40 4A 3A 4F 69 B1 C8 BC 9D 71 52 1C 1D 19 13 00 00 00 00 00
00 00 00 0F 19 17 1D 4D 65 72 7B 7D 95 B8 B3 BE 89 63 56 2E 19 19 0E 00 00 00 00 00
00 00 00 00 0B 11 22 4A 60 60 4B 39 3A 5D 7E 82 69 6E 7C 5A 22 13 01 00 00 00 00 00
00 00 00 00 00 00 1C 3C 39 19 16 17 1D 56 8A 7D 5A 6E 7A 60 36 19 06 04 04 00 00 00
00 00 00 00 00 00 21 35 26 0A 19 19 24 5D 84 76 49 66 67 3A 10 18 19 19 16 00 00 00
00 00 00 00 00 0A 22 39 20 01 20 2B 44 55 81 7D 73 6B 5B 1F 00 08 12 12 03 00 00 00
00 00 00 00 00 1D 34 4A 30 34 39 4C 6A 5A 79 95 65 68 42 0F 00 00 00 00 00 00 00 00
00 00 00 00 00 29 3A 4B 48 5D 67 76 6A 5F 85 8B 49 3D 25 09 00 00 00 00 00 00 00 00
00 00 00 00 00 16 27 4C 5A 67 7B 7A 5B 48 5F 63 32 2B 1C 0F 00 00 00 00 00 00 00 00
00 00 00 00 05 16 26 35 45 64 71 7A 39 19 3E 4B 22 2A 1D 0F 00 00 00 00 00 00 00 00
00 00 00 00 0D 19 1A 23 2F 3A 37 21 02 00 1A 2E 16 0D 19 0F 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 12 19 11 01 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 0E 19 04 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00



###     4. Output the average label value (with rounding down to hundredths) of the first ten from test file
#          , "train-labels.idx1-ubyte".

The average value of first ten labels in 'train-labels.idx1-ubyte' is +3.00



###     5. Extend and output first image to 32x32 from test file, with zero padding on boundary area.

First image array extneds to 32x32 with zero padding over boundary:
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 03 12 12 12 7E 88 AF 1A A6 FF F7 7F 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 1E 24 5E 9A AA FD FD FD FD FD E1 AC FD F2 C3 40 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 31 EE FD FD FD FD FD FD FD FD FB 5D 52 52 38 27 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 12 DB FD FD FD FD FD C6 B6 F7 F1 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 50 9C 6B FD FD CD 0B 00 2B 9A 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 0E 01 9A FD 5A 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 8B FD BE 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 0B BE FD 46 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 23 F1 E1 A0 6C 01 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 51 F0 FD FD 77 19 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 2D BA FD FD 96 1B 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 10 5D FC FD BB 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 F9 FD F9 40 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 2E 82 B7 FD FD CF 02 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 27 94 E5 FD FD FD FA B6 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 18 72 DD FD FD FD FD C9 4E 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 17 42 D5 FD FD FD FD C6 51 02 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 12 AB DB FD FD FD FD C3 50 09 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 37 AC E2 FD FD FD FD F4 85 0B 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 88 FD FD FD D4 87 84 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00



###     6. Output and save first image as BitMap(.bmp) file.

First image is saved into 'first_image.bmp'.

'''