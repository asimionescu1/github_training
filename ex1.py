

def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        return "Nasol"
    elif n == 0:
        return 0
        print("draguta treaba")
    elif n == 1:
        return b
    else:
        for c in range(1,n):
            c = a + b
            a = b
            b = c
        
        return b


print (fibonacci(6))

def sum_fib(n):
    sum = 0
    for i in range(n):
        print(fibonacci(i))
        sum = sum + fibonacci(i)
    return sum
print("Sum:")
print(sum_fib(0))

def avg_fib(n):
    if n == 0:
        return 0
    else:
        return sum_fib(n)/ n

print("Avg:")
print(avg_fib(0))

print("Buna")
print("Buna")
print("Buna")
print("Buna")
print("Buna")
print("Buna")
print("Buna")
print("Buna")
print("Buna")
print("Buna")
print("Buna")
print("Buna")
print("Buna")
    
print("Yaya")
print("yaya")
    
print("yaya")