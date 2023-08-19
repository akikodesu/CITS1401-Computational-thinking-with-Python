#Q1: Write a statement to sum the squares of the variables a, b, c and d, and store the result in variable s
a = 10
b = 12
c = 15
d = 20
# Do not change the code above this line. Write your code below.
s = a ** 2 + b ** 2 + c ** 2 + d ** 2


#Q2: Write a program to print the factorial of variable x.
x = int(input(""))
# Don't change the above line of code. You can assume that x will always be either a positive integer or 0.
def factorial(n):
    sum = 1
    for i in range(1,n+1):
        sum *= i
    return sum
print(factorial(x))


#Q3: Write a program that finds the sum of squares of all numbers between zero and a whole number x that the user enters (x can be positive or negative). 
x = int(input())
# Don't change the above line of code. Add your code after this line. Remember not to print anything other than final answer
sum = 0
if x > 0:
    for i in range(0, x+1):
        sum += i ** 2
else:
    for i in range(x, 1):
        sum += i ** 2
print(sum)


#Q4: Write a program that can add first n positice odd numbers starting from 1 and the number n is entered by the user. The program should only work for positive input data and give zero output for negative data
n = int(input())
# write your program below
if n < 0:
    print(0)
else:
    odd_sum = 0
    start_odd = 1
    for i in range(n):
        odd_sum += start_odd
        start_odd += 2
    print(odd_sum)


#Q5: Write a program to generate Fibonacci Sequence and print the nth number where n is taken as input from the use. For instance, if user inputs 9 then 21 should be printed.
n = int(input())
#Don't change the above line of code. Write your program below this line. Remember to print the final result only.
if n >= 0:
    def fabonacchi(n):
        if n == 0:
            print(0)
        elif n == 1:
            print(1)
        else:
            x = 0
            y = 1
            for i in range(2, n):
                x, y = y, x + y
            print(y)
    result = fabonacchi(n)
else:
    print("this is not a positive number")


#Q6: You already wrote Fibonacci program which you just created in earlier question. Now update it such that it calculates the summation of Fibonacci number with each number too.
n = int(input())
# Don't change the above line. You need to write your code below this line. Remember to print the final value only.
def fibonacci_sum(n):
    if n == 0:
        return 0

    fib_sum = 0
    x, y = 0, 1

    for i in range(n - 1):
        fib_sum += y
        x, y = y, x + y

    return fib_sum

if n < 0:
    print("Please enter a positive integer.")
else:
    result = fibonacci_sum(n)
    print(result)








