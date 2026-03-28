# helper functions
def print_operations():
    # Print the available math operations
    print("This calculator can do:")
    print("• Basic Arithemetics: addition, subtraction, multiplication, and division.")
    
    return

def print_syntax():
    # print math operations syntax
    print("Please enter your operations as the following syntax:")
    print("• Use +, -, * and / for the basic arithmetic operations.")
    print("• The calculator only allows one operation at a time.")
    print("For example:")
    print("1. 5 + 5")
    print("2. 3 / 3")
    print("Enter 'end' to end the program")
    return

# return the result of the equation user provide
def process_operation(user_input):
    symbols = ['+', '-', '*', '/'] # operators
    
    # check the operation
    for i in range(4):
        operator = user_input.find(symbols[i])
        if operator > 0: break

    # find the operands and convert it into integer
    str_nums = [user_input[:operator], user_input[operator + 1:]]

    int_nums = []
    for x in str_nums:
        int_nums.append(int(x))

    # match and perform the operation
    match user_input[operator]:
        case '+': return int_nums[0] + int_nums[1]
        case '-': return int_nums[0] - int_nums[1]
        case '*': return int_nums[0] * int_nums[1]
        case '/': return int_nums[0] / int_nums[1]
    return

# main function
def main():
    print("Welcome to simple calculator.")
    print_operations()
    print_syntax()

    user_input = input("Please Enter: ").replace(" ", "")
    
    while(user_input != 'end'):
        result = process_operation(user_input)
        print("result = ", result)

        user_input = input("Please Enter: ").replace(" ", "")
    
    return

if __name__ == "__main__":
    main()
