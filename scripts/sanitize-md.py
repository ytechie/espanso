import sys

instring = sys.argv[1]
print(instring.replace("[[", "").replace("]]", ""))