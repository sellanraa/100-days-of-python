# def my_function():
#     return 3 * 2

# # return is what signals what to output

# print(my_function())

# Functions with outuputs

def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

formatted_string = format_name("angela", "YU")
print(formatted_string)