# %% SET Creation

# an empty set has to be created with the set() function:
empty_set = set()

# can create sets directly by just using the curved brackets
basket = {'pear', 'apple', 'bread', 'apple', 'cookie', 'pear'}
# {'apple', 'bread', 'cookie', 'pear'}
basket.add('apple')
# {'apple', 'bread', 'cookie', 'pear'}
basket.add('milk')
# {'apple', 'bread', 'cookie', 'milk', 'pear'}
basket

# %% SET Operations
# Which element is new
other_basket = {'apple', 'fish', 'cookie'}
other_basket.difference(basket)
# {'fish'}


# what is the common set from both baskets
totally_other_basket = {'cheese', 'grapes', 'apple'}
basket.intersection(totally_other_basket)
# {'apple'}

# what is the combined set of all basket ?
basket.union(other_basket).union(totally_other_basket)

# %% SET conversion
some_list = list(basket)  # to list
basket = set(some_list)  # and back agains

# %% typical usecase: find mismatch in columnsets (not working without dataframes)
# list(set(dataframe.columns).difference(set(other_dataframe.columns)))
