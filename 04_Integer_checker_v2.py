# checks input is a number more than zero
def num_check(question, low):

    valid = False
    while not valid:

        error = "please insert a number that is more than "
        "(or equal to) {}".format(low)

        try:

            # ask user to enter a number
            response = int(input(question))

            # checks number is more than zero 
            if response > low:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)

# Main Routine goes here

keep_going = ""
while keep_going == "":
    print()
    # ask user for an integer (must be more than / equal to 0)
    var_integer = num_check("Enter an integer: ", 0)
    print()

    # ask for width and height of an image
    # (must be more than / equal to 1)
    image_width = num_check("Image width?", 1)
    print()
    image_height = num_check("Image height?", 1)

    print("""

You chose an integer of {}
Your width is {}
Your height is {}

    """.format(var_integer, image_width, image_height))

    keep_going = input("Again? <enter to repeat, any key to quit>")