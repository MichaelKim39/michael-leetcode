
def isValid(s: str) -> bool:
    if len(s) <= 1:
        return False

    stack = []
    match = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for c in s:
        if c in '({[':
            stack.append(c)
            print(f'appended {c}')
        if c in ')}]':
            popped = stack.pop()
            print(f'matched {c}')
            if popped != match[c]:
                return False

    if stack:
        return False
    return True


print(isValid('({}[])'))
