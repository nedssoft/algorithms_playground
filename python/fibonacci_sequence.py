def fibonacci_sequence(n):
    
    if n == 0:
        print(n)
        return []
    if n == 1:
        return [0]
    a,b = 0,1
    sequence = [a,b]
    if (n == 2):
        return sequence
    
    while n > len(sequence):
        a,b = b,a+b
        sequence.append(b)
    return sequence


if __name__ == '__main__':
    print(fibonacci_sequence(8))
