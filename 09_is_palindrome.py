import string

def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    # case sensitve
    # remove spaces
        # split into arrays by " "
        # join back into a single string
        # " ".join(phrase)

    LETTERS = string.ascii_lowercase

    # check if char is contained in LETTERS
    
    lowercase = phrase.lower()

    letters = [char for char in lowercase if char in LETTERS]

    reverse_letters = letters.copy()

    reverse_letters.reverse()

    # print ("letters =", letters, "reverse_letters =", reverse_letters)

    if letters == reverse_letters:
        return True

    return False