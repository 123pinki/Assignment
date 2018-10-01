"""Assignment2 (programming):
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an
integral number between 1 and n (both included). and then the program should print the dictionary.
Example: Input = 6. Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}"""


def print_dict(num):
    dict1 = lambda num1: {num1: (num1*num1) for num1 in range(1, num1 + 1)}
    return dict1(num)


print(print_dict(8))
