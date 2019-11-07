#archego.py
import sys
import string

finalstr = None
arg_nb = len(sys.argv)
rev = list.reverse(sys.argv)
pos = 0

while pos < arg_nb - 1:
    arg = sys.argv[pos]
    strlen = len(arg)
    newstring = arg[strlen::-1]
    if finalstr:
        finalstr += " " + newstring
    if not finalstr:
        finalstr = newstring
    pos += 1

print(string.swapcase(finalstr))
