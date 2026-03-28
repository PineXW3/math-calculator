symbols = ('+', '-', '*', '/', '^', 'root', '(', ')')

def scanning(user_input):
    smallest_unit = []
    input_length = len(user_input)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    str_num = ""
    op_str = ""
    
    for i in range(input_length):
        if user_input[i].isdigit(): # if the character is a number
            str_num += user_input[i]
            
            # if i is at the end of the list, or next character is not a number
            if (i == input_length - 1 or not(user_input[i + 1].isdigit())):
                smallest_unit.append(int(str_num))
                str_num = ""
        else: # else the character is a symbol
            op_str += user_input[i]
            if op_str in symbols:
                smallest_unit.append(op_str)
                op_str = ""
    return smallest_unit
