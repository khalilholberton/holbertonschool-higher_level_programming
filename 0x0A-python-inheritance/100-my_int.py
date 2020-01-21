#!/usr/bin/python3
"""
This modules contains MyInt class
"""


class MyInt(int):
    """
    MyInt class
    """
    def __ne__(self, other):
        """
        not  equal
        """
        return (not super().__ne__(other))

    def __eq__(self, other):
        """
        equal
        """
        return (not super().__eq__(other))
