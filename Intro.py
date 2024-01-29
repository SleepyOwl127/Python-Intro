first_name = input("Enter your first name: ")
print("Hello, " + first_name + "!")

x = 15
y = "5"
z = x + int(y) # TypeError: can't add an int to a str
print(z)

score = int(input("Enter test score: "))
if score >= 90:
    grade = "A"
    print(grade)
elif score >= 80 and score < 90:
    grade = "B"
    print(grade)
elif score >= 70 and score < 80:
    grade = "C"
    print(grade)
elif score >= 60 and score < 70:
    grade = "D"
    print(grade)
elif score < 60:
    grade = "F" 
    print(grade)

counter = 0
while counter < 5:
    print(counter, end=" ")
    counter += 1
print("\nthe loop ended.")
print(counter)

#1. Create a program that takes a year as input and checks if it
#is a leap year or not
def is_leap_year(year):
    if(year % 4 ==0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
#2. Given a list of integers, find all the even numbers and store
#them in a new list
def is_Even_or_odd(num):
    if(num % 2 == 0):
        return "Even"
    else:
        return "Odd"
number = int(input("Enter number: "))
result = is_Even_or_odd(number)
print("The number is " + result)
#3. Write a Python program to check if a given number is a prime
#number
#4. Create a program that generates the Fibonacci sequence up to a
#given number of terms
#5. Given a list of names, print all names starting with the
#letter 'A'
#6. Implement a program that prints the multiplication table of a
#given number
#7. Write a program that calculates the factorial of a given
#number
#8. Create a loop that prints all prime numbers between 1 and 50
#9. Given a list of words, count the number of words with more
#than five characters
#10. Calculate the sum of digits of a given number
