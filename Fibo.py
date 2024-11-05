#Non-Recursion
a, b = 0, 1

series_length = int(input("Enter the length of the Fibonacci series: "))

print(a, b, end=' ')
for i in range(series_length - 2):
    c = a + b
    print(c, end=' ')
    a, b = b, c
