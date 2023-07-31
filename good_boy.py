import argparse

parser = argparse.ArgumentParser()
parser.add_argument("Name")
parser.add_argument("-b", "--boy", action="store_true")
parser.add_argument("-g", "--girl", action="store_true")

args = parser.parse_args()

if(args.boy):
    print(f"{args.Name} is a good man")

elif(args.girl):
    print(f"{args.Name} is a good girl")

else:
    print(f"{args.Name} is a good person")

