def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    # case sensitive!
    # comprehension!!!!!!!

    freqs = {}

    for char in phrase:
        curr = freqs[char] or 0
        freqs[char] = curr + 1
    
    return freqs