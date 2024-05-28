# app.py

from icecream import ic
from enum import Enum
from pyfiglet import Figlet
from tools.numbers.simp import add, subtract
from tools.numbers.comp import sumofdigits, ispal

class MenuOption(Enum):
    ADD = 1
    SUBTRACT = 2
    SUMOFDIGITS = 3
    ISPAL = 4
    EXIT = 5

def print_ascii_art(text, font="standard"):
    figlet = Figlet(font=font)
    return figlet.renderText(text)

def main():
    print(print_ascii_art("Welcome to Test Management System"))
    
    while True:
        print("\nSelect an operation:")
        for option in MenuOption:
            print(f"{option.value}. {option.name.capitalize()}")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice.isdigit():
            choice = int(choice)
            if choice == MenuOption.ADD.value:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                result = add(a, b)
                ic(result)
                print(print_ascii_art(f"Result: {result}"))

            elif choice == MenuOption.SUBTRACT.value:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                result = subtract(a, b)
                ic(result)
                print(print_ascii_art(f"Result: {result}"))

            elif choice == MenuOption.SUMOFDIGITS.value:
                n = int(input("Enter a number: "))
                result = sumofdigits(n)
                ic(result)
                print(print_ascii_art(f"Result: {result}"))

            elif choice == MenuOption.ISPAL.value:
                n = int(input("Enter a number: "))
                result = ispal(n)
                ic(result)
                if result:
                    print(print_ascii_art(f"{n} is a palindrome"))
                else:
                    print(print_ascii_art(f"{n} is not a palindrome"))

            elif choice == MenuOption.EXIT.value:
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please try again.")
        else:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
