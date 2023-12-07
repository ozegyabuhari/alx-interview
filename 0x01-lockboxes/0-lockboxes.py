#!/usr/bin/python3
"""LockBoxes interview"""


def canUnlockAll(boxes):
    """ Determines if all the boxes can be opened or not
    Returns:
        True: all boxes can be opened
        False: not all boxes can be opened
    """
    num_boxes = len(boxes)
    keys = set()
    unlocked_boxes = []
    j = 0

    while j < num_boxes:
        oldi = j
        unlocked_boxes.append(j)
        keys.update(boxes[j])
        for key in keys:
            if key != 0 and key < num_boxes and key not in unlocked_boxes:
                j = key
                break
        if oldi != j:
            continue
        else:
            break

    for j in range(num_boxes):
        if j not in unlocked_boxes and j != 0:
            return False
    return True
