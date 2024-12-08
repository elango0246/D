import math


def area_of_circle(radius):
    return math.pi * radius ** 2


def area_of_rectangle(length, width):
    return length * width


def area_of_triangle(base, height):
    return 0.5 * base * height


def area_of_square(side):
    return side ** 2


def main():
    print("Choose the shape to calculate the area:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Square")

    choice = input("Enter the number of the shape (1/2/3/4): ")

    if choice == '1':  # Circle
        radius = float(input("Enter the radius of the circle: "))
        print("The area of the circle is:", area_of_circle(radius))

    elif choice == '2':  # Rectangle
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print(f"The area of the rectangle is: {area_of_rectangle(length, width):.2f}")

    elif choice == '3':  # Triangle
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print(f"The area of the triangle is: {area_of_triangle(base, height):.2f}")

    elif choice == '4':  # Square
        side = float(input("Enter the side of the square: "))
        print(f"The area of the square is: {area_of_square(side):.2f}")

    else:
        print("Invalid choice! Please select a valid option.")


main()
