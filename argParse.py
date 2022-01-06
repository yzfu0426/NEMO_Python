import math
import argparse

parser = argparse.ArgumentParser(description='Calculate the volume of a cylinder, users need to provide the radius and height of the cylinder.')
parser.add_argument('-r','--radius', type = int, metavar = '', required = True, help = 'Radius of Cylinder')
parser.add_argument('-H', '--height', type = int, metavar = '', required = True, help = 'Height of Cylinder')
group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action = 'store_true', help='print quiet')
group.add_argument('-v', '--verbose', action = 'store_true', help='print verbose')
group1 = parser.add_mutually_exclusive_group()
group1.add_argument('--AAA', type = float, default = 1.0, help='')
group1.add_argument('--BBB', type = float, default = 2.0, help='')

args = parser.parse_args()

def cylinder_volume(radius, height):
    vol = (math.pi) * (radius **2) * (height)
    return vol

if __name__ == '__main__':
    vol = cylinder_volume(args.radius, args.height)
    if args.quiet:
        print (vol)
    elif args.verbose:
        print ("Volume of a Cylinder with radius %s and height %s is %s" % (args.radius, args.height, vol))
    else: 
        print ("Volume of Cylinder = %s" % vol)
    
    print(type(args))
