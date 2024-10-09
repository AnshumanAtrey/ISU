#WAP to print first 20 prime numbes 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

count = 0
number = 2
while count < 20:
    if is_prime(number):
        print(number, end=' ')
        count += 1
    number += 1
