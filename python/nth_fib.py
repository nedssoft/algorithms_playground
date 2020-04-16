def fibonacci_sequence(n, a=0,b=1):
    
    if n == 0:
        return 
    if n == 1:
        return 0
    if (n == 2):
        return b
    
    a,b = b,a+b
    if a >= n:
        return b
    return fibonacci_sequence(n,a,b)

if __name__ == '__main__':
    print(fibonacci_sequence(8))