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

# Main routines goes here
statement_generator("Money", "$")