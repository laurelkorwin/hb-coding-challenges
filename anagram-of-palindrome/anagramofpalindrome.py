from collections import defaultdict


def is_anagram_of_palindrome(word):

    """A palindrome is a word that reads the same forward and backwards
    (eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
    (eg for "racecar", you could rescramble this as "arceace").

    Determine if the given word is a re-scrambling of a palindrome.
    The word will only contain lowercase letters, a-z.

    Examples::

        >>> is_anagram_of_palindrome("a")
        True

        >>> is_anagram_of_palindrome("ab")
        False

        >>> is_anagram_of_palindrome("aab")
        True

        >>> is_anagram_of_palindrome("arceace")
        True

        >>> is_anagram_of_palindrome("arceaceb")
        False

    """

    my_dict = defaultdict(int)

    for s in word:
        my_dict[s] += 1

    if len(word) % 2 == 0:
        for value in my_dict.values():
            if value % 2 != 0:
                return False

    elif len(word) % 2 != 0:
        odds = 0
        for key, value in my_dict.items():
            if value % 2 != 0 and not key.isspace():
                odds += 1
        if odds > 1:
            return False

    return True

if __name__ == '__main__':
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"
