import sys

def check_div(nb1, nb2, mode):
    """check the result of the division in order to prevent a division by 0"""
    if mode == 1:
        if nb2 == 0:
            return "ERROR (div by zero)"
        return nb1 / nb2
    else:
        if nb2 == 0:
            return "ERROR (modulo by zero)"
        return nb1 % nb2

if len(sys.argv) > 3:
    print("InputError: too many arguments\nUsage: python operations.py\nExample:\n    python operations.py 10 3")
elif len(sys.argv) < 3:
    print("Usage: python operations.py\nExample:\n    python operations.py 10 3")
else:
    try:
        nb1 = int(sys.argv[1])
        nb2 = int(sys.argv[2])
    except ValueError:
        print("InputError: only numbers\nUsage: python operations.py\nExample:\n    python operations.py 10 3")
    print("Sum:        %i" % (nb1 + nb2))
    print("Difference: %i" % (nb1 - nb2))
    print("Product:    %i" % (nb1 * nb2))
    print("Quotient:   " + str(check_div(nb1, nb2, 1)))
    print("Remainder:  " + str(check_div(nb1, nb2, 2)))
