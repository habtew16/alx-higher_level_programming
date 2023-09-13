#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    count = 0
    i = 0
    if(roman_string and isinstance(roman_string, str)):
        while i < len(roman_string):
            c = roman_string[i]

            if i < len(roman_string) - 1 and dic[c] < dic[roman_string[i + 1]]:
                count += dic[roman_string[i + 1]] - dic[c]
                i += 2
            else:
                count += dic[c]
                i += 1
        return count
    else:
        return 0
