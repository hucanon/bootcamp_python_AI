import string
import sys

def text_analyzer(text = "no_text"):
    punc = 0
    space = 0
    low = 0
    upp = 0
    if text == "no_text":
        print("What is the text to analyze?")
        text = raw_input()
    for i in text:
        if i in string.punctuation:
            punc += 1
        elif i in string.whitespace:
            space += 1
        elif i.isupper() and i.isalpha() == True:
            upp += 1
        elif i.islower() and i.isalpha() == True:
            low += 1
    print("The text contains %i characters:" % (len(text)))
    print("- %i upper letters" % upp)
    print("- %i lower letters" % low)
    print("- %i punctuation marks" % punc)
    print("- %i spaces" % space)
