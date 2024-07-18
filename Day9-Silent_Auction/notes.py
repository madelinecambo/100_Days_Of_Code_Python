# Dictionary
# How to nest lists inside lists and/or dictionaries

# dictionaries - key value pairs
# {key: value}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something again and again"
}

print(programming_dictionary['Function'])
print(programming_dictionary)

# Adding new items to a dictionary
programming_dictionary['New Item'] = "this is a new item!"

print(programming_dictionary)

# Creating an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
# useful if you want to clear a user's progress, restart a game etc.

# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary['Bug'] ="A moth in your computer"

print(programming_dictionary)

# Loop through a dictionary

for key in programming_dictionary:
    print(programming_dictionary[key])

# Nesting
# Can have lists and dictionaries nested inside dictionaries

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France": ["Paris", "Lille", "Dijon"]
}

print(travel_log['France'][0])

# Can also nest lists together
# But generally more useful to do this inside a dictionary

# Nesting a dictionary inside a dictionary

#list that contains two items. Each item is a dictionary. NOTE: can mix data types
travel_log = [
    {
        "country": "France",
        'cities_visited': ["Paris", "Lille", "Dijon"],
        "total_visits":12
    },
    {
        "country":"Germany",
        'cities_visited': ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits":5},
]

print(travel_log)

first_key = list(capitals.keys())[0]
first_value = list(capitals.values())[0]
print(first_key)
print(first_value)

print(capitals.values())