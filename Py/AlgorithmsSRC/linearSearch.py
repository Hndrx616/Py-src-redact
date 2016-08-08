'''
author Stephen Hilliard (c) 2015.
developer Stephen Hilliard (c) 2015.
'''
def linear_search(items, desired_item):
    for position, item in enumerate(items):
        if item == desired_item:
            return position

    raise ValueError("%s was not found in the list." % desired_item)