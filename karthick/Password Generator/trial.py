from random import sample
from random import randint
from random import seed
import string


def passwordGenerator(uppercase=1, lowercase=2, numbers=3, symbols=4):
    l1 = list(string.ascii_uppercase)
    l2 = list(string.ascii_lowercase)
    l3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    l4 = list(string.punctuation)
    # print(len(l1), len(l2), len(l3), len(l4))
    seed(1)
    pos = randint(0, 17)
    pos2 = randint(0, 13)
    pos3 = randint(0, 33)
    subset = list(sample(l1, uppercase))
    subset[pos:pos] = list(sample(l2, lowercase))
    subset[pos2:pos2] = list(sample(l3, numbers))
    subset[pos3:pos3] = list(sample(l4, symbols))
    password = ''.join(map(str, subset))
    print("\nThe generated Password is: " + password)


if __name__ == '__main__':
    print("this is a program to generate a random password")
    upperCase = int(input("\nEnter the no. of upper case letters: "))
    if upperCase > 12:
        upperCase = 12
    lowerCase = int(input("Enter the no. of lower case letters: "))
    if lowerCase > 12:
        lowerCase = 12
    nNumbers = int(input("Enter the no. of numbers you want to use: "))
    if nNumbers > 10:
        nNumbers = 10
    nSymbols = int(input("Enter the no. of symbols you want to use: "))
    if nSymbols > 20:
        nSymbols = 20
    passwordGenerator(upperCase, lowerCase, nNumbers, nSymbols)
