length = 56
width = 33
height = 30.5

Volume = length * width * height
print(f"the volume of the box is {Volume} cubic centimeters.")

# Using List remove function

lst = [1, "string", True, None, True]
print(f"Original list is {lst}")

lst.remove(True)
# The value 1 will be removed, as 1 is equal to True. The first
print(lst)

# write a short program to get the email domain from
# "From firstname.surname@unsw.edu.au Tue Oct 06 10:10:15 2020"

email = "from firstname.surname@unsw.edu.au Tue Oct 06 10:10:15: 2020"

x = email.split()[1].split('@')[1]
print(x)

date = 1
mins = 2

y = "the exam's date is {} you will have {} minutes".format(date,mins)
print(y)

# Lower Case
w = "What"
i = "IS"
c = "CamelCase?"

print('{} {} {}'.format(w,i.lower(),c))

obj.x = 1
obj.y = 2
obj.y = obj.x
obj.x = obj.y

print(obj.x)

a = 'this is called'
b = 'problem'
a = f'{a} Parsons {b}'
b = print
b(a)

# Quiz Week 2

# LISTS
# Use the provided list_a and list_b as your starting point.
# Then, perform the following steps:
#
# 1. Create a new list called sol (for solution) consisting of a slice
#    from list_a from the second element through to the word 'it'
# 2. Remove the value 'bad' from sol
# 3. Add a value 'including' so that it is the last value in sol
# 4. Add a value 'good' so that it is the third value in sol
# 5. Add all elements from list_b to the end of sol

list_a = ['this', 'list', 'has', 'bad', 'words', 'in', 'it', 'bad', 'naughty', 'impish']
list_b = ['good', 'nice', 'friendly']

sol = list_a[1:6]
sol.remove('bad')
sol.append('including')
sol.insert(2,'good')
sol.extend(list_b)
print(sol)

# SETS
# Use the set f_suburbs as given as your starting point. Then,
# 1. Remove all suburbs that don't start with a F
# 2. Ensure that the suburbs listed below are in your set
#         Fairfield
#         Fairfield East
#         Fairfield Heights
#         Fairfield West
#         Fairlight
#         Fiddletown
#         Five Dock
#         Flemington
#         Forest Glen
#         Forest Lodge
#         Forestville
#         Freemans Reach
#         Frenchs Forest
#         Freshwater

f_suburbs = {"Randwick", "Kensington", "Frenchs Forest", "Flemington"}

f_suburbs.remove("Randwick")
f_suburbs.remove("Kensington")

f_suburbs.add("Fairfield")
f_suburbs.add("Fairfield East")
f_suburbs.add("Fairfield Heights")
f_suburbs.add("Fairfield West")
f_suburbs.add("Fairlight")
f_suburbs.add("Fiddletown")
f_suburbs.add("Five Dock")
f_suburbs.add("Flemington")
f_suburbs.add("Forest Glen")
f_suburbs.add("Forest Lodge")
f_suburbs.add("Forestville")
f_suburbs.add("Freemans Reach")
f_suburbs.add("Frenchs Forest")
f_suburbs.add("Freshwater")

print(f_suburbs)

# TUPLES

# The Fibonacci sequence is 0, 1, 1, 2, 3, 5, ... where each
# subsequent number is equal to the the preceeding two.
# This means the next elements in the list above would be 8 (5 + 3)
# and 13 (8 + 5)
#
# The 9th element in the sequence is 21. Let's call this the `current` value.
# The 8th element in the sequence is 13. Let's call this the `last` Value.
#
# Using PARALLEL ASSIGNMENT/TUPLE UNPACKING, perform the following operations
# in a single statement
#   1. replace the value of `current` with the value of the 10th
#       element in the sequence (so the sum of the 8th and 9th element)
#   2. replace the value of `last` with the value of the 9th element

# Leave this here
current = 21 # at this point, the 9th element of the sequence
last = 13 # at this point, the 8th element of the sequence
# Now, use parallel assignment to replace the value of `current` and `last`
# (put your answer below)

(current, last) = (last + current, current)

# DICTIONARY

# Use the dictionary f_suburbs as given as your starting point.
# This dictionary contains Sydney suburb/population pairs,
# with the mapping going from suburb keys to population values.

# Do the following steps:
# 1. Remove all suburbs that don't start with a F
# 2. Ensure that your dictionary contains:
#
#     Fairfield: 18081
#     Fairfield East: 5273
#     Fairfield Heights: 7517
#     Fairfield West: 11575
#     Fairlight: 5840
#     Fiddletown: 233
#     Five Dock: 9356
#     Flemington: None
#     Forest Glen: None
#     Forest Lodge: 4583
#     Forestville: 8329
#     Freemans Reach: 1973
#     Frenchs Forest: 13473
#     Freshwater: 8866

# The None values indicate the Wikipedia did not have population data.
# These should be INCLUDED in your dictionary.


f_suburbs = {"Randwick": 29986, "Kensington": 15004, "Frenchs Forest": 13473, "Flemington": None}
f_suburbs.pop("Randwick")
f_suburbs.pop("Kensington")

f_suburbs.update({"Fairfield": 18081,
                    "Fairfield East": 5273,
                    "Fairfield Heights": 7517,
                    "Fairfield West": 11575,
                    "Fairlight": 5840,
                    "Fiddletown": 233,
                    "Five Dock": 9356,
                    "Flemington": None,
                    "Forest Glen": None,
                    "Forest Lodge": 4583,
                    "Forestville": 8329,
                    "Freemans Reach": 1973,
                    "Frenchs Forest": 13473,
                    "Freshwater": 8866})

print(f_suburbs)

# Define a few lists...
lst_a = ['a']
lst_b = ['b', lst_a]
lst_c = ['b', ['a']]

lst_c[1].append("c")

print(lst_a)
print(lst_b[1])
print(lst_c[1])

' some text '.strip('')


def create_dict_from_list_elements(input_list):
    if len(input_list) % 2 != 0:
        raise ValueError("The input list must have an even number of elements.")

    result_dict = {}
    for i in range(0, len(input_list), 2):
        key = input_list[i]
        value = input_list[i + 1]
        result_dict[key] = value

    return result_dict


# Example usage:
input_list = ["name", "John", "age", "30", "city", "New York"]
my_dict = create_dict_from_list_elements(input_list)
print(my_dict)
