import sys

def check_partity(nb):
    if nb == -1:
        print("ERROR")
    elif nb == 0:
        print("I'm Zero.")
    elif nb % 2 == 0:
        print("I'm Even.")
    elif nb % 2 == 1:
        print("I'm Odd.")

if len(sys.argv) > 2:
    print("ERROR")
elif len(sys.argv) == 2:
    try:
        nb = int(sys.argv[1])
        check_partity(nb)
    except ValueError:
        print("ERROR")
