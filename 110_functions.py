# %% a very simple function definition

# cast an input to upper case strings
def make_upper(input):
    return input.upper()

# %% a more complex template
def do_something_fancy_with_input(input, some_function, repetition=1):
    """Oneliner comment

    Further comments"""
    fancy_result = some_function(input) * repetition
    return fancy_result

# %% calling functions
# most simple function call
do_something_fancy_with_input("x", make_upper, 3)

# the order my vary
do_something_fancy_with_input(repetition=3, some_function=make_upper, input="x")

# function calls via tuple
args_tuple = ("x", make_upper, 3)
do_something_fancy_with_input(*args_tuple)

# function calls via dict
args_dict = {"function": make_upper, "repetition": 3, "input": "x"}
do_something_fancy_with_input(**args_dict)


do_something_fancy_with_input(repetition=3, some_function=make_upper, input="x")

# %% function with args
def a_flexible_function(some_func, *args, **kwargs):
    for element in args:
        some_func(element)
    for key, value in kwargs.items():
        some_func(value)

a_flexible_function(print, "A", "B", some_key="C", some_key_otherkey="D")


# %% scope of variables in functions

some_string = "hello, I'm on the outside"

def do_someting():
    print(some_string)
    some_other_string = some_string + ", but also on the inside"
    print(some_other_string)

do_someting() # shows the outer string
print(some_string)

# this is dangerous!!!! better:
def do_someting(some_string_input):  # pick a NEW name
    print(some_string_input)
    some_other_string = some_string_input + ", but also on the inside"
    print(some_other_string)


# %% Example for a function that filters on a specific file-ending
from typing import List
from pathlib import Path
import os

# first attempt. It is not very generic and only works for one ending
def get_files_by_rst():
    """Get all files that end with 'rst'"""
    files = os.listdir(target_path)
    files_filtered = [file for file in files if file.endswith("rst")]
    return files_filtered

# better version that, takes the ending as a parameter
def get_files_by_ending(ending, with_ending = True):
    files = os.listdir(target_path)
    files_filtered = [file for file in files if file.endswith(ending)]
    if not with_ending:
        files_filtered = [file.split(".")[0] for file in files_filtered]
    return files_filtered

# lets use the function
target_path = Path(r"C:\Users\Stefan.Seltmann\PycharmProjects\python_trainings_master\exercises")
args = {'ending': 'rst', 'with_ending': True}
rst_files = get_files_by_ending(ending='rst')
rst_files = get_files_by_ending('rst', False)
rst_files = get_files_by_ending(with_ending=False, ending='rst',)
html_files = get_files_by_ending('html')
py_files = get_files_by_ending('py')


# best version that also uses type hints. Major improvement is the addition of a search-path parameter
def get_files_by_ending_typed(search_path, ending: str, with_ending: bool = True) -> List[str]:
    """Function for filtering my files depending on a path."""
    files: List[str] = os.listdir(search_path)
    files_filtered: List[str] = [file for file in files if file.endswith(ending)]
    if not with_ending:
        files_filtered: List[str] = [file.split(".")[0] for file in files_filtered]
    return files_filtered

# also possible to call functions via a dict
args = {'ending': 'rst', 'with_ending': True}
get_files_by_ending(**args)
