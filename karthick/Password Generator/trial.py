from random import sample
from random import randint, shuffle
from random import seed
import string


def passwordGenerator(uppercase=1, lowercase=2, numbers=3, symbols=4, reps=20):
    i = 0
    while i < reps:
        l1 = list(string.ascii_uppercase)
        l2 = list(string.ascii_lowercase)
        l3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        l4 = list(string.punctuation)
        # print(len(l1), len(l2), len(l3), len(l4))
        seed(randint(0, 100))
        pos = randint(0, 17)
        pos2 = randint(0, 13)
        pos3 = randint(0, 33)
        subset = list(sample(l1, uppercase))
        subset[pos:pos] = list(sample(l2, lowercase))
        subset[pos2:pos2] = list(sample(l3, numbers))
        subset[pos3:pos3] = list(sample(l4, symbols))
        shuffle(subset)
        password = ''.join(map(str, subset))
        print("\nThe generated Password is: " + password)
        i = i+1


if __name__ == '__main__':
    print("this is a program to generate a random password\tThere can be 18 char max-")
    upperCase = int(input("\nEnter the no. of upper case letters: "))
    if upperCase > 5:
        upperCase = 4
    lowerCase = int(input("Enter the no. of lower case letters: "))
    if lowerCase > 5:
        lowerCase = 4
    nNumbers = int(input("Enter the no. of numbers you want to use: "))
    if nNumbers > 4:
        nNumbers = 4
    nSymbols = int(input("Enter the no. of symbols you want to use: "))
    if nSymbols > 4:
        nSymbols = 4
    iterations = int(input("no. of passwords you want to generate: "))
    if iterations > 20:
        iterations = 20

    passwordGenerator(upperCase, lowerCase, nNumbers, nSymbols, iterations)
