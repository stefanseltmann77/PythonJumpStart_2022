################################################################################################################
# Handling files the simple way

f = open("data/Stocks/aal.us.txt")
f.readline()  # 'Date,Open,High,Low,Close,Volume,OpenInt\n'
f.readline()  # '2013-12-10,23.698,24.345,23.61,24.064,18043837,0\n'
f.readlines()   # '2013-12-12,25.342,25.832,24.616,24.616,20749989,0\n' .... .... ... and so on
f.readlines()   # []  the file is depleted

f.seek(0)   # reset the cursor
f.readline()  # 'Date,Open,High,Low,Close,Volume,OpenInt\n'

f.seek(0)   # reset the pointer
f.read(20)  # 'Date,Open,High,Low,C'  just 20 characters

from collections import namedtuple
with open("data/Stocks/aal.us.txt") as f:
    content = f.read()
    content_parsed = [row.split(",") for row in content.strip().split("\n")]

    content_header, content_data = content_parsed[0], content_parsed[1:]
    StockRecord = namedtuple("StockRecord", field_names=content_header)
    data_set = [StockRecord._make(row) for row in content_data]



import csv
# get the result as tuples
with open("data/Stocks/aal.us.txt") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


# get the result as dicts
with open("data/Stocks/aal.us.txt") as f:
    reader = csv.DictReader(f, quotechar='"', delimiter=",")
    for row in reader:
        print(row)  # every row is a dictionary
# date gets accessible as an array of ordered dicts.


# Or use your own dialect, if you need it more often.
csv.register_dialect("my_dialect", quotechar='"', delimiter=",", escapechar="\\", lineterminator="\r\n")
with open("data/Stocks/aal.us.txt") as f:
    reader = csv.DictReader(f, dialect="my_dialect")


import pandas as pd
data = pd.read_csv("data/Stocks/aal.us.txt") # read it
data.to_csv("some_output")  # write it pack
data.to_dict(orient="record")   # get the equivalent of a csv.DictReader


# %% how to write to a file
my_data = [(1, "Boryana"), (2, "Harald"), (3, "Verena")]

with open("class_list", "w") as f:  # use "w" as the writing mode
    f.write("SeatNumber,Name\n")
    for row in my_data:
        print(",".join([str(chunk) for chunk in row]), file=f)

