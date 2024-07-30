import re
from medium import mquestion8


# 1. Write a program that finds the prime factors of a given number using a for loop. A prime factor is a prime number 
# that divides another number exactly without leaving a remainder, e.g. the prime factors of `12` are `2` and `3`.
# 2. Write a program that calculates the `n`th term of the Fibonacci sequence using a while loop.
# 3. Write a program that checks if a given string is an anagram using a for loop.
# 4. Write a program that prints the first `n` terms of the arithmetic sequence using a while loop. An arithmetic sequence 
# is a sequence of numbers in which each term after the first is found by adding a fixed, non-zero number called the common difference to the previous term, e.g. `2, 4, 6, 8, 10, 12, 14, 16, 18, 20, ...`, where the common difference is `2`.
# 5. Write a program that finds the median of a given list of numbers using a for loop. The median is the middle value of a 
# list of numbers when they are sorted in ascending order. If the list has an odd number of elements, the median is the 
# middle element. If the list has an even number of elements, the median is the average of the two middle elements.
# 6. Write a program that checks if a given number is a perfect number using a while loop. A perfect number is a positive integer 
# that is equal to the sum of its proper divisors, excluding itself, e.g. `6` is a perfect number because `1 + 2 + 3 = 6`.
# 7. Write a program that prints the sum of all digits in a given number using a for loop. For example, 
# the sum of the digits in `12345` is `1 + 2 + 3 + 4 + 5 = 15`.
# 8. Write a program that finds the longest word in a given sentence using a while loop.
def question8():
    """
    Could easily do this using the sort() function with regular expression split() function 
    but this asks us to use a while loop.
    doesn't work
    """
    sentence = input("Enter a sentence: ")
    list_of_words = re.split(r"[ :,.!?;]\s*", sentence)
    count = 0
    length_of_longest_word = 0
    word_or_words = {}
    only_one_longest_word = True
    while count <= len(list_of_words):
        length_of_word = len(list_of_words[count]) #why is this giving an error?
        word = list_of_words[count]
        if length_of_word > length_of_longest_word:
            word_or_words = {} #replaces existing dictionary with an empty dictionary
            word_or_words[word] = length_of_word #enters the key (word) and value (length of word) into empty dictionary
            count += 1
            length_of_longest_word = length_of_word
        elif length_of_word == length_of_longest_word:
            word_or_words[word] = length_of_word
            count += 1
            only_one_longest_word = False
        else:
            count += 1
    if only_one_longest_word is True:
        key = (word_or_words.keys())[0]
        value = (word_or_words.values())[0]
        print(f"Your longest word, {key}, is {value} characters long")
    else:
        print("There are multiple words with the highest number of characters in your sentence.\nHere they are:")
        count = 0
        word_or_words = list(word_or_words.items())

        while count <= len(word_or_words):
            print(f"{word_or_words[count][0]}: {word_or_words[count][1]} characters")

question8()



# 9. Write a program that checks if a given string is a pangram using a for loop. A pangram is a sentence 
# that contains every letter of the alphabet at least once, e.g. `The quick brown fox jumps over the lazy dog`.
# 10. Write a program that prints the prime numbers between 1 and 1000 using a while loop.

def question10(lower_bound, upper_bound):
    mquestion8(lower_bound, upper_bound)

# question10(1,1000)
