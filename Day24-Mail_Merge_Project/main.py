# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()


#don't have to remember to close the file
with open("../../../OneDrive/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)



# with open("new_file.txt", mode = "w") as file:
#     file.write("New Text.")
