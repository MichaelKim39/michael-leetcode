"""
Given a string s consisting of some words separated by some number of spaces, 
return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""

import re


def length_last_word(s: str) -> int:
    strs = re.split('\s+', s)
    print(strs)

    for i in range(1, len(strs)+1):
        last = strs[-i]
        print(-i, last)
        if len(last) > 0:
            return len(last)

    return 0


print(length_last_word('hello allo   a    '))
