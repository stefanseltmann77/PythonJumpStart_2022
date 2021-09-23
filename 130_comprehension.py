# I want all chars as upper case
some_strings = ['A', 'b', 'C', 'd', 'E', 'f']

# basic approach
list(map(str.upper, some_strings))  # ['A', 'B', 'C', 'D', 'E', 'F']

# ok, but what if the function is more complex
def make_upper(input): return input.upper()
list(map(make_upper, some_strings))  # ['A', 'B', 'C', 'D', 'E', 'F']
# ... that's nice put not very pythonic

# That's a naive approach
some_strings_upper = []
for chunk in some_strings:
    some_strings_upper.append(chunk.upper())
# ['A', 'B', 'C', 'D', 'E', 'F']

# and here the list comprehension
some_strings_upper = [chunk.upper() for chunk in some_strings]


# some string with German sz
some_strings = ['A', 'b', 'C', 'd', 'E', 'f', 'ß']
# That's a naive approach
some_strings_upper = []
for chunk in some_strings:
    if chunk != 'ß':
        some_strings_upper.append(chunk.upper())
# and here a filtered list comprehension
some_strings_upper = [chunk.upper() for chunk in some_strings if chunk != 'ß']
# if it doesn't fit a line, write it like this:
some_strings_upper = [chunk.upper()
                      for chunk in some_strings
                      if chunk != 'ß']


# double "for loops" possible
einmaleins = [x * y  for x in range(10) for y in range(10) if x and y]


# great as well: the dict-comprehension
some_dict = {'A': 1, 'B': 2}
# Auch prima: Die Dict-Comprehension
new_dictionary = {key.lower(): value*2 for key, value in {'A': 1, 'B': 2}.items()}
# {'a': 2, 'b': 4}
