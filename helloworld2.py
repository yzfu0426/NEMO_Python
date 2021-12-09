#Second way, use "argument = "as option, 
# still use regular expression to replace the everything before the "=".

import sys, re

name = re.sub("[A-Za-z]+\=", "", sys.argv[1])
age = int(re.sub("[A-Za-z]+\=", "", sys.argv[2]))


print (f"In file 2, Hello my name is {name} and I am {age}")
