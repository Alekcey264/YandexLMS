def brackets(text):
    stack = []
    for letter in text:
        if letter == "(":
            stack.append(letter)
        elif letter == ")":
            if not stack or stack.pop() != "(":
                return False
    return not stack

