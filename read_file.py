# fileName = 'data_of_mAiLab003/train-images.idx3-ubyte'
fileName = 'data_of_mAiLab003/test_file_io.hex'


# a placeholder for 2D array
matrix_image = None



# preview counter
count = 0

# byte count
byte_count = 0

with open(fileName, 'rb') as f:
   while True:


        byte_s = f.read(1)
        print( "byte_s", byte_s)

        if not byte_s:
            # Handle End-of-File
            break

        byte = byte_s[0]



        byte_count +=1

        if count < 10:
            print( format(byte, '02X') )  
            # print( "{:02X}".format( byte ) )    
            count += 1
      
        if 10 == count:
            break