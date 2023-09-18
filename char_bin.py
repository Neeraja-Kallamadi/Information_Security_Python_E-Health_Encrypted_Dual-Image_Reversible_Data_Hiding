## Function to Convert Character to Binary
def char_binary():
    # Open the Input and Output Files
    with open('emb_input.txt', 'r') as file_in, open('emb_output.txt', 'w') as file_out:
        # Loop over Each Character in the Input File
        for char in file_in.read():
            # Convert the Character to Binary and write it to the Output File
            binary = bin(ord(char))[2:].zfill(8)  # Convert to Binary and Pad with Leading Zeros
            file_out.write(binary)
#char_binary()