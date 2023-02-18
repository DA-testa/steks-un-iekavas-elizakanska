# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
   
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))

        elif next in ")]}":
            # Tukšs steks, nav jēga tālāk skatīties
            if not opening_brackets_stack:
                return i
            top = opening_brackets_stack.pop()
            # Pārbauda vai aizverošā iekava sakrīt ar atverošo iekavu
            if not are_matching(top.char, next):
                return i
     
    # Ja steks vēl nav tukšs, tad beigas ir neaizvērtas iekavas
    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    
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
