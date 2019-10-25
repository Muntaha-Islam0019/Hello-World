from pathlib import Path

path = Path("Shop")
print(path.exists())

path = Path("Directory")
print(path.exists())

# Creates the directory.
# path.mkdir()

# Removes the directory.
# path.rmdir()

# Returns the name of all .py files.
path = Path()
for a_python_file in path.glob("*.py"):
    print(a_python_file)
