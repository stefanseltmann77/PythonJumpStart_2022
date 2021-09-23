# %% Contextmanager example on file reading
# writing files the old way
f = open("demo_file", "w")
f.write("content")
f.close()

# writing files the best way
with open("demo_file", "w") as f:
    f.write("content")

# reading files with encoding
with open("demo_file", "w", encoding="UTF8") as f:
    f.read()


# %% How it works

class MyDummyConnection():

    def __new__(cls, *args, **kwargs):
        print("__new__")
        return super(MyDummyConnection, cls).__new__(cls)

    def __init__(self):
        print("__init__")

    def __enter__(self):
        print("__enter__")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")


# call without contextmanager:
conn = MyDummyConnection()
# __enter__ and __exit__ are not touched.

# call with context manager
with MyDummyConnection() as conn:
    # __enter__ and __exit__ are executed.
    pass

# %% Contextmanagers without classes are also possible.
import contextlib


class MyOtherDummyConnection():

    @contextlib.contextmanager
    def get_file(self):
        file = open('tmp.txt', mode='w')
        try:
            yield file
        finally:
            file.close()


conn = MyOtherDummyConnection()

with conn.get_file() as file:
    file.close()

