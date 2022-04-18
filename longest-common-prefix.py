from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ''

    shortest = min(strs)
    longest = max(strs)

    for i, c in enumerate(shortest):
        for _ in longest:
            if c != longest[i]:
                return shortest[:i]

    return shortest
