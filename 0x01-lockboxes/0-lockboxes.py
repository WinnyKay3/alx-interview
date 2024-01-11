#!/usr/bin/python3
'''Write a method that determines if all the boxes can be opened'''


def canUnlockAll(boxes):
    '''Check if all boxes can be unlocked
    :param boxes:
    :return: True or False
    '''

    if not boxes or type(boxes) is not list:
        return False

    unlocked = [0]
    for n in unlocked:
        for key in boxes[n]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True

    return False
