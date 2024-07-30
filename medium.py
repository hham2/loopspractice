import re

# 1. Write a program that finds the largest element in a given list using a for loop.
def question1():
    x = ["yes","no","yesyes","nono", "Eeeeeeeeeeeeeeeeeeeee"]
    sorted_list = sorted(x, key = len)
    for i in sorted_list:
        if sorted_list[sorted_list.index(i)] != sorted_list[-1]:
            continue
        else:
            print(sorted_list[-1])

# 2. Write a program that calculates the average of a list of numbers using a while loop. You are not allowed to use the built-in `sum()` function.

def question2():
    list_of_numbers = []
    looping = True
    print(r"Welcome to the average number calculator. Input 'stop' to stop inputting numbers")
    while looping:
        response = input("Input a number: ")
        if response == "stop":
            looping = False
        try:
            response = float(response)
            list_of_numbers.append(response)
        except ValueError:
            print("Please enter a valid response.")
            continue  
    the_sum = 0
    for number in list_of_numbers:
        the_sum += number
    average = the_sum / len(list_of_numbers)
    print(f"The average value of the numbers you inputted is {average:.2f}")

# question2()

# 3. Write a program that checks if a given string is a palindrome using a for loop.
# A palindrome is a word, phrase, number, or other sequence of characters
# that reads the same forward and backward, e.g. `radar`, `level`, `12321`

def question3():
    # word = input("Enter a word: ")
    # counter = 0
    # for i in word:
    #     if i == word[word.index(i)]:
    #         counter += 1
    # if counter == len(word):
    #     print(f"{word} is a palindrome")
    word = input("Enter a word: ")
    if word == word[::-1]:
        print(f"{word} is a palindrome.")
    else:
        print(f"{word} is not a palindrome.")
    #wtf was I thinking this is so easy. I'll blame it on getting <5 hours of sleep but that's embarrassing. 

# 4. Write a program that prints the first _n_ terms of the geometric sequence using a while loop. 
# A geometric sequence is a sequence of numbers in which each term after the first is found by multiplying 
# the previous term by a fixed, non-zero number called the common ratio, e.g. `2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, ...`, 
# where the common ratio is `2`.

def question4forloop(a, n, r):
    """
    :param a the first term of the sequence
    :param n the number of terms in the sequence
    :param r the common ratio of the sequence
    """
    first_term = int(a)
    number_of_terms = int(n)
    common_ratio = int(r)
    sequence = []
    for n in range(number_of_terms):
        term = first_term * (common_ratio ** n)
        sequence.append(term)
    print(f"The first {number_of_terms} terms of the geometric sequence is:\n{sequence}")

def question4whileloop(a, n, r):
    """
    :param a the first term of the sequence
    :param n the number of terms in the sequence
    :param r the common ratio of the sequence
    """
    first_term = int(a)
    number_of_terms = int(n)
    common_ratio = int(r)
    sequence = []
    count = 0
    while count < number_of_terms:
        term = first_term * (common_ratio ** count)
        sequence.append(term)
        count += 1
    print(f"The first {number_of_terms} terms of the geometric sequence is:\n{sequence}")

# question4forloop(1,10,2)
# question4whileloop(1,10,2)

# 5. Write a program that finds the second largest element in a given list using a for loop.

def question5():
    x = ["yes","no","yesyes","nono"]
    sorted_list = sorted(x, key = len)
    for i in sorted_list:
        if sorted_list[sorted_list.index(i)] != sorted_list[-2]:
            continue
        else:
            print(sorted_list[-2])

# 6. Write a program that calculates the factorial of a given number using a while loop.

def question6():
    number = int(input("Input a number: "))
    factorial = 1
    while number > 1:
        factorial = factorial * number
        number -= 1
    print(factorial)

# 7. Write a program that checks if a given number is a perfect square using a for loop. A perfect square is a number that can be expressed as the 
# product of two equal integers, e.g. `1`, `4`, `9`, `16`, `25`, `36`, `49`, `64`, `81`, `100`, ...

def question7(n):
    length = [1]
    sqrt = 0
    validity = "is not"
    for i in length:
        if (n / i) == i:
            validity = "is"
            sqrt = i
        else:
            if length[-1] > n:
                break
            else:
                length.append(i + 1)
    if sqrt == 0:
        print(f"{n} {validity} a perfect square.")
    else:
        print(f"{n} {validity} a perfect square and its square root is {sqrt}.")

# question7(1296)

# 8. Write a program that prints the sum of all prime numbers between 1 and 100 using a while loop.
def mquestion8(lower_bound, upper_bound):
    """
    :param lower_bound the lower bound of the range in which you want all prime numbers to be summed, inclusive
    :param upper_bound the upper bound of the range in which you want all prime numbers to be summed, inclusive
    """
    primes = []
    iterations_thus_far = [1]
    num = lower_bound
    while num <= upper_bound:
        valid_options = [1, num]
        evenly_divisible_numbers = []
        for i in iterations_thus_far:
            if num % i == 0:
                evenly_divisible_numbers.append(i)
        if evenly_divisible_numbers == valid_options:
            primes.append(num)
        num += 1
        iterations_thus_far.append(num)
    count = 0
    the_sum = 0
    while count < len(primes):
        the_sum += primes[count]
        count += 1
    print(f"The sum of all prime numbers between {lower_bound} and {upper_bound} is {the_sum}.")

# question8(1,100)
        

    # previous attempt:
    # primes = []
    # up_to_i = [1]
    # for i in range(lower_bound, upper_bound + 1):
    #     valid_options = [1, i]
    #     temp_valid_options = []
    #     up_to_i.append(i)
    #     for number in up_to_i:
    #         if i % number == 0:
    #             temp_valid_options.append(number)
    #         else:
    #             continue
    #     if temp_valid_options == valid_options:
    #         primes.append(i)
    # print(primes)
    #not working; will come back to this later

# question8(1,100)

# 9. Write a program that counts the number of words in a given sentence using a for loop. Words can be separated by 
# spaces, commas, periods, exclamation marks, question marks, etc. You may be interested in the built-in `split()` function, 
# which splits a string into a list of words based on a delimiter. The delimiter is a space by default, but you can specify a 
# different delimiter, e.g. `split(',')`, `split('.')`, `split('!')`, `split('?')`, etc. You can even specify multiple delimiters, e.g. `split(',.!?')`.

def question9():
    print("This program counts the number of words in a sentence. Please do not end your sentence with more than one punctuation character.")
    sentence = input("Input a sentence: ")
    if sentence[-1] in [".","!","?",";","-",":"]:
        list_of_words = (re.split(r"[ :,.!?;]\s*", sentence))[:-1]
    else:
        list_of_words = re.split(r"[ :,.!?;]\s*", sentence)
    number_of_words = len(list_of_words)
    print(f"There are {number_of_words} words in your sentence.")

# question9()

# 10. Write a program that prints the common elements between two lists using a while loop.

def question10():
    list1 = ["yes", "no", "yesyes", "nono"]
    list2 = ["nah", "no", "nope", "nono"]
    common_list = []
    for i in list1: 
        if i in list2:
            common_list.append(i)
        else:
            continue
    if not common_list:
        print("There are no common terms between these two lists.")
    else:
        print(common_list)

