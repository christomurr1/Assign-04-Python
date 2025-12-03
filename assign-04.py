#!/usr/bin/env python3
# Created By: Christopher El-Murr
# Date: 11 14, 2025
# This program uses a for loop calculate the factors of the number


def main():
    try:
        # Ask the user for a positive integer
        num = int(input("Enter a positive integer: "))

        if num <= 0:
            print("Please enter a number greater than zero.")
        else:
            print(f"Factors of {num} are:")

        # Use a while loop to check for factors
        i = 1
        while i <= num:
            # If remainder is 0, i is a factor
            if num % i == 0:
                print(i)
            # Move to the next number
            i += 1

    except ValueError:
        # Handles the case where the user enters something that's not an integer
        print("Invalid input! Please enter a valid integer.")


if __name__ == "__main__":
    main()
