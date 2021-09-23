import os
from pathlib import Path

# Doing paths the worst way
filename = "myfile.csv"
project_folder = "/home/my_user/my_folder"
dataset_folder = "datasets"

## DON'T
filepath = dataset_folder + "/" + project_folder + "/" + filename
## DON'T

# Doing paths a litte better
filepath = os.sep.join([dataset_folder, project_folder, filename])
# but still things can go wrong


# Doing paths the best way
filename = Path("myfile.csv")
project_folder = Path("/home/my_user/my_folder")
dataset_folder = Path("datasets")

# save and robust
filepath = project_folder / dataset_folder / filename

# get infos about the path:
filepath.exists()
filepath.is_dir()
filepath.cwd()
