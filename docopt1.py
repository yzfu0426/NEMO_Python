
"""
Usage: docopt1.py -b BBB [options]   

-a AAA --aaa AAA   the a variable is an integer [default: 1]
-b BBB --bbb BBB   the b variable is a float 

This program is beautiful!


"""

from docopt import docopt
arguments = docopt(__doc__)

print(arguments)

a = int(arguments['--aaa'])
b = float(arguments['--bbb'])

print(a, b)
#At least one variable required, one or more variable have default value

#try catch, user friendly