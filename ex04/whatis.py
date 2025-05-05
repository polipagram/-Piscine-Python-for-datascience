import sys

def checker(number):
    if number % 2 == 0:
        return "I'm Even."
    else:
        return "I'm Odd."

def main():
    if len(sys.argv) == 1:
        return
    elif len(sys.argv) != 2:
        print("AssertionError: more than one argument is provided")
        sys.exit(1)

    try:
        nb = int(sys.argv[1])
        res = checker(nb)
        print(res)
    except ValueError:
        print("AssertionError: Argument is not an integer")
        sys.exit(1)

if __name__ == "__main__":
    main()
