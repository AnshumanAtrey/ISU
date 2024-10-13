n = int(input("Enter the number of terms: "))
fibonacci_series = []
f1, f2 = 0, 1

for i in range(n):
    fibonacci_series.append(f1)
    f1, f2 = f2, f1 + f2

print("Fibonacci series:", fibonacci_series)

