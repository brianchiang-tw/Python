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
                serial_number = index + 1

                image_matrix = image_return

                    # Push origianl source image into image container
                image_container.append(image_matrix)


###     1. Conduct and output pooling image, with 'Max' as well as 'Average' operator, on first 5 input source images.


                    # max pooling, with step_size = 2
                max_pooling_img = array_pooling(image_matrix, step_size=2, pooling_mode="Max")
                max_pooling_img_container.append( max_pooling_img )

                    # print to console
                print("\n Max pooling image of input_#{:2d}".format( serial_number ) )
                print_image_array( max_pooling_img )

                    # output and saved as BitMap file
                save_to_bmp(max_pooling_img, ouput_directory_path+"image_"+str(serial_number)+"_max_pooling")



                    # average pooling, with step_size = 2
                avg_pooling_img = array_pooling(image_matrix, step_size=2, pooling_mode="Average")
                avg_pooling_img_container.append( avg_pooling_img )

                    # print to console
                print("\n Average pooling image of input_#{:2d}".format( serial_number ) )
                print_image_array( avg_pooling_img )

                    # output and saved as BitMap file
                save_to_bmp(avg_pooling_img, ouput_directory_path+"image_"+str(serial_number)+"_average_pooling")



'''

Example output:



###     1. Conduct and output pooling image, with 'Max' as well as 'Average' operator, on first 5 input source images.


 Max pooling image of input_# 1
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 12 12 88 AF FF F7 00 00
00 00 00 31 FD FD FD FD FD E1 FD C3 00 00
00 00 00 12 FD FD FD C6 F7 00 00 00 00 00
00 00 00 00 0E 9A FD 02 00 00 00 00 00 00
00 00 00 00 00 0B FD E1 6C 00 00 00 00 00
00 00 00 00 00 00 51 FD FD 96 00 00 00 00
00 00 00 00 00 00 00 10 FC FD 40 00 00 00
00 00 00 00 00 00 94 FD FD FD 02 00 00 00
00 00 00 00 42 FD FD FD FD 4E 00 00 00 00
00 00 AC FD FD FD FD 50 00 00 00 00 00 00
00 00 FD FD D4 84 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00


Image is saved into './output_of_mAiLab006/image_1_max_pooling.bmp'.

 Average pooling image of input_# 1
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 05 09 41 32 69 5D 00 00
00 00 00 0C 8B BC E8 FD FC 8F 9E 4A 00 00
00 00 00 04 B1 D8 F1 61 AB 00 00 00 00 00
00 00 00 00 03 49 C4 00 00 00 00 00 00 00
00 00 00 00 00 02 B3 71 1B 00 00 00 00 00
00 00 00 00 00 00 14 B5 DB 32 00 00 00 00
00 00 00 00 00 00 00 04 94 EB 10 00 00 00
00 00 00 00 00 00 2E A4 EB DF 00 00 00 00
00 00 00 00 16 97 F5 EF 86 13 00 00 00 00
00 00 38 A7 F4 FA 94 16 00 00 00 00 00 00
00 00 61 7E 56 25 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00


Image is saved into './output_of_mAiLab006/image_1_average_pooling.bmp'.

 Max pooling image of input_# 2
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 EE FD FC 00 00 00 00
00 00 00 00 00 0A E0 FD FC FC FD 00 00 00
00 00 00 00 00 EE FD FD FD BD FF 00 00 00
00 00 00 00 A5 FD FC 4B 79 00 FD A5 00 00
00 00 00 39 FC F0 1C 00 00 00 FD C3 00 00
00 00 00 F6 FD 00 00 00 00 00 FF C4 00 00
00 00 00 FC E6 00 00 00 07 FC FD 0C 00 00
00 00 00 FD E1 00 00 72 FD FC 00 00 00 00
00 00 00 FC FC E5 FC FD DF 38 00 00 00 00
00 00 00 C7 FC FD FC 91 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00


Image is saved into './output_of_mAiLab006/image_2_max_pooling.bmp'.

 Average pooling image of input_# 2
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 54 E5 AE 00 00 00 00
00 00 00 00 00 02 54 F6 EC CD 6D 00 00 00
00 00 00 00 00 71 FC CA F6 66 D2 00 00 00
00 00 00 00 3E F4 B4 15 23 00 FA 35 00 00
00 00 00 10 E9 5D 0B 00 00 00 FC 61 00 00
00 00 00 82 C9 00 00 00 00 00 FD 56 00 00
00 00 00 A8 77 00 00 00 01 83 B7 03 00 00
00 00 00 A9 5C 00 00 1C B0 92 00 00 00 00
00 00 00 A8 E0 82 BF E7 82 0E 00 00 00 00
00 00 00 3F DD FC A5 24 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00


Image is saved into './output_of_mAiLab006/image_2_average_pooling.bmp'.

 Max pooling image of input_# 3
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 E8 27 00 00
00 00 A3 00 00 00 00 00 00 02 D2 28 00 00
00 00 DE 00 00 00 00 00 00 B7 FE 00 00 00
00 78 FE 00 00 00 00 00 00 E7 FE 00 00 00
00 9F FE 00 00 00 00 0E B2 FE D8 00 00 00
00 9F FE CF FD FE F0 F3 EA FC 28 00 00 00
00 00 B1 B1 B1 62 00 00 A9 FE 00 00 00 00
00 00 00 00 00 00 00 00 A9 FE 00 00 00 00
00 00 00 00 00 00 00 00 A9 FF 00 00 00 00
00 00 00 00 00 00 00 00 A9 FF 00 00 00 00
00 00 00 00 00 00 00 00 60 FE 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00


Image is saved into './output_of_mAiLab006/image_3_max_pooling.bmp'.

 Average pooling image of input_# 3
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 4A 09 00 00
00 00 6C 00 00 00 00 00 00 00 A5 13 00 00
00 00 C0 00 00 00 00 00 00 34 C6 00 00 00
00 29 CE 00 00 00 00 00 00 71 94 00 00 00
00 4F AD 00 00 00 00 03 42 E5 50 00 00 00
00 4D CF 67 7E A7 B7 B3 6F F4 0A 00 00 00
00 00 4A 58 58 26 00 00 43 D8 00 00 00 00
00 00 00 00 00 00 00 00 54 9B 00 00 00 00
00 00 00 00 00 00 00 00 54 AE 00 00 00 00
00 00 00 00 00 00 00 00 54 CB 00 00 00 00
00 00 00 00 00 00 00 00 18 65 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00


Image is saved into './output_of_mAiLab006/image_3_average_pooling.bmp'.

 Max pooling image of input_# 4
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 FD FF 00 00 00
00 00 00 00 00 00 00 00 7F FB FD 00 00 00
00 00 00 00 00 00 00 3C FB FB 1F 00 00 00
00 00 00 00 00 00 00 FD FD BD 00 00 00 00
00 00 00 00 00 00 68 FD FB 00 00 00 00 00
00 00 00 00 00 20 FD FD 17 00 00 00 00 00
00 00 00 00 00 DD FB FB 00 00 00 00 00 00
00 00 00 00 00 FD FB 0C 00 00 00 00 00 00
00 00 00 00 E4 FF FD 00 00 00 00 00 00 00
00 00 00 00 FB FD 00 00 00 00 00 00 00 00
00 00 00 00 C1 FD 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00


Image is saved into './output_of_mAiLab006/image_4_max_pooling.bmp'.

 Average pooling image of input_# 4
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 5E 4F 00 00 00
00 00 00 00 00 00 00 00 37 F9 9D 00 00 00
00 00 00 00 00 00 00 0F C3 C9 09 00 00 00
00 00 00 00 00 00 00 6B F8 3F 00 00 00 00
00 00 00 00 00 00 22 F0 90 00 00 00 00 00
00 00 00 00 00 08 CE D6 05 00 00 00 00 00
00 00 00 00 00 69 FB 73 00 00 00 00 00 00
00 00 00 00 00 F7 C4 03 00 00 00 00 00 00
00 00 00 00 6C FC 6C 00 00 00 00 00 00 00
00 00 00 00 9D EC 00 00 00 00 00 00 00 00
00 00 00 00 36 76 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00


Image is saved into './output_of_mAiLab006/image_4_average_pooling.bmp'.

 Max pooling image of input_# 5
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 94 FD FD 94 37 00 00 00
00 00 00 00 04 F2 FC FD FC FD A8 00 00 00
00 00 00 00 FD FC B7 00 FC FC 15 00 00 00
00 00 00 E8 FD B0 24 FC FD 81 00 00 00 00
00 00 00 FC FD FC FC FD FB 00 00 00 00 00
00 00 00 37 FD D9 3E FF 8F 00 00 00 00 00
00 00 00 00 00 00 47 FD 15 00 00 00 00 00
00 00 00 00 00 00 6A FD 15 00 00 00 00 00
00 00 00 00 00 00 2D FF 38 00 00 00 00 00
00 00 00 00 00 00 00 FC FC 0B 00 00 00 00
00 00 00 00 00 00 00 0E FC 2A 00 00 00 00


Image is saved into './output_of_mAiLab006/image_5_max_pooling.bmp'.

 Average pooling image of input_# 5
PS D:\Python> & C:/Users/123/Anaconda3/python.exe d:/Python/mAiLab006.py

 Max pooling image of input_# 1
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 12 12 88 AF FF F7 00 00
00 00 00 31 FD FD FD FD FD E1 FD C3 00 00
00 00 00 12 FD FD FD C6 F7 00 00 00 00 00
00 00 00 00 0E 9A FD 02 00 00 00 00 00 00
00 00 00 00 00 0B FD E1 6C 00 00 00 00 00
00 00 00 00 00 00 51 FD FD 96 00 00 00 00
00 00 00 00 00 00 00 10 FC FD 40 00 00 00
00 00 00 00 00 00 94 FD FD FD 02 00 00 00
00 00 00 00 42 FD FD FD FD 4E 00 00 00 00
00 00 AC FD FD FD FD 50 00 00 00 00 00 00
00 00 FD FD D4 84 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00


Image is saved into './output_of_mAiLab006/image_1_max_pooling.bmp'.

 Average pooling image of input_# 1
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 05 09 41 32 69 5D 00 00
00 00 00 0C 8B BC E8 FD FC 8F 9E 4A 00 00
00 00 00 04 B1 D8 F1 61 AB 00 00 00 00 00
00 00 00 00 03 49 C4 00 00 00 00 00 00 00
00 00 00 00 00 02 B3 71 1B 00 00 00 00 00
00 00 00 00 00 00 14 B5 DB 32 00 00 00 00
00 00 00 00 00 00 00 04 94 EB 10 00 00 00
00 00 00 00 00 00 2E A4 EB DF 00 00 00 00
00 00 00 00 16 97 F5 EF 86 13 00 00 00 00
00 00 38 A7 F4 FA 94 16 00 00 00 00 00 00
00 00 61 7E 56 25 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00


Image is saved into './output_of_mAiLab006/image_1_average_pooling.bmp'.

 Max pooling image of input_# 2
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 EE FD FC 00 00 00 00
00 00 00 00 00 0A E0 FD FC FC FD 00 00 00
00 00 00 00 00 EE FD FD FD BD FF 00 00 00
00 00 00 00 A5 FD FC 4B 79 00 FD A5 00 00
00 00 00 39 FC F0 1C 00 00 00 FD C3 00 00
00 00 00 F6 FD 00 00 00 00 00 FF C4 00 00
00 00 00 FC E6 00 00 00 07 FC FD 0C 00 00
00 00 00 FD E1 00 00 72 FD FC 00 00 00 00
00 00 00 FC FC E5 FC FD DF 38 00 00 00 00
00 00 00 C7 FC FD FC 91 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00


Image is saved into './output_of_mAiLab006/image_2_max_pooling.bmp'.

 Average pooling image of input_# 2
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 54 E5 AE 00 00 00 00
00 00 00 00 00 02 54 F6 EC CD 6D 00 00 00
00 00 00 00 00 71 FC CA F6 66 D2 00 00 00
00 00 00 00 3E F4 B4 15 23 00 FA 35 00 00
00 00 00 10 E9 5D 0B 00 00 00 FC 61 00 00
00 00 00 82 C9 00 00 00 00 00 FD 56 00 00
00 00 00 A8 77 00 00 00 01 83 B7 03 00 00
00 00 00 A9 5C 00 00 1C B0 92 00 00 00 00
00 00 00 A8 E0 82 BF E7 82 0E 00 00 00 00
00 00 00 3F DD FC A5 24 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00


Image is saved into './output_of_mAiLab006/image_2_average_pooling.bmp'.

 Max pooling image of input_# 3
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 E8 27 00 00
00 00 A3 00 00 00 00 00 00 02 D2 28 00 00
00 00 DE 00 00 00 00 00 00 B7 FE 00 00 00
00 78 FE 00 00 00 00 00 00 E7 FE 00 00 00
00 9F FE 00 00 00 00 0E B2 FE D8 00 00 00
00 9F FE CF FD FE F0 F3 EA FC 28 00 00 00
00 00 B1 B1 B1 62 00 00 A9 FE 00 00 00 00
00 00 00 00 00 00 00 00 A9 FE 00 00 00 00
00 00 00 00 00 00 00 00 A9 FF 00 00 00 00
00 00 00 00 00 00 00 00 A9 FF 00 00 00 00
00 00 00 00 00 00 00 00 60 FE 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00


Image is saved into './output_of_mAiLab006/image_3_max_pooling.bmp'.

 Average pooling image of input_# 3
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 4A 09 00 00
00 00 6C 00 00 00 00 00 00 00 A5 13 00 00
00 00 C0 00 00 00 00 00 00 34 C6 00 00 00
00 29 CE 00 00 00 00 00 00 71 94 00 00 00
00 4F AD 00 00 00 00 03 42 E5 50 00 00 00
00 4D CF 67 7E A7 B7 B3 6F F4 0A 00 00 00
00 00 4A 58 58 26 00 00 43 D8 00 00 00 00
00 00 00 00 00 00 00 00 54 9B 00 00 00 00
00 00 00 00 00 00 00 00 54 AE 00 00 00 00
00 00 00 00 00 00 00 00 54 CB 00 00 00 00
00 00 00 00 00 00 00 00 18 65 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00


Image is saved into './output_of_mAiLab006/image_3_average_pooling.bmp'.

 Max pooling image of input_# 4
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 FD FF 00 00 00
00 00 00 00 00 00 00 00 7F FB FD 00 00 00
00 00 00 00 00 00 00 3C FB FB 1F 00 00 00
00 00 00 00 00 00 00 FD FD BD 00 00 00 00
00 00 00 00 00 00 68 FD FB 00 00 00 00 00
00 00 00 00 00 20 FD FD 17 00 00 00 00 00
00 00 00 00 00 DD FB FB 00 00 00 00 00 00
00 00 00 00 00 FD FB 0C 00 00 00 00 00 00
00 00 00 00 E4 FF FD 00 00 00 00 00 00 00
00 00 00 00 FB FD 00 00 00 00 00 00 00 00
00 00 00 00 C1 FD 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00


Image is saved into './output_of_mAiLab006/image_4_max_pooling.bmp'.

 Average pooling image of input_# 4
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 5E 4F 00 00 00
00 00 00 00 00 00 00 00 37 F9 9D 00 00 00
00 00 00 00 00 00 00 0F C3 C9 09 00 00 00
00 00 00 00 00 00 00 6B F8 3F 00 00 00 00
00 00 00 00 00 00 22 F0 90 00 00 00 00 00
00 00 00 00 00 08 CE D6 05 00 00 00 00 00
00 00 00 00 00 69 FB 73 00 00 00 00 00 00
00 00 00 00 00 F7 C4 03 00 00 00 00 00 00
00 00 00 00 6C FC 6C 00 00 00 00 00 00 00
00 00 00 00 9D EC 00 00 00 00 00 00 00 00
00 00 00 00 36 76 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00


Image is saved into './output_of_mAiLab006/image_4_average_pooling.bmp'.

 Max pooling image of input_# 5
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 94 FD FD 94 37 00 00 00
00 00 00 00 04 F2 FC FD FC FD A8 00 00 00
00 00 00 00 FD FC B7 00 FC FC 15 00 00 00
00 00 00 E8 FD B0 24 FC FD 81 00 00 00 00
00 00 00 FC FD FC FC FD FB 00 00 00 00 00
00 00 00 37 FD D9 3E FF 8F 00 00 00 00 00
00 00 00 00 00 00 47 FD 15 00 00 00 00 00
00 00 00 00 00 00 6A FD 15 00 00 00 00 00
00 00 00 00 00 00 2D FF 38 00 00 00 00 00
00 00 00 00 00 00 00 FC FC 0B 00 00 00 00
00 00 00 00 00 00 00 0E FC 2A 00 00 00 00


Image is saved into './output_of_mAiLab006/image_5_max_pooling.bmp'.

 Average pooling image of input_# 5
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 32 73 5B 3A 0D 00 00 00
00 00 00 00 01 60 E7 80 A4 FC 47 00 00 00
00 00 00 00 78 E1 34 00 CA CA 05 00 00 00
00 00 00 5D E8 2E 09 86 E5 23 00 00 00 00
00 00 00 82 C4 A1 E5 F6 8B 00 00 00 00 00
00 00 00 0D 7A 58 20 EE 3F 00 00 00 00 00
00 00 00 00 00 00 11 FC 0A 00 00 00 00 00
00 00 00 00 00 00 2C FC 0A 00 00 00 00 00
00 00 00 00 00 00 0B F4 13 00 00 00 00 00
00 00 00 00 00 00 00 88 A3 02 00 00 00 00
00 00 00 00 00 00 00 03 63 0A 00 00 00 00

'''                