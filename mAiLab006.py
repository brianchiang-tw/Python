# For image output to bmp file
import os

# For image operation
from library.image_tool_box import * 

# For math/statistic operation
from library.math_tool_box import StatMaker
import math


###     Prelude: Downlaod and unpack those 4 test data from MNIST database.

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
ouput_directory_path = './output_of_mAiLab006/'
path_of_MNIST_image = data_directory_path + file_name_of_MNIST_image
path_of_MNIST_label = data_directory_path + file_name_of_MNIST_label





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
        max_pooling_img_container = []
        avg_pooling_img_container = []

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

                    # max pooling, with step_size = 2
                max_pooling_img = array_pooling(image_matrix, step_size=2, pooling_mode="Max")
                max_pooling_img_container.append( max_pooling_img )

                print("Max pooling image of input_#{:2d}".format( index+1 ) )
                print_image_array( max_pooling_img )


                    # average pooling, with step_size = 2
                avg_pooling_img = array_pooling(image_matrix, step_size=2, pooling_mode="Average")
                avg_pooling_img_container.append( avg_pooling_img )

                print("Average pooling image of input_#{:2d}".format( index+1 ) )
                print_image_array( avg_pooling_img )




                