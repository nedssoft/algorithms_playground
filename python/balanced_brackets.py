"""
A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].

Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) of the exact same type. 
There are three types of matched pairs of brackets: [], {}, and ().

A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. 
For example, {[(])} is not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a single, 
unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ].

By this logic, we say a sequence of brackets is balanced if the following conditions are met:

It contains no unmatched brackets.
The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
Given  strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, return YES. Otherwise, return NO.
"""


def isBalanced(s):
    brackets_dict = {'{':'}', '[':']', '(':')'}
    opening_brackets = ['{', '(', '[']
    closing_brackets = ['}', ')', ']']

    # use a stack for LIFO ordering
    # this allows us to check if the brackets adhere to a palindromic ordering
    stack = []

    # boolean to keep track of whether we currently have an open pipe or not
    open_pipe = False
    for chr in s:
        if chr == '|':
           open_pipe = False if open_pipe == True  else  True;
        if chr in opening_brackets:
            stack.append(chr)
        elif chr in closing_brackets:
            if not len(stack):
                return 'NO'
            last_opening_bracket = stack.pop()
            if chr != brackets_dict[last_opening_bracket] or open_pipe == True:
                return 'NO'
    #  after we've walked throughout the entire string, we want to check
    #  that our stack is empty and that there are no open pipes
    if len(stack) !=0 and not open_pipe:
        return 'NO'
    return 'YES'


if __name__ == '__main__':
    print(isBalanced('{{||[||]||}}'))