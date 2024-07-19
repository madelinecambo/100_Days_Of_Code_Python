# Functions with Outputs

def my_function():
    result = 3 * 2
    return result

x = my_function()
print(x)


# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return("You didn't provide valid inputs")
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     #return tells you its the end of the function
#     return f"{formatted_f_name} {formatted_l_name}"



print(format_name(input("What is your first name?"), input("What is your last name?")))

# Docstrings
length = len('string')

def format_name(f_name, l_name):
    """Take a first and last name and format it,
     to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return("You didn't provide valid inputs")
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    #return tells you its the end of the function
    return f"{formatted_f_name} {formatted_l_name}"

format_name()