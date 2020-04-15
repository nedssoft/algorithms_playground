const Fib = (n) => {
    let [a, b] = [0, 1]
    if (n == 0) {
      return []
    }
    if (n ==1) {
      return [0]
    }
      
    const sequence = [a, b]
    if (n == 2) {
      return arr
    }
    while (n > sequence.length) {
      [a, b] = [b, a+b]
      sequence.push(b)
    }
    return sequence
    
    
  }
  
  console.log(Fib(4))