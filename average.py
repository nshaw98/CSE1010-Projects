# This program averages a set amount of numbers.

avg = 0
print("How many numbers are to be averaged?")
num = int(input())
sum = 0
for i in range(1, num+1):
        sum = sum + i

avg = sum / num

print(avg)
