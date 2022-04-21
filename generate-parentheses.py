"""
LEFOWIT
Q - https://leetcode.com/problems/generate-parentheses/
A - https://leetcode.com/problems/generate-parentheses/discuss/10110/Simple-Python-DFS-solution-with-explanation 

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

n is between 1 and 8
"""

from typing import List


def generate_parentheses(n: int) -> List[str]:
    left, right = n, n
    ans = []
    dfs(left, right, ans, "")
    return ans


def dfs(left, right, ans, s):
    if right < left:
        return
    if not left and not right:
        ans.append(s)
        return
    if left:
        dfs(left-1, right, ans, s+'(')
    if right:
        dfs(left, right-1, ans, s+')')


print(generate_parentheses(4))
