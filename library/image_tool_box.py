# For image output to bmp file
import numpy as np
import imageio



# Get height and width from an image array
def get_size_of_image( img ):

    height = len( img )
    width = len( img[0] )

    return (height, width)




# Parse and get MNIST image header from a file handle
def get_MNIST_label_header( file_handle ):

    byte_stream = file_handle.read(8)


    if ( not byte_stream ) or ( len(byte_stream) != 8 ):
        # Handle End-of-File, or exception
        print("Failed to read label header")
        return -1
    else:

        number_of_items = (byte_stream[4] << 24) | (byte_stream[5] << 16) | (byte_stream[6] << 8) | (byte_stream[7])

    return ( number_of_items )



# Parse and get MNIST image header from a file handle
def get_MNIST_image_header( file_handle ):

    byte_stream = file_handle.read(16)


    if ( not byte_stream ) or ( len(byte_stream) != 16 ):
        # Handle End-of-File, or exception
        print("Failed to read image header")
        return -1
    else:

        # Parse header, and we get height and width of image
        img_height = (byte_stream[8] << 24) | (byte_stream[9] << 16) | (byte_stream[10] << 8) | (byte_stream[11])
        
        img_width = (byte_stream[12] << 24) | (byte_stream[13] << 16) | (byte_stream[14] << 8) | (byte_stream[15])


    return ( img_height, img_width )



# Create an image matrix with heigh, width and default pixel value
def create_image_matrx( height = 2 , width = 2, default_pixel_value = 0 ): 
    
    image_matrix = [ [ default_pixel_value for x in range(width) ] for y in range(height)  ]
    return image_matrix


# Read and store one image from a file handle of MNIST image
def read_one_MNIST_image( file_handle, h, w ):

    size_of_one_image = h * w
    raw_image_bytes = file_handle.read( size_of_one_image )

    # Create a 2D array of h x w, for storing image pixels
    image_matrix = create_image_matrx( h, w, 0x00 )

    if ( not raw_image_bytes ) or ( len(raw_image_bytes) != size_of_one_image ) :
        # Handle End-of-File, or exception
        print("Failed to read one MNIST image")
        return -2
    else:
        for i in range( size_of_one_image ):
            image_matrix[ int(i/h) ][ int(i%w) ] = raw_image_bytes[i]

    return image_matrix



# Output image into console
def print_image_array( image_matrix, mode = "Hex" ):

    image_height = len( image_matrix )


    image_width = len( image_matrix[0] )


    for y in range( image_height ):
        for x in range( image_width ):

            if "Hex" == mode:
                print( "{:02X}".format( image_matrix[y][x] ), end = ' ' )
            elif "Decimal" == mode:
                print( "{: 10d}".format( image_matrix[y][x] ), end = ' ' )
            else:
                print("Invliad print mode  {:<10} is not supported.".format(mode) )

        print()    

    # One more extra new line in order to keep output neat and tidy
    print("\n")



# Output image into console with padding
def print_image_array_with_padding( image_matrix , padding_size = 0):

    image_height = len( image_matrix )
    image_width = len( image_matrix[0] )

    new_height = image_height + int(padding_size*2)
    new_width = image_width + int(padding_size*2)


    for y in range( new_height ):
        for x in range( new_width ):

            if padding_size <= y < ( padding_size + image_height ) and padding_size <= x < ( padding_size + image_width ):
                # Draw original image in main center area
                print( "{:02X}".format( image_matrix[y-padding_size][x-padding_size] ), end = ' ' )

            else:
                # Padding boundary with dummy 0s
                print( "{:02X}".format( 0x00 ), end = ' ' )

        print()    

    # One more extra new line in order to keep output neat and tidy
    print("\n")



# Extend an image with specified padding size and padding item.
def extend_image_array_with_padding( image_matrix, padding_size = 0, padding_item = 0x00 ):

    image_height = len( image_matrix )
    image_width = len( image_matrix[0] )

    new_height = image_height + int( padding_size * 2 )
    new_width = image_width + int( padding_size * 2 )

    extended_image = create_image_matrx( new_height, new_width, 0x00 )

    for y in range( new_height):
        for x in range( new_width ):

            if padding_size <= y < ( padding_size + image_height ) and padding_size <= x < ( padding_size + image_width ):
                # Copy original image in main center area
                extended_image[ y ][ x ] = image_matrix[ y-padding_size ][ x-padding_size ]

            else:
                # Padding boundary with specified dummy item
                extended_image[ y ][ x ] = padding_item


    return extended_image


