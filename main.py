# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    first_bracket_index = -1

    for i in range(len(text)):
        char = text[i]

        #Kad programma atrod pirmo iekavu, tā piešķir mainīgajam tās vertību, lai tālāk var strādāt tiaki ar iekavu virktni
        if char in "([{":
            if first_bracket_index == -1:
                first_bracket_index = i
            opening_brackets_stack.append(Bracket(char, i))
        elif char in ")]}":
            if not opening_brackets_stack:
                return i
            top = opening_brackets_stack.pop()
            if not are_matching(top.char, char):
                return i

    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    elif first_bracket_index != -1:
        return first_bracket_index
    else:
        return -1



def main():
    text = input()
    #Pirmkārt nosaka, kur jāsāk skaitīt iekavu virkne
    start_index = 0
    while start_index < len(text) and text[start_index] not in "([{":
        start_index += 1
        
    mismatch = find_mismatch(text[start_index:])
    # ja nav bijusi kļūme, tās pozīcija būs negatīva (ārpus teksta robežām)
    if mismatch == -1:
        print("Success")
    else:
        print(mismatch + start_index + 1)


if __name__ == "__main__":
    main()
