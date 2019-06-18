# For image operation
from library.image_tool_box import print_image_array
from library.image_tool_box import get_MNIST_image_header
from library.image_tool_box import read_one_MNIST_image
from library.image_tool_box import gen_average_image


fileName = 'data_of_mAiLab003/train-images.idx3-ubyte'
# fileName = 'data_of_mAiLab003/test_file_io.hex'


with open(fileName, 'rb') as f:
    # Read header of train image file

    header_return = get_MNIST_image_header(f)

    if -1 == header_return:
        # Handle End-of-File, or exception
        pass

    else:
        (img_height, img_width) = header_return

        image_container = []

        for index in range(10):

            image_return = read_one_MNIST_image(f, img_height, img_width)

            if -2 == image_return:
                # Handle exception
                print("Error occurs in index {:0>2d}".format( index ) )
                break

            else:
                image_matrix = image_return

                # Push image_matrix into container
                image_container.append(image_matrix)

        print("len of container", len(image_container) )
        average_image_of_first_ten = gen_average_image( image_container )


# print_first image
print_image_array( image_container[0] )

# print average image of first ten
print_image_array( average_image_of_first_ten )










