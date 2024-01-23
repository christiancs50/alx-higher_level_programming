#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        divident = a / b
    except (ZeroDivisionError):
        divident = None
    finally:
        print("Inside result: {}".format(divident))
        return divident
