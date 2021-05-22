#!/usr/bin/python3
"""Defines a text identation function"""


def text_indentation(text):
    """Indents a text.

    Args:
        text (str): text to evaluate.

    Raises:
        TypeError: if text is not string.
    """
    space = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for character in text:
        if character == '.' or character == '?' or character == ':':
            space = 1
            print("{:s}".format(character))
            print()
        else:
            if space != 1:
                print("{:s}".format(character), end="")
            space = 0
    print()
