# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    stack = []
    for i in range(len(text)):
        if text[i] in "([{":
            stack.append((text[i], i))
        elif text[i] in ")]}":
            if not stack:
                return i
            top = stack.pop()
            if not ((top[0] == '(' and text[i] == ')') or
                    (top[0] == '[' and text[i] == ']') or
                    (top[0] == '{' and text[i] == '}')):
                return i
    if stack:
        return stack[0][1]
    return -1

def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch == -1:
        print("Success")
    else:
        print(mismatch + 1)


if __name__ == "__main__":
    main()
