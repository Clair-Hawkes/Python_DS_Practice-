def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    # Comprehension
    # We loop over the items for item in list
    # Conditional check either via the item as falsy truthy check or via bool()
    # place item if resolved true

    return [itm for itm in lst if itm]
