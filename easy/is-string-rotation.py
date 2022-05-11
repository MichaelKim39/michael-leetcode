# LEFOWIET
"""
IN: 'abcd', 'dabc'
OUT: True (1 rotation clockwise)

str1 = abcdefg
str2 = 
rotations = 
"""


def is_string_rotation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    return (s1 in s2*2)


assert is_string_rotation('abcd', 'dabc')

assert not is_string_rotation('abcd', 'dabcc')

assert not is_string_rotation('', 'abcd')

assert is_string_rotation('', '')

assert not is_string_rotation('abab', 'ab')
