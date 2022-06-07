def intersection(l1, l2):
    """Return intersection of two lists as a new list::

        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]

        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]

        >>> intersection([1, 2, 3], [3, 4])
        [3]

        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    # union,
    # lst to set 1
    # lst2 to set 2
    # return intersection of set1 & set 2

    set1 = set(l1)
    set2 = set(l2)
    return [*(set1 & set2)]
