#!/usr/bin/python3
"""text indentation function"""


def text_indentation(text):
    """text indeintation"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    start = 0
    for idx, val in enumerate(text):
        if val in '?:.':
            print(text[start:idx + 1].strip() + '\n')
            start = idx + 1
    if not start:
        print(text, end='')
    elif start is not len(text):
        print(text[start:idx + 1].strip(), end='')
