# LEFOWIET
"""
IN: 'abcd', 'dabc'
OUT: True (1 rotation clockwise)

str1 = abcdefg
str2 = 
rotations = 
"""


def is_string_rotation(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False

    return str1 in str2 * 2


assert is_string_rotation('abcd', 'dabc')

assert not is_string_rotation('abcd', 'dabcc')

assert not is_string_rotation('', 'abcd')

assert is_string_rotation('', '')

assert not is_string_rotation('abab', 'ab')
