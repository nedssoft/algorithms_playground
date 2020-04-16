function balancedBrackets(string) {
    // store openers and closers in sets for fast access
    const openers = new Set(["(", "[", "{"]);
    const closers = new Set([")", "]", "}"]);
    const pairs = {"(":")", "{":"}", "[":"]"};
    
    // use a stack for LIFO ordering
    // this allows us to check if the brackets adhere to a palindromic ordering
    const stack = [];
    
    // boolean to keep track of whether we currently have an open pipe or not
    let openPipe = false;
      
    for (let i = 0; i < string.length; i++) {
      const char = string[i];
      if (char === "|") {
        openPipe = openPipe ? "NO" : "YES";
      } else if (openers.has(char)) {
        stack.push(char);
      } else if (closers.has(char)) {
      
        // upon encountering a closer, we have a few things to check 
        // 1. if our stack is empty, that means that there is no opener 
        // associated with this closer 
        // 2. does the top opener's type match our closer?
        // 3. is there currently an open pipe?
        if (!stack.length || pairs[stack.pop()] !== char || openPipe) {
          return "NO";
        }
      }
    }
    let retVal = ""
    // after we've walked throughout the entire string, we want to check
    // that our stack is empty and that there are no open pipes
    if (stack.length === 0 && !openPipe) {
        retVal = "YES"
    } else {
        retVal = "NO"
    }
    return retVal
  }