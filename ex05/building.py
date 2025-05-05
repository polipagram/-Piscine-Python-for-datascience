import sys
import string

def count_chars(content):
    counter = {
        'upper': 0,
        'lower': 0,
        'punct': 0,
        'spaces': 0,
        'digits': 0
    }
    for char in content:
        if char.isupper():
            counter['upper'] += 1
        elif char.islower():
            counter['lower'] += 1
        elif char.isdigit():
            counter['digits'] += 1
        elif char.isspace():
            counter['spaces'] += 1
        elif char in string.punctuation:
            counter['punct'] += 1
    return counter

def main():
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    
    text = sys.argv[1] if len(sys.argv) == 2 else input("What is the text to count?\n")
    
    total = len(text)
    counts = count_chars(text)
    print(f"The text contains {total} characters:")
    print(f"{counts['upper']} upper letters")
    print(f"{counts['lower']} lower letters")
    print(f"{counts['punct']} punctuation marks")
    print(f"{counts['spaces']} spaces")
    print(f"{counts['digits']} digits")

if __name__ == "__main__":
    main()
