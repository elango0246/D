def is_armstrong_number(num):
    # Convert the number to string to easily iterate through digits
    digits = str(num)
    n = len(digits)  # Number of digits
    sum_of_powers = sum(int(digit) ** n for digit in digits)
    return sum_of_powers == num

def main():
    num = int(input("Enter a number to check if it's an Armstrong number: "))
    if is_armstrong_number(num):
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")


main()
