import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("path")
args = parser.parse_args()

target_dir = Path(args.path)

if not target_dir.exists():
    print("Doesnt exist")
    raise SystemExit(1)

for entry in target_dir.iterdir():
    print(entry.name)