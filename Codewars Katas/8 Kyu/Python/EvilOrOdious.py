'''

Codewars Kata - 8 Kyu - Evil or Odious

Description:

The number n is Evil if it has an even number of 1's in its binary expansion.
First ten: 3, 5, 6, 9, 10, 12, 15, 17, 18, 20

The number n is Odious if it has an odd number of 1's in its binary expansion.
First ten: 1, 2, 4, 7, 8, 11, 13, 14, 16, 19

You have to write a function that determine if a number is Evil of Odious, function should return "It's Evil!" in case of evil number and "It's Odious!" in case of odious number.

good luck :)

'''

def evil(n):
    return 'It\'s Evil!' if bin(n)[2:].count('1') % 2 == 0 else 'It\'s Odious!'
