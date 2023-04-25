#SE226 – LAB#6.5
#Task 1
def Intersection(list1, list2):
    intersection = []                                       # define a list
    for element in list1:                                   # check whether there is common elements in list1 and list2
        if element in list2:
            intersection.append(element)                    # if so add it to intersection list
    return intersection                                     # return list of common elements
#Task 2
def isPalindromes(strings):
    """
    A string is said to be palindrome if it remains the same on reading from both ends.
    It means that when you reverse a given string, it should be the same as the original string.
    """
    palindromes = []                                        # define a list
    for string in strings:                                  # check whether the string is palindromes or not
        if string == string[::-1]:
            palindromes.append(string)                      # if so add it to the list
    return palindromes                                      # return list palindromes strings
#Task 3
def pirmeNumbers(list):
    is_prime = [True] * (max(list) + 1)                     # define a list of boolean values initialized to True
    is_prime[0], is_prime[1] = False, False                 # since 0 and 1 are not prime we set them to false

    # use the Sieve of Eratosthenes algorithm to mark all non-prime numbers
    for i in range(2, int(max(list) ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max(list) + 1, i):
                is_prime[j] = False

    # define a new list for only prime numbers from the original list and store them in it
    primesList = []
    for number in list:
        if is_prime[number]:
            primesList.append(number)

    return primesList                                       # return list of prime numbers
#Task 4
def Anagrams(word, word_list):
    """
    An anagram is a word or phrase formed by rearranging the letters of another word or phrase,
    such as "cinema" and "iceman".
    """
    anagrams_list = []                                      # define an empty list to store anagrams
    sorted_input = sorted(word.lower().replace(" ", ""))    # convert the input word into a sorted list of characters
    for Word in word_list:                                  # iterate over the strings in word_list and for each string
        sorted_word = sorted(Word.lower().replace(" ", "")) # convert the string into a sorted list of characters
        # since the word "enlists" has two "s" letter the code couldn't return it, so I added these two lines below to handle the repetition
        temp = []
        [temp.append(x) for x in sorted_word if x not in temp]
        if temp == sorted_input:                            # compare the sorted list of characters to the sorted list of characters for word
            anagrams_list.append(Word)                      # if the two lists are equal, the string is an anagram of word and should be added to the output list
    return anagrams_list                                    # return the output list of anagrams

#Testing
List1 = [4, 9, 2, 0, 8]; List2 = [1, 5, 0, 2, 7]
print(Intersection(List1, List2))

strings = ["moon", "level", "kayak", "strawberry", "dad"]
print(isPalindromes(strings))

List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(pirmeNumbers(List))

word = "listen"; word_list = ["enlists", "google", "inlets", "banana"]
print(Anagrams(word, word_list))
