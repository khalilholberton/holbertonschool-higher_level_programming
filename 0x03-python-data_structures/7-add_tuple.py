#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        tpa = (0, 0)
    elif len(tuple_a) == 1:
        tpa = (tuple_a[0], 0)
    else:
        tpa = tuple_a
    if len(tuple_b) == 0:
        tpb = (0, 0)
    elif len(tuple_b) == 1:
        tpb = (tuple_b[0], 0)
    else:
        tpb = tuple_b
    big_tuple = (tpa[0] + tpb[0], tpa[1] + tpb[1])
    return (big_tuple)
