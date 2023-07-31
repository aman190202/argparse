import argparse

parser = argparse.ArgumentParser()
parser.add_argument("Name")

args = parser.parse_args()

print(f"{args.Name} is a good man")