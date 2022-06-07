def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    empty_string = ''



    for char in phrase:
        if char.lower == to_swap.lower:
            print(char,char.isupper())
            if char.isupper():
                empty_string += char.lower()
            else:
                empty_string += char.upper()
        else:
            empty_string += char

    return empty_string


