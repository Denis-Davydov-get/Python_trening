def process(input_string: str) -> str:
    new_list = input_string.split()
    count_a, count_b, count_c = 0, 0, 0
    for i in new_list:
        i = int(i)
        if i > 0:
            count_a += 1
        elif i < 0:
            count_b += 1
        else:
            count_c += 1
    return f"выше нуля: {count_a}, ниже нуля: {count_b}, равна нулю: {count_c}"

input_string = "5 -2 0 0 7 8 -1"
output_string = process(input_string)
print(output_string)