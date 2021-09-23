# %% variable assignment
# variable assignment is extremely simple
some_string = "abc"
some_number = 123
some_float = 1.23

# %% dynamic casting of types, if sensible
some_number + some_float

# %%  not possible due to dynamic strong typing
some_string + some_number  # throws error

# direct updates are possible
i = 1
i += 1  # 2
i /= 2  # 1
i *= 4  # 4
i -= 2  # 2
assert i == 2

# %% immutability of objects
# example of an update on an immutable int
var_a = 123
var_b = var_a
var_b = var_b + 1

var_a  # 123, unchanged
var_b  # 124

# example of an update on a mutable set
var_a = {'a', 'b'}
var_b = var_a
var_b.add('c')

var_a  # {'a', 'b', 'c'}, changed
var_b  # {'a', 'b', 'c'}

# assign multiple at once with tuple unpacking
a, b = 1, 2


# direct updates are possible
i = 1
i = i + 1  # 2
i = i / 2  # 1
i = i * 4  # 4
i = i - 2  # 2
assert i == 2

x, y = 1, 2