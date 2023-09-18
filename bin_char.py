## Function to Convert Binary to Character
def bin_chars():
    byte_list = []
    # Open the Input and Output Files
    with open('ext_input.txt', 'r') as file_in, open('ext_output.txt', 'w') as file_out:
        # Read in the Binary Data and Split it into Groups of 8 Bits
        binary_data = file_in.read()
        for i in range(0, len(binary_data), 8):
            byte = binary_data[i:i+8]
            byte_list.append(byte)
        # Loop Over Each Group of 8 Bits and Convert it to an ASCII Character
        for i in byte_list:
            ascii_char = chr(int(i, 2))
            file_out.write(ascii_char)
#bin_chars()