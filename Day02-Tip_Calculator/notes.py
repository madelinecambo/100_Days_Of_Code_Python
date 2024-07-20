# Data Types

# String

#subscripting
print("HelLo"[0])

# String concatenation
print("123" + "455")

# Integer (whole numbers no decimal places)
print(123 + 345)

# the computer will ignore _ in numbers. Makes it more human readable
print(123_456_893)

# Float Type
print(3.1456)

# Boolean - True or False
print(True)
print(False)

# num_char = len(input("What is your name?"))
# print("Your name has " + str(num_char) + " characters.")

# type conversion (casting) - used to change variable types

print(int(6/3))
#will yield a floating number. happens everytime with division

# Basic Math Operations
3 + 5
7 - 4
3 * 2
6 / 3
2 ** 3

# always keep in mind PEMDAS-LR
# ()
# **
# * /
# + -
# result will be 7

print(3 * (3 + 3) / 3 - 3)

# round function
print(round(8/3, 2))

# Floor Division - will just give you an integer - no rounded. Just truncates the number
print(8//3)

# when you need to manipulate a value based on prior value
score = 0
score += 1

print(score)

height = 1.8
isWinning = True

# f strings - mix strings and different data types
print(f"your score is {score}, your height is {height}, and you are winning is {isWinning}")



