# Module - a python file is a mdoule
# Package - a folder containing multiple modules / files

# Pattern 1 - import all modue
import math

# math.sqrt(16)

# Pattern 2 - import specific items from a module
from math import sqrt, pi

# sqrt(16)

# Built in functions in py
import random
import datetime
import os
import json

number = random.randint(1, 10)
random.choice(["Apple", "Banana", "Orange"])

today = datetime.datetime.now()
print(today)

# Operting system
current_dir = os.getcwd()
print(current_dir)