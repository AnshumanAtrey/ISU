sum1, sum2 = 0, 0
count1, count2 = 0, 0

for i in range(1, 61):
    if 5 <= i <= 15:
        sum1 += i
        count1 += 1
    elif 21 <= i <= 60:
        sum2 += i
        count2 += 1
    else:
        pass

average1 = sum1 / count1 if count1 > 0 else 0
average2 = sum2 / count2 if count2 > 0 else 0

print("Average from 5 to 15 is:", average1)
print("Average from 21 to 60 is:", average2)

