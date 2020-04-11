# generate a random password with length "of  MIN 6 charcters" 
from random import seed
from random import randint
import string


def pw_gen(password):
    # ENTER THE REQUIREMENT TO DISPLAY PASSWORD
    # "saShank23$"
    l1 = set(string.ascii_uppercase)
    l2 = set(string.ascii_lowercase)
    l3 = set(string.digits)
    l4 = set(string.punctuation)
    pwd = set([ch for ch in str(password)])
    if len(pwd) > 6 and len(pwd.intersection(l1)) > 0 and len(pwd.intersection(l2)) > 0 and len(pwd.intersection(l3)) > 0 and len(pwd.intersection(l4)) > 0:
        print("your password ", password, " is approved")
    else:
        print("PASSWORD INSUFFICENT")


x = input("pls enter your password: ")
pw_gen(x)
