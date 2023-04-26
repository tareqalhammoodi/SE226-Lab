//SE226 – LAB#6.5
#include <iostream>
#include <algorithm>
#include <list>
using namespace std;

//Task 1
list<int> Intersection(list<int> list1, list<int> list2) {
    list<int> intersection;                                                                                             // define a list
    for (auto it = list1.begin(); it != list1.end(); ++it) {                                            // check whether there is common elements in list1 and list2
        if (find(list2.begin(), list2.end(), *it) != list2.end()) {
            intersection.push_back(*it);                                                                             // if so add it to intersection list
        }
    }
    return intersection;                                                                                                // return list of common elements
}
//Task2
list<string> isPalindromes(const list<string> & strings) {
    /*
     *  A string is said to be palindrome if it remains the same on reading from both ends.
     *  It means that when you reverse a given string, it should be the same as the original string.
     */
    list<string> palindromes;                                                                                           // define a list
    for (const string& str : strings) {                                                                                 // check whether the string is palindromes or not
        bool is_palindrome = true;
        for (size_t i = 0; i < str.size() / 2; ++i) {
            if (str[i] != str[str.size() - i - 1]) {
                is_palindrome = false;
                break;
            }
        }
        if (is_palindrome) {
            palindromes.push_back(str);                                                                              // if so add it to the list
        }
    }
    return palindromes;                                                                                                 // return list palindromes strings
}
//Task3
list<int> pirmeNumbers(list<int> List) {
    list<int> primesList;                                                                                               // create an empty list to store the prime numbers
    while (!List.empty()) {                                                                                             // repeat until there are no more numbers in the input list
        int current_number = List.front();                                                                              // take the first number in the input list and remove it
        List.pop_front();
        if (current_number == 0 || current_number == 1) {
            continue;
        }
        primesList.push_back(current_number);                                                                        // add the current number to the prime list.
        List.remove_if([current_number](int n) { return n % current_number == 0; });
    }
    return primesList;                                                                                                  // return list of prime numbers
}
//Task4
list<string> Anagrams(string word, list<string> word_list) {
    /*
     * An anagram is a word or phrase formed by rearranging the letters of another word or phrase,
     * such as "cinema" and "iceman".
     */
    list<string> anagrams_list;                                                                                         // define an empty list to store anagrams
    transform(word.begin(), word.end(), word.begin(), ::tolower);                                   // convert the input word into a sorted list of characters
    sort(word.begin(), word.end());
    for (auto it = word_list.begin(); it != word_list.end(); it++) {                                 // iterate over the strings in word_list and for each string
        string sorted_word = *it;
        transform(sorted_word.begin(), sorted_word.end(), sorted_word.begin(), ::tolower);          // convert the string into a sorted list of characters
        sort(sorted_word.begin(), sorted_word.end());
        if (sorted_word == word) {                                                                                      // compare the sorted list of characters to the sorted list of characters for word
            anagrams_list.push_back(*it);                                                                            // if the two lists are equal, the string is an anagram of word and should be added to the output list
        }
    }
    return anagrams_list;                                                                                               // return the output list of anagrams
}

//Testing
int main() {
    list<int> List1 = {4, 9, 2, 0, 8};
    list<int> List2 = {1, 5, 0, 2, 7};
    list<int> intersection = Intersection(List1, List2);
    cout << "Intersection: ";
    for (auto it = intersection.begin(); it != intersection.end(); ++it) {
        cout << *it << " | ";
    }

    cout << endl;

    list<string> strings = {"moon", "level", "kayak", "strawberry", "dad"};
    list<string> palindromes = isPalindromes(strings);
    cout << "Palindromes: ";
    for (const string& str : palindromes) {
        cout << str << " | ";
    }

    cout << endl;

    list<int> List = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20};
    list<int> primeList = pirmeNumbers(List);
    cout << "Prime Numbers: ";
    for (int prime : primeList) {
        cout << prime << " | ";
    }

    cout << endl;

    string word = "listen"; list<string> word_list = {"enlists", "google", "inlets", "banana"};
    list<string> anagrams_list = Anagrams(word, word_list);
    cout << "Anagrams: ";
    for (auto it = anagrams_list.begin(); it != anagrams_list.end(); it++) {
        cout << *it << " | ";
    }

    return 0;
}
