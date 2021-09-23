import sys

# %% Create a empty dictionary
my_dict = dict()  # deprecated
my_dict = {}  # aktuell

# keys and values my have mixed types.
# keys must be hashable
# here they are integers but also strings
my_dict = {1: 'one',
           2: 'two',
           'three': 3}

# %% Retrieve keys
# retrieve values
my_dict[1]  # by value
my_dict.get(2)  # by method
my_dict.get('one')

# throws KeyError if you pick a wrong key
try:
    my_dict[3]
except KeyError:
    pass
# returns none but without error
my_dict.get(3)
# returns default
my_dict.get(3, "default")

# just pick the keys
my_dict.keys()
# just pick the values
my_dict.values()
# just pick both as tuples
my_dict.items()

# sets defaults while retrieving
my_dict.setdefault(99, []).append('66')
my_dict

# in python3 only special dicts as a return value:
print(my_dict.values())  # dict_values(['eins', 'zwei', 3])
print(list(my_dict.values()))  # ['eins', 'zwei', 3]

# iterate pythonic:
for key, value in my_dict.items():
    print(key, value)

# %% example for usecase as data definition
campaign_metadata = {123: {'testgroup': True,
                           'samplesize': 10000,
                           'channel': 'mail'},
                     456: {'testgroup': False}}

# pick the channel for 123
campaign_metadata[123]['channel']
# pick the channel for 456
campaign_metadata[456].get('channel', 'unkown')

for campaign_id, campaign_config in campaign_metadata.items():
    print(campaign_id, campaign_config)


# %% updating an existing dict with a new dict

some_base_dict = {'abc': 123, 'def': 456, 'ghj': 789}
some_new_dict = {'def': 555, 'ghj': 888}

# updating the dict in place
some_base_dict.update(some_new_dict)

# updating the dict on the fly, only on Python 3.9+
if sys.version_info.major >=3 and sys.version_info.minor >= 9:
    combined_dict = some_base_dict | some_new_dict
