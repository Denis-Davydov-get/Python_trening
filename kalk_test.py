def calc(a, actions, b):
    if actions == "*":
        return a * b
    elif actions == "/":
        return a / b
    elif actions == "-":
        return a - b
    elif actions == "+":
        return a + b
    else:
        print('None')

i = calc(8, "*", 8)