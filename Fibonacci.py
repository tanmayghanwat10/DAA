#Recursion
'''def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n-1) + recur_fibo(n-2)

# Taking user input
nterms = int(input("Enter the number of terms for the Fibonacci sequence: "))

# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibo(i))'''
        
def recursive_fibonacci(n, a=0, b=1):
    if n == 0:
        return []
    elif n == 1:
        return [a]
    else:
        return [a] + recursive_fibonacci(n-1, b, a+b)

# Taking user input for the length of the series
length = int(input("Enter the length of the Fibonacci series: "))

# Printing the Fibonacci series
result = recursive_fibonacci(length)
print("Fibonacci series:", result)


