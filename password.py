#!/usr/bin/python
# Some license stuff

from random import sample, choice
import sys

def pickRandomTypeableCharacters(numberOfCharacters, unique):
    """Generates N (unique, if required) ASCII characters and
    returns as a list"""
    allTypeableAscii = [chr(x) for x in range(32, 127)]
    allTypeableAscii.remove('`') # These make everything horrible
    allTypeableAscii.remove('\'')
    if unique:
        return sample(allTypeableAscii, numberOfCharacters)
    else:
        return [choice(allTypeableAscii) for x in range(numberOfCharacters)]

def generateLayout():
    """Generates a new layout for the keyboard"""
    layout = pickRandomTypeableCharacters(26, True)
    keyboard = "QWERTYUIOPASDFGHJKLZXCVBNM"
    zipped = zip(keyboard, layout)
    return [layout, [str(": ".join(x)) for x in list(zipped)]]

def generateBasePhrase():
    """Generates an eight character base phrase, guarantee at leat one digit"""
    containsDigit = False
    while not containsDigit:
        basePhrase = "".join(pickRandomTypeableCharacters(8, False))
        containsDigit = any(character.isdigit() for character in basePhrase)
    return basePhrase

def generateNewValues():
    """Generates a new layout and base phrase"""
    layout = generateLayout()
    layoutString = "".join(layout[0])
    yourLayout = "\n".join(layout[1])
    yourBasePhrase = generateBasePhrase()

    string = "Layout: {}\nBase phrase: {}\nKeep these safe and don't lose them!".format(layoutString,
                                                                                           yourBasePhrase)
    string2 = "Use your layout like this: ./main.py '{}' '{}' <secret> <sitename>".format(layoutString,
                                                                                          yourBasePhrase)
    print(string)
    print(string2)

def giveEncodedString(layout, basePhrase, secret, sitename):
    """Returns the password string that should be typed for the provided details"""
    keyboard = "QWERTYUIOPASDFGHJKLZXCVBNM"
    layoutMap = dict(zip(keyboard, layout))
    encodedSecret = "".join([layoutMap[char.upper()] for char in secret])
    encodedSitename = "".join([layoutMap[char.upper()] for char in sitename])
    print("Your password is: " + basePhrase + encodedSecret + encodedSitename)

if __name__ == '__main__':
    if (len(sys.argv) == 1):
        generateNewValues()
    elif (len(sys.argv) == 5):
        giveEncodedString(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        progName = sys.argv[0]
        print("""Usage: {} - Generate new layout and base phrase
       {} <layout> <base phrase> <secret> <sitename> - Return password string
       <secret> should be constant across uses, <sitename> is the name of the site""".format(progName, progName))
