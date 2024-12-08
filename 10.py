def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison

    return s == s[::-1]

def main():
    string = input("Enter a string to check if it's a palindrome: ")
    if is_palindrome(string):
        print(f"'{string}' is a palindrome.")
    else:
        print(f"'{string}' is not a palindrome.")

if __name__ == "__main__":
    main()
