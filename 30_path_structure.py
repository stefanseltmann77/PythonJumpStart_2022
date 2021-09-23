import sys
import os

# where am I
print(os.getcwd())

# what is Python seeing?
print(sys.path)

# which python am I using?
sys.version

# where is it installed?
sys.executable

# pimp my path
sys.path.append("/somedirectory/modules")

