################ 29. Find the sum of all even numbers between 1 to n ################
n = int(input("Enter the value of n: "))

sum_even = 0
for i in range(2, n+1, 2):
    sum_even += i
print("The sum of all even numbers between 1 and", n, "is:", sum_even)