import sys

print(f"The name of the script is: {sys.argv[0]}")

print(f"There are {len(sys.argv) - 1} parameters passed.")

num_arguments = len(sys.argv[1:])
i = 1
while(i <= num_arguments):
    print(f"{i} parameters passed as : {sys.argv[i]}")
    i += 1