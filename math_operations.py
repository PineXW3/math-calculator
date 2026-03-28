def basic_arithmetic(nums, operator):
    ""
    match operator:
        case '+': return nums[0] + nums[1]
        case '-': return nums[0] - nums[1]
        case '*': return nums[0] * nums[1]
        case '/': return nums[0] / nums[1]
        case '^': return nums[0] ** nums[1]
        case 'root': return nums[0] ** (1/nums[1])
    return