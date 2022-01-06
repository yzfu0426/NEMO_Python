import math
import argparse

class CmdArgs:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        # self.quiet = quiet
        # self.verbose = verbose

    def calculate_volume(self):
        vol = (math.pi) * (self.radius **2) * (self.height)
        print ("Volume of a Cylinder with radius %s and height %s is %s" % (self.radius, self.height, vol))

def get_args():
        parser = argparse.ArgumentParser(description='Calculate volume of a cylinder')
        #Get the name for the program

        parser.add_argument('-r','--radius', type = int, metavar = '', default = 1, help = 'Radius of Cylinder')
        parser.add_argument('-H', '--height', type = int, metavar = '', required = True, help = 'Height of Cylinder')
        # group = parser.add_mutually_exclusive_group()
        # group.add_argument('-q', '--quiet', action = 'store_true', help='print quiet')
        # group.add_argument('-v', '--verbose', action = 'store_true', help='print verbose')


        return parser.parse_args()



    
def main(args):
    instance = CmdArgs(args.radius, 
                        args.height)

    instance.calculate_volume()


if __name__ == '__main__':
    args = get_args()
    main(args)
