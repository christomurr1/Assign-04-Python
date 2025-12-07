#!/usr/bin/env python3
# Created By: Christopher El-Murr
# Date: 12,01, 2025
# This program uses a for loop calculate the factors of the number


def main():
    try:
        # Ask the user for a positive integer
        num = int(input("Enter a positive integer: "))

        if num <= 0:
            print("Please enter a number greater than zero.")
        else:
            print(f"Factors of {num} are:")

            # Use a for loop to check for factors
            for i in range(1, num + 1):
                # If remainder is 0, i is a factor
                if num % i == 0:
                    print(i)

    except ValueError:
        # Handles the case where the user enters something that's not an integer
        print("Invalid input! Please enter a valid integer.")


if __name__ == "__main__":
    main()
