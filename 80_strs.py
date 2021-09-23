######################################################################################################################
## STR is for users, REPR for machines
from datetime import date
some_date = date(2018, 8, 31)
str(some_date)      # '2018-08-31'
repr(some_date)     # 'datetime.date(2018, 8, 31)'


basic_str = "ab\tc"
str(basic_str)      # 'ab\tc'
repr(basic_str)     # "'ab\\tc'"
print(basic_str)    # ab	c


basic_raw_string = r"ab\tc"
str(basic_raw_string)   # 'ab\\tc'
repr(basic_raw_string)  # "'ab\\\\tc'"
print(basic_raw_string) # ab\tc


######################################################################################################################
## Both can be set for objects. REPR is fallback for STR

class Btelligent(object):
    def __init__(self):
        self.name = "b.telligent"

bt = Btelligent()
str(bt)    # '<__main__.Btelligent object at 0x00000200DAA36390>'
repr(bt)   # '<__main__.Btelligent object at 0x00000200DAA36390>'



class Btelligent(object):
    def __init__(self):
        self.name = "b.telligent"

    def __repr__(self):
        return self.name

bt = Btelligent()
str(bt)     # 'b.telligent'
repr(bt)    # 'b.telligent'



class Btelligent(object):
    def __init__(self):
        self.name = "b.telligent"

    def __str__(self):
        return self.name

bt = Btelligent()
str(bt)     # 'b.telligent'
repr(bt)    # '<__main__.Btelligent object at 0x00000200DAA3C588>'


######################################################################################################################
## .format() always casts to str
from datetime import date
some_date = date(2018, 8, 31)
some_tuple = (1, 2, "3", 4, 5)

str(some_date)
repr(some_date)

"{}".format(some_date)
"{!r}".format(some_date)  # back to repr with !

"{}".format(some_tuple)




