import json

def add_numbers(num1, num2):
    num1_str = str(num1)[::-1]  # reverse the strings for easier processing
    num2_str = str(num2)[::-1]
    max_len = max(len(num1_str), len(num2_str))
    carry = 0
    steps = {}

    for i in range(max_len):
        digit1 = int(num1_str[i]) if i < len(num1_str) else 0
        digit2 = int(num2_str[i]) if i < len(num2_str) else 0
        digit_sum = digit1 + digit2 + carry

        carry_str = '1' * carry if carry > 0 else ''
        sum_str = carry_str + str(digit_sum)[-1]

        steps[f"step{i+1}"] = {"carryString": carry_str, "sumString": sum_str}

        carry = digit_sum // 10

    if carry > 0:
        steps[f"step{max_len+1}"] = {"carryString": '1' * carry, "sumString": str(carry)}

    return steps

num1 = 1489
num2 = 714
steps = add_numbers(num1, num2)
print(json.dumps(steps, indent=4))
