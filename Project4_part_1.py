#  Task_one
num = [1, 2, 3, 7, 4, 5, 10, 21, 15]

def checking_numbers(list_of_numbers):  # блок проверки и присвоения четности
    if(list_of_numbers % 2) == 0:
        return True
    else:
        return False
even_numbers = filter(checking_numbers, num)

def checking_numbers(list_of_numbers):  # блок проверки и присвоения нечетности
    if (list_of_numbers % 2) == 0:
        return True
    else:
        return False
odd_numbers = filter(checking_numbers, num)

print("Even numbers: ", list(even_numbers))
print("Odd numbers: ", list(odd_numbers))
print("\n")


#  Task_two
num = [1, 2, 3, 7, 4, 5, 10, 21, 15]

line = list(map(str, num))

print(line)
print("\n")


# Task_three
words =["Dad", "level", "Madam", "Bike", "list", "rotor", "Home"]

def palindrome(word):
    if word.upper() == word[::-1].upper():
        return True
    else:
        return False

palindromes = filter(palindrome, words)
print(list(palindromes))
print("\n")


#  Task_five
dictionary = {1: 'Alex', 2: 'Nika', 3: 'Anna', 4: 'Petya'}
a = dictionary[1]
b = dictionary[3]
dictionary[3] = a
dictionary[1] = b
a = dictionary[2]
b = dictionary[4]
dictionary[4] = a
dictionary[2] = b
print(dictionary)
print("\n")


#  Task_six
n = int(input("Set n:"))

fact = 1   #  Без рекурсии
while n > 1:
    fact = fact * n
    n = n - 1

print(fact)
print("\n")

n = int(input("Set n:"))

def fact_rek(n):   # Через рекурсию
    if (n <= 1):
        return 1
    else:
        return (fact_rek(n-1) * n)

print(fact_rek(n))
print("\n")


# Task_seven
import random

def game():
    number = random.randint(0, 10)
    guess = 0
    print("Guess a number from 0-10:")
    while number != guess:
        try:
            guess = int(input(""))
            if number != guess:
                print("You haven't guessed the number, keep trying and enter the number: ")
            else:
                print("You guessed it!")
                break
        except ValueError:
            print("Please enter an integer")

game()

choose = input("Would you like to play again? y or n\n")
while choose == "y":
    game()
    choose = input("Would you like to play again? y or n\n")
    if choose == "n":
        break
