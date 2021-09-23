import os

# where am I
print(os.getcwd())

# set new path
os.chdir("mypath")

# %% path introspection
# what is located in the data folder?
os.listdir("./data")

# walk the directory
list(os.walk("./data"))

dummy = list(os.scandir("./data/Stocks")) [0]

filenames = os.listdir("./data/Stocks")
