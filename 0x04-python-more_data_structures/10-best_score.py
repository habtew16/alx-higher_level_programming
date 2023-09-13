#!/usr/bin/python3
def best_score(a_dictionary):
    a = {}
    m = 0
    if a_dictionary:
        for key, val in a_dictionary.items():
            if val > m:
                m = val
            else:
                continue
        if m != 0:
            for key, val in a_dictionary.items():
                if m == val:
                    a[key] = m
                if a:
                    break
        return a
    else:
        return None
