#First way, just use -Option, and use regular expression to replace the hyphen.

import sys, re

name = re.sub("\-", "", sys.argv[1])
age = int(re.sub("\-", "", sys.argv[2]))


print (f"In file 1, Hello my name is {name} and I am {age}")