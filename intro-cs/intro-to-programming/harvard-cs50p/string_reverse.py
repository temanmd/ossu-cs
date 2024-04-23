import sys


string = sys.argv[1].strip()
for i in range(len(string)):
    print(string[-(i + 1)], end="")
print("")
