from collections import namedtuple # nametupled 사용

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    is_over  = True
    position = 0

    for i, next in enumerate(text):

        if next in "([{": # Process opening bracket
            opening_brackets_stack.append(Bracket(next, i))

        elif next in ")]}": # Process closing bracket
            closing_top_back  = next
            if opening_brackets_stack != []:
                opening_top_front = opening_brackets_stack.pop().char

                if not are_matching(opening_top_front, closing_top_back):
                    print(i+1)
                    is_over = False
                    break
            else:
                print(i+1)
                is_over = False
                break
            
    if is_over:
        if len(opening_brackets_stack) != 0:
            print(opening_brackets_stack[0].position +1)
        else:
            print("Success")

def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer


if __name__ == "__main__":
    main()
