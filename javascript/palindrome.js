const isPalindrome = (s) => {
    if (s.length < 2) {
      return true
    }
    if (s[0] !== s.slice(-1)) {
      return false
    } 
    return isPalindrome(s.slice(1, -1))
  }
  console.log(isPalindrome('abaca')) // false
  console.log(isPalindrome('aba')) // true