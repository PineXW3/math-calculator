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
    # If there's only two operands and one operator
    if (len(equation) == 3):
        # Perform the operation
        nums = [equation[0], equation[2]]
        operator = equation[1]
        return [mop.basic_arithmetic(nums, operator)] # return the result
    
    # The subequation contains a one step arithmetic equation: a operator b.
    subequation = order_operations(equation)

    # Replace the subequation inside the equation by the computed result of the subequation
    equation[subequation["left_side"]:subequation["right_side"] + 1] = compute(subequation["new_equation"]) 
    
    return compute(equation)
    

def order_operations(equation):
    # The if-elif statements followed the order of PEMDES

    # Parathesis
    if all(x in equation for x in '()'):
        count = 0

        # Find the most inner parathesis
        left_bracket = equation.index('(')
        right_bracket = 0
        for index in range(left_bracket, len(equation)):
            if equation[index] == '(': 
                count += 1
                
            elif equation[index] == ')':
                count -= 1
                right_bracket = index
            if count == 0: break # We found the right bracket that match the left
        
        return {
            "new_equation":equation[left_bracket + 1:right_bracket],
            "left_side":left_bracket,
            "right_side":right_bracket
            }
    
    # Exponents
    elif '^' in equation or 'root' in equation:
        for index, value in enumerate(equation):
            if value == '^' or value == 'root':
                return helper(equation, index - 1, index + 1)
    
    # Multiply or Divide
    elif '*' in equation or '/' in equation:
        for index, value in enumerate(equation):
            if value == '*' or value == '/':
                return helper(equation, index - 1, index + 1)
    
    # Add or Subtract
    elif '+' in equation or '-' in equation:
        for index, value in enumerate(equation):
            if value == '+' or value == '-':
                return helper(equation, index - 1, index + 1)

    
    return

def helper(equation, left_side, right_side):
    subequation = {"new_equation":equation[left_side:right_side + 1], "left_side":left_side, "right_side":right_side}
    return subequation

# main function
def main():
    # Introduction
    
    print("Welcome to simple calculator.")
    print_operations()
    print_syntax()

    user_input = "" # declaration
    
    # Looping until user end the program
    while(user_input != 'end'):
        try:
            # Prompt for math equations
            user_input = input("Please Enter: ").replace(" ", "")

            # Turn the user_input into tokens 
            equation = scanner.scanning(user_input)

            # Compute the equation
            answer = compute(equation)
            print("Answer =", answer[0])
            
        except Exception:
            print("Oh No, error")
    return
    
        

if __name__ == "__main__":
    main()
