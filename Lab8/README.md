### Lab 8: File Handling, Classes and Inheritance.
### Instructions:

In today’s lab, you will read a file and calculate each letter’s frequency in a file. Letters frequency means, how many times that letter appeared in the text. You will write a Python code.

1. Create an abstract class with one class attribute/member called “address”. This will hold the file address that is given to you. In “_init_” method, you will pass this as a parameter. Also, you need to have an abstract method called “calculateFreqs”. You will override this method in subclasses.

2. Create 2 subclasses: ListCount and DictCount.

3. In ListCount, override the “calculateFreqs” method. It will read the file using its address given in “_init_” and store each letter in a list. Your task is to make this method calculate the frequency of each unique letter in the file. Append the frequencies of the letter at the end of them. Print the resulting list.

```
Example: 
              List -> a         Resulting List -> a = 157
                      b                           b = 185
                      ...                         ...
```


4. In DictCount, override the “calculateFreqs” method. It will read the file using its address given in “_init_” and store each letter in a dictionary with a value 0 initially. Your task is to make this method calculate the frequency of each unique letter in the file. Update values of the letters with their calculated frequencies. Print the resulting dictionary.

```
Example: 
              Dict -> “a” 0        Updated Dict -> “a” 157
                      “b” 0                        "b" = 185
                      ...                          ...
```

5. In your script, create an object from each subclass and call the methods to test your script.
