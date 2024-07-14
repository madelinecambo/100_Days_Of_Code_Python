# For Loops

# In association with lists
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)

# Using a Loop independently of a list
# range function
# generates a range of numbers to loop through
# not inclusive

# for number in range(0, 10):
#     print(number)

for number in range(0, 11, 3):
    print(number)

total = 0
for number in range(1, 101):
    total += number

print(total)



