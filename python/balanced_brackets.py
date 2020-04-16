def balancedBrackets(string):
    brackets_dict = {'{': '}', '[': ']', '(':')', '|':'|'}
    open_brackets =['{', '[', '(']
    brackets = []
    stack = []

    # Extract all the brackets from the string
    for char in string:
        if char in brackets_dict or char in brackets_dict.values():
            brackets.append(char)
    # Loop through the brackets
    for i, c in enumerate(brackets):
        # Check for consecutive pipes (|)
        # if the pipe isn't in the stack, push it onto the stack
        if c == '|' and '|' not in stack:
            stack.append(c)
        # else, check if the the char is an open brackets
        elif c in open_brackets:
            # push it onto the stack
            stack.append(c)
        # If it's a closing bracket
        else:
            # pop the last open bracket off the stack
            last = stack.pop()
            # Check if the value of the last open bracket in the brackets_dict is equal to the closing bracket
            # Example if c = }, if the last item in the stack is {, then
            # brackets_dict['{'] should be equal to c = }
            if c != brackets_dict[last]:
                # The brackets are not balanced
                return False
    # If the stack is not empty, then the brackets are not balanced
    if len(stack) != 0:
        return False
    # The brackets are balanced
    return True


if __name__ == '__main__':
    print(balancedBrackets('{{||[||]||}}'))