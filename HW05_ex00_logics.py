#!/usr/bin/env python3
# HW05_ex00_logics.py


##############################################################################
def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    pass
    num = int(input("Number? "))
    if (num % 2) == 0:
        print ("Your number is even")
    else:
        print ("Your number is odd") 


def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    numbers_in_grid = list(range(1,101))
    count = 0
    pass
    for x in numbers_in_grid:
        print("{:<4} ".format(x), end = " ")
        count += 1
        if count % 10 == 0:
            print()
            count = 0


def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    pass 
    number_list = []
    
    while True:
        try:
            user_input = input("Enter a number to be averaged or 'done': ")
            if user_input.lower() == "done":
                if len(number_list) > 0:
                    print(sum(number_list)/len(number_list))
                else:
                    return "More numbers please!"
            else:
                number_list.append(float(user_input))
        except:
            print("Not a valid number!")



##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    pass
    even_odd()
    ten_by_ten()
    print(find_average())


if __name__ == '__main__':
    main()
