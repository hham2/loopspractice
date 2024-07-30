# 1. Write a program that prints the numbers from 1 to 10 using a for loop.
def question1(lower_bound, upper_bound):
    for number in range (lower_bound, upper_bound + 1):
        print(number)

# question1(1,10)

# 2. Write a program that prints the even numbers from 1 to 20 using a while loop.
def question2(lower_bound, upper_bound):
    count = lower_bound
    even_numbers = []
    while count <= upper_bound:
        if (count % 2) == 0:
            even_numbers.append(count)
            count += 1
        else:
            count += 1
    print(even_numbers)

# question2(1,20)


# 3. Write a program that calculates the sum of all numbers from 1 to 100 using a for loop.
# def question3whileloop(lower_bound, upper_bound):
#     count = lower_bound
#     the_sum = 0
#     while count <= upper_bound:
#         the_sum += count
#         count += 1
#     return the_sum

def question3forloop(lower_bound, upper_bound):
    the_sum = 0
    for number in range(lower_bound, upper_bound + 1):
        the_sum += number
    return the_sum


# print(question3whileloop(1,100))
# print(question3forloop(1,100))

# 4. Write a program that prints the first 10 multiples of 3 using a while loop.
def question4(given_integer):
    given_integer = int(given_integer)
    multiples = []
    count = 1
    number = 1
    while count <= 10:
        if (number % given_integer) == 0:
            count += 1
            multiples.append(number)
            number += 1
        else:
            number += 1
    print(multiples)
    #originally "number" wasn't being added to because it was a temporary variable within the while loop
    #instead of a variable that remained constant across iterations unless changed within the while loop

# question4(3)

# 5. Write a program that prints the factorial of a given number using a for loop. 
# The factorial of a number is the product of all positive integers less than or equal to that number, e.g. `5! = 5 * 4 * 3 * 2 * 1 = 120`.
def question5(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial = factorial * i
    print(factorial)

# 6. Write a program that prints the Fibonacci sequence up to a given number using a while loop. The Fibonacci sequence 
# is a series of numbers in which each number is the sum of the two preceding ones, starting from 0 and 1, e.g. `0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...`.
def question6(max):
    n1 = 0
    n2 = 1
    x = 0
    while x < max:
        x = n1 + n2
    print(x)
    

# question6(10)

# 7. Write a program that counts the number of vowels in a given string using a for loop. The vowel letters are `a`, `e`, `i`, `o`, and `u`.
def question7():
    """ 
    Write a program that counts the number of vowels in a given string 
    using a for loop. The vowel letters are `a`, `e`, `i`, `o`, and `u`.
    """
    word = input("Enter a word: ")
    counter = 0
    for i in word:
        if i in ["a","e","i","o","u"]:
            counter += 1
        else:
            continue
    print(f"The number of vowels in your word is {counter}!")

# 8. Write a program that checks if a given number is prime using a while loop. 
# A prime number is a number greater than `1` that is only evenly divisible by `1` and itself.

def question8(n):
    number = int(n)
    is_prime = conditions(number)
    if is_prime is True:
        print(f"{number} is prime.")
    else:
        print(f"{number} is not prime.")

def conditions(n):
    """
    Checks if the parameter n is prime
    """
    count = 1
    acceptable_numbers = [1, n]
    evenly_divisible_numbers = []
    while count <= n:
        result = n % count
        if result == 0:
            evenly_divisible_numbers.append(count)
            count += 1
        else:
            count += 1
    if evenly_divisible_numbers == acceptable_numbers:
        return True
    else:
        return False
    #I gave up on this one for a bit but randomly had a brief vision of how to
    #approach this and was able to do it without copying an online solution, so I'm glad

# question8(11)

# 9. Write a program that prints the ASCII values of all uppercase letters using a for loop. 
# You may use the built-in `ord()` function to convert any character to its ASCII value.
def question9():
    uppercase_letters = [
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N',
        'O','P','Q','R','S','T','U','V','W','X','Y','Z'
    ]
    for i in uppercase_letters:
        ascii = ord(i)
        print(ascii, end=" ")

# question9()

# 10. Write a program that prints the reverse of a given string using a while loop.
def question10():
    word = input("Enter some text: ")
    count = 0
    while count < 1:
        word = word[::-1]
        count += 1
    print(word)

# question10()
