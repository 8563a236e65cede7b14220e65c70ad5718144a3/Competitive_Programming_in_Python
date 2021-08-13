"""
This module groups the code for Chapter 2 of Competitive Python Programming. These deal with text related algorithms.
"""


def anagrams(S: set[str]) -> list[list[str]]:
    """
    Finds all anagrams of words contained within an input set of words.

    :param set[str] S: The set of words to find anagrams within.
    :return: A list of lists of anagrams.
    """
    # Create a dictionary that associates a word's signature to an array
    # containing all words with that signature.
    d: dict[str, list[str]] = {}

    # Declare the iterator.
    word: str

    # For each word in the set of words.
    for word in S:
        # Calculate its signature. This is just each character sorted in alphabetical order as a single string.
        s: str = "".join(sorted(word))

        # If the signature has been encountered already
        if s in d:
            # Append the latest anagram to the list of anagrams with the same signature.
            d[s].append(word)
        # Otherwise this is the first occurrence of the signature.
        else:
            # Initialize the dictionary value with an array consisting of the word.
            d[s] = [word]

    # Return the lists of words for signatures that had more than one entry.
    return [d[s] for s in d if len(d[s]) > 1]
