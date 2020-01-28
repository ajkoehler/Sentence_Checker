# Sentence_Checker

Simple sentence checker based off of a Daily Coding Problem.

Daily Coding Problem: Problem #431 [Medium]



This problem was asked by Nest.

Create a basic sentence checker that takes in a stream of characters and determines whether they form valid sentences. If a sentence is valid, the program should print it out.

We can consider a sentence valid if it conforms to the following rules:

The sentence must start with a capital letter, followed by a lowercase letter or a space.
All other characters must be lowercase letters, separators `(,,;,:)` or terminal marks `(.,?,!,‽)`.
There must be a single space between each word.
The sentence must end with a terminal mark immediately following a word.


### Sample output:
python3 sentence_checker.py

```
Line 1: This is a valid sentence.
Sentence is valid
Line 2: Testing?
Sentence is valid
Line 3: This is not a valid sentence
Sentence must end in a terminating mark
Line 4: Testing numbers 1
No Numbers
Line 5: Testing1 numbers2
No Numbers
Line 6: Testing double  spaces
No double spaces allowed
Line 7: Testing invalid char-
Invalid character
Line 8: Testing all of the valid characters, is really difficult: sometimes it is not.
Sentence is valid
Line 9: Can I do them all correctly?
Too many uppercases
*This is a flaw in the way the problem was asked and how it was coded.  I should be an acceptable letter, unless it's within another word*
Line 10: This is an exclamation!
Sentence is valid
Line 11: Semi colon: what does this do?
Sentence is valid
Line 12: testing lowercase
Sentence must start with an uppercase letter
Line 13: Testing double Uppercase
Too many uppercases
akoehler:~ andrewkoehler$ python3 sentence_checker.py
Line 1: This is a valid sentence.
Sentence is valid
Line 2: Testing?
Sentence is valid
Line 3: This is not a valid sentence
Sentence must end in a terminating mark
Line 4: Testing numbers 1
No Numbers
Line 5: Testing1 numbers2
No Numbers
Line 6: Testing double  spaces
No double spaces allowed
Line 7: Testing invalid char-
Invalid character
Line 8: Testing all of the valid characters, is really difficult: sometimes it is not.
Sentence is valid
Line 9: I actually cannot use the uppercase I in a sentence, this would fail.
Too many uppercases
Line 10: This is an exclamation!
Sentence is valid
Line 11: Semi colon: what does this do?
Sentence is valid
Line 12: testing lowercase
Sentence must start with an uppercase letter
Line 13: Testing double Uppercase
Too many uppercases
```
