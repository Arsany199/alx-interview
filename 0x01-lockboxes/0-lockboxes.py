#!/usr/bin/python3
"""function that determines if box containing list can be opened using keys"""


def canUnlockAll(boxes):
    """Determines if boxes can be unlocked or not"""
    place = 0
    unlocked = {}

    for b in boxes:
        if len(b) == 0 or place == 0:
            unlocked[place] = "always_unlocked"
        for key in b:
            if key < len(boxes) and key != place:
                unlocked[key] = key
        if len(unlocked) == len(boxes):
            return True
        place = place + 1
    return False
