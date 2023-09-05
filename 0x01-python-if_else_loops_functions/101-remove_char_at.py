#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n > len(str):
        return str
    result = ''
    for i, v in enumerate(str):
        if i != n:
            result += v
    return result
