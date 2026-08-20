import sys
from pathlib import Path

if len(sys.argv) > 1:
    extensions = [sys.argv[1]]
else:
    extensions = [".err", ".out"]

for extension in extensions:
    for file in Path.cwd().glob(f"*{extension}"):
        if file.is_file():
            print(f"Deleting {file}")
            file.unlink()