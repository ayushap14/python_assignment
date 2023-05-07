def reverse_string_using_stack(string: str) -> str:
    stack = []
    for char in string:
        stack.append(char)
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()
    return reversed_string
