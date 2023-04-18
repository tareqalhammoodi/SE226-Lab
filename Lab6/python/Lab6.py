#SE226 – LAB#6
import math

#Task 1
while True:
    # get input from user
    n = int(input("Enter a positive value of n : "))
    x = int(input("Enter a positive value of x : "))
    # check if the inputs are valid
    if x < 0:
        print("Invalid number, x can not be a negative number. Try again!")
    else:
        result = sum(list(map(lambda i: (n ** i) / math.factorial(i), range(x + 1))))
        print("The result is : ", result)
        break

print()

#Task 2
result = 0
def SUM(n):
    global result
    if n != 0:
        result += (-1) ** (n + 1) / n
        SUM(n - 1)

while True:
    N = int(input("Enter a value of n : "))
    if N < 1:
        print("Invalid number, n should be greater or equal to 1 , Try again!")
    else:
        SUM(N)
        print("The result is : ", result)
        break

