function balancedBrackets(string){
    const brackets_pairs = {'{': '}', '[': ']', '(':')', '|':'|'}
    const open_brackets =['{', '[', '(']
    const closing_brackets =['}', ']', ')']
    const brackets = []
    const stack = []

    // Extract all the brackets from the string
    for (let char of string) {
        if (brackets_pairs[char] || (closing_brackets.includes(char))) {
            brackets.push(char)
        }
    }
        
    // Loop through the brackets
    for (let i = 0; i < brackets.length; i++) {
         // Check for consecutive pipes (|)
        // if the pipe isn't in the stack, push it onto the stack
        if (brackets[i] === '|' && !stack.includes('|')) {
            stack.push(brackets[i])
        }
        // else, check if the the char is an open brackets
        else if (open_brackets.includes(brackets[i])) {
            
            // push it onto the stack
            stack.push(brackets[i])
        }
        else {
            // pop the last open bracket off the stack
            const last_open_bracket = stack.pop()
            // Check if the value of the last open bracket in the brackets_pairs is equal to the closing bracket
            // Example if c = }, if the last item in the stack is {, then
            // brackets_pairs['{'] should be equal to c = }
            if (brackets[i] != brackets_pairs[last_open_bracket]) {

                // The brackets are not balanced
                return false
            }
        }

    }

    // If the stack is not empty, then the brackets are not balanced
    if (stack.length != 0)
        return false
    // The brackets are balanced
    return true
        
}

console.log(balancedBrackets('{{||[||]||}}'))