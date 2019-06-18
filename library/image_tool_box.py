


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



# Read and store one image from a file handle of MNIST image
def read_one_MNIST_image( file_handle, h, w ):

    size_of_one_image = h * w
    raw_image_bytes = file_handle.read( size_of_one_image )

    # Create a 2D array of h x w, for storing image pixels
    image_matrix = [ [ 0 for x in range(w) ] for y in range(h) ]

    if ( not raw_image_bytes ) or ( len(raw_image_bytes) != size_of_one_image ) :
        # Handle End-of-File, or exception
        print("Failed to read one MNIST image")
        return -2
    else:
        for i in range( size_of_one_image ):
            image_matrix[ int(i/h) ][ int(i%w) ] = raw_image_bytes[i]

    return image_matrix



# Output image into console
def print_image_array( image_matrix ):

    image_height = len( image_matrix )


    image_width = len( image_matrix[0] )


    for y in range( image_height ):
        for x in range( image_width ):
            print( "{:02X}".format( image_matrix[y][x] ), end = ' ' )

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
                # print("Img")

            else:
                # Padding boundary with dummy 0s
                print( "{:02X}".format( 0x00 ), end = ' ' )

        print()    

    # One more extra new line in order to keep output neat and tidy
    print("\n")



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