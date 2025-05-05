# создать функцию, которая принимает на вход кортеж и возвращает кортеж из 3 элементов: первого, третьего и второго с конца элементов заданного кортежа.


def easy_unpack(elements: tuple) -> tuple:
    first_el = elements[0]
    three_el = elements[2]
    last_but_one = elements[-2]
    return first_el, three_el, last_but_one


print("Example:")
print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))

# These "asserts" are used for self-checking
assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
assert easy_unpack((6, 3, 7)) == (6, 7, 3)

print("The mission is done! Click 'Check Solution' to earn rewards!")
