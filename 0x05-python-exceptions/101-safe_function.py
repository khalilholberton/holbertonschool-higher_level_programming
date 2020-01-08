#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        func = fct(*args)
    except Exception as err:
        func = None
        print('Exception: {}'.format(err), file=sys.stderr)
    return func
