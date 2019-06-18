# For image operation
from library.image_tool_box import get_MNIST_image_header
from library.image_tool_box import get_MNIST_label_header

from library.image_tool_box import read_one_MNIST_image
from library.image_tool_box import print_image_array
from library.image_tool_box import print_image_array_with_padding
from library.image_tool_box import gen_average_image

# For statistic operation
from library.math_tool_box import StatMaker

file_name_of_MNIST_image = 'train-images.idx3-ubyte'
file_name_of_MNIST_label = 'train-labels.idx1-ubyte'
data_directory_path = 'data_of_mAiLab003/'
path_of_MNIST_image = data_directory_path + file_name_of_MNIST_image
path_of_MNIST_label = data_directory_path + file_name_of_MNIST_label

# file_name_of_test_io = 'test_file_io.hex'
# a tiny 16 bytes file to test file I/O
# Its content is as following
#            Hexadicaml content                      ASCII content
# 48 65 6C 6C 6F 20 20 20 57 6F 72 6C 64 20 20 20    Hello...World...



with open(path_of_MNIST_image, 'rb') as file_handle:

    # Read header of MNIST image file
    header_return = get_MNIST_image_header(file_handle)

    if -1 == header_return:
        # Handle End-of-File, or exception
        pass

    else:
        (img_height, img_width) = header_return

        image_container = []

        for index in range(10):

            image_return = read_one_MNIST_image(file_handle, img_height, img_width)

            if -2 == image_return:
                # Handle exception
                print("Error occurs in index {:0>2d}".format( index ) )
                break

            else:
                image_matrix = image_return

                # Push image_matrix into container
                image_container.append(image_matrix)

        
        average_image_of_first_ten = gen_average_image( image_container )


# print_first image
print("First image array:")
print_image_array( image_container[0] )

# print average image of first ten
print("Average image array of first ten:")
print_image_array( average_image_of_first_ten )



with open(path_of_MNIST_label, 'rb') as file_handle:

    # Read header of MNIST label file
    header_return = get_MNIST_label_header(file_handle)

    if -1 == header_return:
        # Handle End-of-File, or exception
        pass

    else:
        number_of_items  = header_return

        # Read first 10 labels, then save them into label_series
        label_series = list( file_handle.read(10) )
        label_stat = StatMaker( label_series )
        print("The average value of first ten labels in '{:<20}' is {:+02.2f}".format( str(file_name_of_MNIST_label), label_stat.get_avg() ) )



# print_first image, with zero padding over boundary area
new_side_length = 32
original_side_length = img_width
padding_size = (new_side_length - original_side_length)//2

print_image_array_with_padding( image_container[0], padding_size )