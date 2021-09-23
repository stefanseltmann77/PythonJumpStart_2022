# %% simple "if else"
value = "C"
if value == "A":
    print("first")
elif value == "B" or value == "C":
    print("second")
elif value == "D" and True:
    print("third")
else:
    print("all other")

# %% the ternary operator
gender = 'male'

# this if else block works fine, but has three times an assignment to gender_id
if gender == 'male':
    gender_id = 1
elif gender == 'female':
    gender_id = 2
else:
    gender_id = -1

# this oneliner does the same, but only with one assignment
gender_id = 1 if gender == 'male' \
    else 2 if gender == 'female' else -1




# %% case switch via dict
# this does the same, even shorter
value_map = {'male': 1,
             'female': 2}
gender_id = value_map.get(gender, -1)


# %% use ranges

some_range = range(10)
print(some_range)  # range(0, 10)
list(some_range)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
range(1, 10)
range(1, 10, 3)


# %% the loop for elements

# just loop over a list
for number in [1, 2, 3, 4]:
    print(number)

# just loop over a string:
some_string = "abc"
for character in some_string:
    print(character)

# a more complex example:
for i, number in enumerate(range(0, 10, 2)):
    if i % 2 == 0:
        if i == 4:
            continue
        print(number)
    if i > 10:
        break
else:
    print("finished")

