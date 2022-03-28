integer_var = 123456
list_var = [1, 2, 3, 4, 5]


def do_something(integer_input, list_input):
    print(integer_input is integer_var)
    print(list_var is list_input)
    integer_input += 2
    list_input.append(6)


do_something(integer_var, list_var)
print(integer_var)
print(list_var)
