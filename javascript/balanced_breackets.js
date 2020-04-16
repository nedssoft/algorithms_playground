function balancedBrackets(string) {
    const splitCharacters = string.split('');
    const characters = splitCharacters.filter(item => ['(', ')', '{', '}', '[', ']', '|'].includes(item))
    let response = []
    let check = {
        '(': ')',
        '[': ']',
        '{': '}',
        '|': '|'
    }
    for(let i=0; i < characters.length; i++ ){
        if (characters[i] == '(' || characters[i] == '[' || characters[i] == '{' || characters[i] == '|') {
            response.push(characters[i])
        } else {
            let lastItem = response.pop();
            console.log(characters[i], check[lastItem])
            console.log(characters[i], check[lastItem])
            if (characters[i] != check[lastItem]) {
                console.log('a')
                return false;
            }
        }
    }

    if (response.length !== 0){ console.log('v')
        return false
    }
    return true
}