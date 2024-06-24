#!/usr/bin/python3
"""model determines if a given data set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """function that return True if data is a valid UTF-8 else return False"""
    mycount = 0
    for i in data:
        binari = bin(i).replace('0b', '').rjust(8, '0')[-8:]
        if mycount == 0:
            if binari.startswith('10'):
                return (False)
            if binari.startswith('110'):
                mycount = 1
            if binari.startswith('1110'):
                mycount = 2
            if binari.startswith('11110'):
                mycount = 3
        else:
            if not binari.startswith('10'):
                return (False)
            mycount = mycount - 1
    if mycount != 0:
        return (False)
    return (True)
