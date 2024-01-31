# Computation and Programming
# 2.5 While Loops

# Finger exercise: Replace the comment in the following code with a
# while loop.

# num_x = int(input('How many times should I print the letter
# X? '))
# to_print = ''
# #concatenate X to to_print num_x times
# print(to_print)

def print_x():
    num_x = int(input('How many times should I print the letter X? '))
    result = f'I printed x {num_x} times.'

    while num_x > 0:
        print('X')
        num_x -= 1

    print(result)


# Finger exercise: Write a program that asks the user to input 10
# integers, and then prints the largest odd number that was entered. If
# no odd number was entered, it should print a message to that effect.

def print_largest_odd():

    largest_odd = float('-inf')
    iterations = 0

    print("Enter 10 integers, I will return the largest odd integer")

    while iterations < 10:
        num = int(input(f"Enter integer # {iterations + 1}: "))
        if num % 2 != 0 and num > largest_odd:
            largest_odd = num
        iterations += 1

    if largest_odd != float('-inf'):
        print(largest_odd)
    else:
        print('No odd number')


# Finger exercise: Write a program that prints the sum of the prime
# numbers greater than 2 and less than 1000. Hint: you probably want
# to use a for loop that is a primality test nested inside a for loop that
# iterates over the odd integers between 3 and 999.

def print_sum_of_primes():
    total = 0
    for num in range(2, 1000):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            total += num
    print(total)


def main():
    print("Please choose a program to run:")
    print("1. X Printer")
    print("2. Largest Odd")
    print("3. Sum of Primes")
    program = input("Enter 1 or 2 ")

    if program == '1':
        print_x()
    if program == '2':
        print_largest_odd()
    if program == '3':
        print_sum_of_primes()
    else:
        print(f"Sorry, program {program} not found")


main()
