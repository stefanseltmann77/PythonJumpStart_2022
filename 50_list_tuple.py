# %% CREATE LISTS OR TUPLES

my_list = list()
my_list = []

my_tuple = tuple()
my_tuple = ()

# %% Indexing on tuples or lists
my_list_or_tuple = [1, 2, 3, 4, 5]  # or (1, 2, 3, 4, 5)
my_list_or_tuple[0]  # first = 0
my_list_or_tuple[-1]  # last = 5
my_list_or_tuple[-2:]  # from second to last on = [4, 5]
my_list_or_tuple[1:-1]  # without first or last [2, 3, 4]
my_list_or_tuple[1::2]  # starting with the second and only every second [2, 4]
my_list_or_tuple[2::-1]  # starting with the third and going backwards [3, 2, 1]
3 in my_list_or_tuple  # True
my_list_or_tuple.index(3)  # 2

# %% Operations on tuples or lists
my_list = [1, 2, 3, 4, 5]
my_other_list = [6, 7]
my_list + my_other_list  # [1, 2, 3, 4, 5, 6, 7]
my_list.pop()  # 5
my_list.remove(3)  # delete 3 in place
my_list.extend(my_other_list)  # list+list in place
my_list.append(6)  # list+element in place

# %% Tuple Unpacking
var_a, var_b, var_c = ('a', 'b', 'c')

# even without brackets
var_a, var_b, var_c = 'a', 'b', 'c'

# %% Emumeration:

# unwise, because you need to initialize the variable i
# and update it every time
some_tuple = (1,2,3,4,5,6)
i = 0
for y in some_tuple:
    i += 1
    print(i, y)

# Better, because enumerate returns always the running index and the element:
# like this (0, first_element_of_list), (1, second_element_of_list)
# tuple unpacking will fill it into the variables i and y
for i, y in enumerate(some_tuple):
    print(i, y)






