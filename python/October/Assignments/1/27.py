num = int(input("Enter a number: "))
order = len(str(num))
sum_of_powers = 0
for digit in str(num):
    sum_of_powers += int(digit) ** order

if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

