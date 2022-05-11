"""
Given a string s consisting of some words separated by some number of spaces, 
return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""

import re

# Using ReGex


def length_last_word_1(s: str) -> int:
    strs = re.split('\s+', s)
    print(strs)

    for i in range(1, len(strs)+1):
        last = strs[-i]
        print(-i, last)
        if len(last) > 0:
            return len(last)

    return 0

# One pass


def length_last_word_2(s: str) -> int:
    full_length = len(s)
    slow = -1

    while slow >= -full_length and s[slow] == ' ':
        slow -= 1

    fast = slow

    while fast >= -full_length and s[fast] != ' ':
        fast -= 1

    return slow - fast


print(length_last_word_2('hello allo   a    '))
