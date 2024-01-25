# Return as an early exit
def format_name(f_name, l_name):
    # Docstrings must be the first line in function
    """Take a first and last name and format it to
    return the title case version of the name. If
    proper inputs aren't provided, there will be an
    early exit of the function."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Result: {formatted_f_name} {formatted_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))