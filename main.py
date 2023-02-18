# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []

    for i in range(len(text)):
        char = text[i]

        if char in "([{":
            opening_brackets_stack.append(Bracket(char, i))
        elif char in ")]}":
            if not opening_brackets_stack:
                return i
            top = opening_brackets_stack.pop()
            if not are_matching(top.char, char):
                return top.position

    if opening_brackets_stack:
        return opening_brackets_stack[0].position

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
