import configparser

# just a simple example config
config_string = """
[company]
name=btelligent
city=munich
years=15
"""

# initialize the config object
configs = configparser.ConfigParser()

# fill the object
configs.read_string(config_string)

# get the metadata
configs.sections()
configs.options("company")

# retrieve the config
configs.get("company", "name")
configs["company"].get("name")
configs["company"]["name"]

# This is not true!
assert configs.get("company", "years") == 15

# use typed get-functions
assert configs.getint("company", "years") == 15

# use dicts for configs

# just a simple example config
config_dict = {"company": {"name": "btelligent",
                           "years": 15,
                           "staff": 160},
               "training": {"topic": "python"}}
# load the dict on the existing object
configs.read_dict(config_dict)

# notice, that it just updates the existing
configs.sections()
configs.options("company")
