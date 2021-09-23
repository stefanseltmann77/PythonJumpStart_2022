import logging
# %% ### Let's set up the stage

some_string = "ABCDEFG"
some_dict = {'first': '1st'}
some_integer = 12345


# %% now let's break things

#  get the 10th letter
some_string[10]  # IndexError

# get the element "second" from the dict, without using "get"
some_dict['second']  # KeyError

# add a string to an integer
some_integer + "a"  # TypeError

# divide by zero
some_divisor = 0
result = some_integer / some_divisor   #  ZeroDivisionError
# ZeroDivisionError: division by zero


# workarounds for the ZeroDivisions [not recommended]
if some_divisor != 0:
    result = some_integer / some_divisor
else:
    result = None

# or with the ternary operator
result = some_integer / some_divisor \
    if some_divisor != 0 else None

# best practice: exceptions
try:
    result = some_integer / some_divisor
except ZeroDivisionError:
    result = None

# if unclear what happens, reraise
try:
    result = some_integer / some_divisor
except:
    logging.exception("Well this went wrong", exc_info=True)
    raise

# reraised exceptions are escalated to the top
try:
    print("upper level")
    try:
        print("deeper level")
        0 / 0
    except ZeroDivisionError:
        print("ZeroDivisionError alert")
        raise
except ZeroDivisionError:
    print("Caught the raise")












