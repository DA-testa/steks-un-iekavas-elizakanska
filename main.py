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
    input_type = input("Enter 'F' for File or 'I' for import: ")
    
    if input_type.upper() == 'F':
        file_name = input("File name: ")
        try:
            with open(file_name, 'r') as file:
                text = file.read().strip()
        except FileNotFoundError:
            print("Error: file not found.")
            return
    elif input_type.upper() == 'I':
        text = input("Enter brackets: ")
    else:
        print("Invalid input type.")
        return
    
    
    mismatch = find_mismatch(text)
    # ja nav bijusi kļūme, tās pozīcija būs negatīva (ārpus teksta robežām)
    if mismatch == -1:
        print("Success")
    else:
        print(mismatch + 1)


if __name__ == "__main__":
    main()
