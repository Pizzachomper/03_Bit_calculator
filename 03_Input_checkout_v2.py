# Checks user choice is 'integer' 'text' or 'image'\
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

# Main routine goes here
keep_going = ""
while keep_going == "":
    data_type = user_choice()
    print("You choose", data_type)
    print()