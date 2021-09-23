# first builtins
import os
import sys

# first then own modules
import btelligent_module

# possible, but not encouraged
import os, sys

# nested imports until last level possible.
import datetime

datetime.datetime.today()
# or
from datetime import datetime

datetime.today()

# possible and accepted
from datetime import datetime, date

# standard pattern in Pandas:
import pandas as pd
import numpy as np
