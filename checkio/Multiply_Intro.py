# Напишите функцию, которая будет получать 2 числа и возвращать результат произведения этих чисел.
def mult_two(a: int, b: int) -> int:
    if b != 0 and a != 0:
        return a * b
    return 0


print("Example")
print(mult_two(1, 2))

assert mult_two(3, 2) == 6
assert mult_two(0, 1) == 0

print("The first mission is done! Click 'Check' to earn cool rewards!")
