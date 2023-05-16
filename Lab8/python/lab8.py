from abc import ABC, abstractmethod

""" creating an abstract class with one class member called address and abstract method called calculateFreqs """
class FrequencyCounter(ABC):
    address = ""

    def __init__(self, address):
        self.address = address

    @abstractmethod
    def calculateFreqs(self):
        pass

""" creating ListCount subclasses that override the “calculateFreqs” method and read the file using its address 
    given in “_init_” and store each letter in a list. Also the method calculate the frequency of each unique 
    letter in the file. Append the frequencies of the letter at the end of them. Print the resulting list.          """
class ListCount(FrequencyCounter):
    def calculateFreqs(self):
        letterInitial = []
        letterFreqs = []
        letters = []

        with open(self.address, 'r') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        letters.append(char.lower())

        uniqueLetters = set(letters)

        for letter in uniqueLetters:
            frequency = letters.count(letter)
            letterInitial.append(letter)
            letterFreqs.append(letter + " = " + str(frequency))

        print("List           ->", letterInitial)
        print("Resulting List ->", letterFreqs)

""" creating DictCount subclasses that override the “calculateFreqs” method. It will read the file using its
    address given in “_init_” and store each letter in a dictionary with a value 0 initially. Also the method
    calculate the frequency of each unique letter in the file. Update values of the letters with their calculated
    frequencies. Print the resulting dictionary.                                                                    """
class DictCount(FrequencyCounter):
    def calculateFreqs(self):
        letterInitial = {}
        letterFreqs = {}

        with open(self.address, 'r') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        char = char.lower()
                        letterInitial[char] = letterInitial.get(char, 0)
                        letterFreqs[char]   = letterFreqs.get(char, 0) + 1

        print("Dict           ->", letterInitial)
        print("Updated Dict   ->", letterFreqs)


""" calling the methods """
listCounter = ListCount("weirdWords.txt")
listCounter.calculateFreqs()

dictCounter = DictCount("weirdWords.txt")
dictCounter.calculateFreqs()
