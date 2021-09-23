# let's create a dictionary
some_dictionary = {'a': 123, 'b': 456}
print(some_dictionary)  # {'a': 123, 'b': 456}

# what is the type of it?
type(some_dictionary)  # dict

# is it a child of?
isinstance(some_dictionary, object)  # true

# what can I do with it? Show me the DOCs!
help(some_dictionary)

# what are the methods and fields?
some_dictionary.__dir__()
# or
dir(some_dictionary)

# example of output:
['__repr__',
 '__hash__',
 # ...
 '__le__',
 '__len__',
 # ...
 'get',
 'setdefault',
 'pop',
 'popitem',
 'keys',
 'items',
 ...]

# what is the unique id of the instance?
id(some_dictionary)

help(some_dictionary.__len__)

# what is the unique id of the instance?
# some_dictionary?
