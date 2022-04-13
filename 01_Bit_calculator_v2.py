# Functions go here

# Puts series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):

# Make string with five charecters
    ends = decoration * 5

    # Add decoration to start and end of statement
    statement = "{}  {}  {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""

# Checks user choice is 'integer', 'text', or 'image'
def user_choice():

    valid = False
    while not valid:
        
        # Ask user for choice and change response to lowercase
        response = input("File type (integer / text / image): ").lower()

        # If they choose "t" or "text", return response
        text_ok = ["text", "t", "txt"]
        if response in text_ok:
            return "text"

        integer_ok = ["integer", "int", "#", "number"]
        if response in integer_ok:
            return "integer"

        image_ok = ["image", "img", "pix", "picture", "pic", "p"]
        if response in image_ok:
            return "image"            

        if response == "i":
            want_integer = input("Press <enter> for an integer or any key for an image")
            if want_integer == "":
                return "integer"
            else:
                return "image"

        else:
            # If response is not valid, output an error
            print("Please choose a valid file type!")
            print()

# checks input is a number more than a given value
def num_check(question, low):

    valid = False
    while not valid:

        error = "please insert a number that is more than "
        "(or equal to) {}".format(low)

        try:

            # ask user to enter a number
            response = int(input(question))

            # checks number is more than zero 
            if response >= low:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)

# calculates the # of bits for text (# of characters x 8)
def text_bits():

    print()
    # ask user for a string
    var_text = input("Enter some text: ")

    # calculate # of bits (length of string x 8)
    var_length = len(var_text)
    num_bits = 8 * var_length

    # output answer with working
    print()
    print("\'{}\' has {} characters ...".format(var_text, var_length))
    print("# of bits is {} x 8...".format(var_length))
    print("We need {} bits to represent {}".format(num_bits, var_text))
    print()

# finds # of bits for 24 bit colour
def image_bits():

    # gets width and height...
    image_width = num_check("Image width? ", 1)
    image_height = num_check("Image height? ", 1)

    # calculate # of pixels
    num_pixels = image_width * image_height

    # calculate # bits (24 x num pixels)
    num_bits = num_pixels * 24

    # output answer with working
    print()
    print("# of pixels = {} x {} = {}".format(image_height,
                                              image_width, num_pixels))
    print("# of bits = {} x 24 = {}".format(num_pixels, num_bits))
    print()

    return ""



    # get integer (must be >= 0)
    var_integer = num_check("Please enter an integer: ", 0)

    var_binary = "{0:b}" .format(var_integer)

    # calculate # of bits (length of string above)
    num_bits = len(var_binary)

    # output answer with working
    print()
    print("{} in binary is {}".format(var_integer, var_binary))
    print("# of bits is {}".format(num_bits))

# converts decimal to binary and states how many bits are needed to represent the original integer
def int_bits():

    # get integer (must be >= 0)
    var_integer = num_check("Please enter an integer: ", 0)

    var_binary = "{0:b}" .format(var_integer)

    # calculate # of bits (length of string above)
    num_bits = len(var_binary)

    # output answer with working
    print()
    print("{} in binary is {}".format(var_integer, var_binary))
    print("# of bits is {}".format(num_bits))

# Main routines goes here

# Heading
statement_generator("Bit calculator for Integers, Text and Images", "-")

# Display instructions if user has not used the program before

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    # Ask the user for the file type
    data_type = user_choice()
    print("You choose", data_type)

    # For integers, ask for integer
    if data_type == "integer":
        int_bits()

    # For images, ask for width and height
    # (must be an integer more than / equal to 0)
    elif data_type == "image":
        image_bits()

    # For text, ask for a string
    else:
        text_bits()

    keep_going = input("press <enter> for another calculation or any key to quit")