#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill?"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
split_n = int(input("How many people to split the bill?"))

# the calculation for adding the tip to the total bill and then dividing among people paying
split_amount = round((total_bill + total_bill * tip/100)/split_n, 2)

# print the amount that everyone should pay. Use string formatting to show 2 decimal places in all cases
print(f"Each person should pay: ${split_amount:.2f}")