# Generate average image from image container
def gen_average_image( image_container ):

    image_height = len( image_container[0] )
    image_width = len( image_container[0][0] )

    total_image_count = len( image_container )


    # Create a 2D array of h x w, for storing image pixels
    image_sum = [ [ 0 for x in range(image_width) ] for y in range(image_height) ]
    image_avg = [ [ 0 for x in range(image_width) ] for y in range(image_height) ]


    # Summation of all images
    for img_index in range( total_image_count ):
        for y in range( image_height ):
            for x in range( image_width ):
                image_sum[y][x] += image_container[img_index][y][x]


    # Average
    for y in range( image_height ):
        for x in range( image_width ):

            # Use // integer division to round down decimal point
            image_avg[y][x] = image_sum[y][x] // total_image_count


    return image_avg



# Conduct a 2D image convolution with specified kernel 
def img_conv_kernel(img, kernel):

    img_h = len( img )
    img_w = len( img[0] )

    kernel_h = len( kernel )
    kernel_w = len( kernel[0] )
    kernel_size = kernel_h

    # Calculate the padding size from kernel size
    zero_padding_size = kernel_size // 2

    # Locate center position of kernel
    ker_center_y = kernel_h // 2
    ker_center_x = kernel_w // 2

    # Pad original image with dummy 0s
    zero_padding_img = extend_image_array_with_padding( img, zero_padding_size )

    # Create an image array for output convolution result
    output_image = create_image_matrx( img_h, img_w, 0x00 )


    output_img_h = len( output_image )
    output_img_w = len( output_image[0] )


    for y in range(output_img_h):
        for x in range(output_img_w):


            # Coordination translation from output_image to zero-padding image
            zero_padding_img_y = y + zero_padding_size
            zero_padding_img_x = x + zero_padding_size


            for ker_y in range(kernel_h):
                
                # By definition of convolution, 
                # kernel has to flip on both horizontal and vertical direction before dot operation

                flip_y = ( kernel_h - 1 ) - ker_y

                for ker_x in range(kernel_w):

                    flip_x = ( kernel_w - 1 ) - ker_x



                    offset_y = (ker_center_y - flip_y)
                    offset_x = (ker_center_x - flip_x)

                    conv_y = zero_padding_img_y + offset_y
                    conv_x = zero_padding_img_x + offset_x

                    
                    # dot operation
                    output_image[ y ][ x ] += zero_padding_img[ conv_y ][ conv_x ] * kernel[ flip_y ][ flip_x ]



    return output_image



# Conduct absolute value trasform over partial differential image
def absolute_value_tranform_of_partial_differential_img( diff_img ):

    ( img_h, img_w ) = get_size_of_image( diff_img )

    # Create an image array for output 
    output_image = create_image_matrx( img_h, img_w, 0x00 )

    for y in range(img_h):
        for x in range(img_w):

            output_image[y][x] = abs(diff_img[y][x])

    return output_image


# Calculate and create Sobel gradient image
def get_Sobel_gradient_magnitude( img_Gx, img_Gy ):


    img_h = len( img_Gx )
    img_w = len( img_Gx[0] )

    # Create an image array for output convolution result
    gradient_magnitude_image = create_image_matrx( img_h, img_w, 0x00 )

    for y in range(img_h):
        for x in range(img_w):

            # magnitude = sqrt( Gx^2 + Gy^2 )
            sum_of_squre = img_Gx[y][x]**2 + img_Gy[y][x]**2
            magnitude = sum_of_squre**(1/2) 
            gradient_magnitude_image[y][x] = int(magnitude)
            
    return gradient_magnitude_image



# Get the maximum value of an given image
def get_max_value_of_image( img ):

    max_value =  max( map(max, img ) )
    return max_value



def get_edge_image( grad_magnitude_image, threshold_factor = 0.8 ):

    ( img_h, img_w ) = get_size_of_image( grad_magnitude_image )

    max_value = get_max_value_of_image(grad_magnitude_image)

    # Create an image array for output convolution result
    edge_image = create_image_matrx( img_h, img_w, 0x00 )

    for y in range(img_h):
        for x in range(img_w):

            ratio = grad_magnitude_image[y][x] / max_value

            if ratio >= threshold_factor:
                # Mark those pixels above intensity threshold as edge (white pixel)
                edge_image[y][x] = int( ratio * 255 )

    
    return edge_image   



def save_to_bmp( image_matrix, file_name ):

    if None == image_matrix or 0 == len(image_matrix) or 0 == len(image_matrix[0]):
        print("image_matrix is not a valid input")
        return None

    else:
        # Output and save first image as BitMap(.bmp) file.

        print("Image is saved into '{}.bmp'.".format(file_name) )

        # Convert python 2D array(list) to numpy array on datatype uint8.
        # data type: np.uint8 = Unsigned 8 bit integer, from 0 to 255
        numpu_array = np.array( object=image_matrix, dtype=np.uint8 )

        # Save it from numpy array to bmp file
        imageio.imwrite( file_name+".bmp", numpu_array )



# Transpose a 2d array
def array_transpose( array_2d ):

    array_t = [*zip(*array_2d)]

    return array_t



def array_with_negation( array_2d ):

    array_negation = np.negative( array_2d )

    return array_negation