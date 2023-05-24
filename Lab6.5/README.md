### Lab 6.5: Understanding functions and data structures.
### Instructions:

1. Write a Python function that takes two lists of integers as input and returns a new list with only the elements that appear in both lists.
2. Write a Python function that takes a list of strings as input and returns a new list with only the strings that are palindromes.
3. Write a Python function that takes a list of integers as input and returns a new list with the prime numbers in the original list. The function should use the “Sieve of Eratosthenes” algorithm to generate the list of primes from the original list.

Hint: Instead of marking the “not primes” remove them from the list on each run.

4. Write a Python function called anagrams(word, word_list) that takes a string word and a list of strings word_list as input and returns a new list with only the strings from word_list that are anagrams of word. An anagram is a word or phrase formed by rearranging the letters of another word or phrase, such as "cinema" and "iceman". Your function should use the following approach:
- Convert the input word word into a sorted list of characters.
- Iterate over the strings in word_list and for each string:
  - Convert the string into a sorted list of characters.
  - Compare the sorted list of characters to the sorted list of characters for word.
  - If the two lists are equal, the string is an anagram of word and should be added to the output list.
- Return the output list of anagrams.

For example, if word is "listen" and word_list is ["enlists", "google", "inlets", "banana"], your function should return ["enlists", "inlets"]. Note that the input strings may contain spaces and should be treated as case-insensitive.

5. Do the tasks 1 to 4 again in C++.
