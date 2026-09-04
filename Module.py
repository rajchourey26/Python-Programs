# Two types of modules-

#1.built in module  math , os ,   . list of all module https://docs.python.org/3/py-modindex.html

import math
print(math.sqrt(2))

import os

import My_module  # this module which I created in file {My_module} 
My_module.hello() # and the name of the function is {hello} inside it. 

import mymodule2
mymodule2.mymodule2()

#2.external module 
#pip install requests

import requests
r=requests.get("https://www.google.com")
print(r.text)
