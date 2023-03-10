import numpy as np
import sys


'''Function that checks if the user input is a positive integer.
It takes the argument provided as input, and if the input is a positive integer, it executes 
the fibonacci_sequence_digit_index function; otherwise it will display error messages.'''
def check_input(n):
    if n.isdigit():
        fibonacci_sequence_digit_index(int(n))
    else:
        try:
            if float(n):
                return print("Input is incorrect. Enter a Postive Interger.")
        except ValueError:
            return print("Input is incorrect. Enter a Postive Interger.")


'''Function that counts the number of digits in a number. 
It takes a number as input and returns the amount of digits in the number.'''
def count_digits(number):
    count = 0
    if number == 0:
        return 1
    while number > 0:
        count += 1
        number = np.floor_divide(number, 10)
    return count


'''Function that will determine the index that will n digits
It takes the number of digits as input and returns the index of the first term in the
Fibonacci sequence that contains that number of digits.'''
def fibonacci_sequence_digit_index(n):
    if n == 0:
        print("There is no term that will contain zero digits!")
    elif n == 1:
        print("The first term in the Fibonacci seqeunce that will contain 1 digit is at index 0.")
    else:
        a = np.array([1, 1], dtype='object')
        index_counter = 2
        while True:
            a = np.append(a, [a[index_counter-1]+a[index_counter-2]])
            if count_digits(a[index_counter]) >= n:
                return print("In the Fibonacci sequence the first term to contain " 
                + str(n) + " digits is at index: " + str(index_counter + 1))
            index_counter += 1


if __name__ == "__main__":
    '''Chech in an argument is given'''
    if len(sys.argv) > 1:
        check_input(sys.argv[1])
    else:
        print("Please enter a Postive Interger")
   