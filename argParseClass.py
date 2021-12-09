import math
import argparse

class CmdArgs:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height


    def do_things():
        vol = (math.pi) * (radius **2) * (height)
        print ("Volume of a Cylinder with radius %s and height %s is %s" % (args.radius, args.height, vol))

def get_args():
        parser = argparse.ArgumentParser(description='Calculate volume of a cylinder')
        parser.add_argument('-r','--radius', type = int, metavar = '', required = True, help = 'Radius of Cylinder')
        parser.add_argument('-H', '--height', type = int, metavar = '', required = True, help = 'Height of Cylinder')


        return parser.parse_args()

    
def main(args):
    instance = CmdArgs(args.radius, 
                        args.height)

    instance.do_things()


if __name__ == '__main__':
    args = get_args()
    main(args)
