import math_operations as mop
import scanner

# helper functions
def print_operations():
    # Print the available math operations
    print("This calculator can do:")
    print("• Basic Arithemetics: addition, subtraction, multiplication, and division.")
    print("• Advanced Arithemetics: finding exponents and roots.")
    return

def print_syntax():
    # print math operations syntax
    print("Please enter your operations as the following syntax:")
    print("• Use +, -, * and / for the basic arithmetic operations.")
    print("• Use base^exponent and 'radicand' root 'index' for the advanced arithmetic.")
    print("• The calculator only allows one operation at a time.")
    print("For example:")
    print("1. 5 + 5")
    print("2. 5^2")
    print("3. 25 root 2")
    print("Enter 'end' to end the program")
    return

def compute(equation):
    nums = [equation[0], equation[2]]
    operator = equation[1]
    return mop.basic_arithmetic(nums, operator)

def determine_operation(equation):
    return

# main function
def main():
    # Introduction
    print("Welcome to simple calculator.")
    print_operations()
    print_syntax()

    user_input = "" # declaration
    
    #
    while(user_input != 'end'):
        user_input = input("Please Enter: ").replace(" ", "")
        equation = scanner.scanning(user_input)

        print(compute(equation))
    
    return

if __name__ == "__main__":
    main()
