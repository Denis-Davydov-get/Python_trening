# выяснить какое количество нулей содержит данное число в конце

def end_zeros(n):
    return 0 if n % 10 else 1 + (end_zeros(n // 10) if n else 0)



print("Example:")
print(end_zeros(10))

# These "asserts" are used for self-checking
assert end_zeros(0) == 1
assert end_zeros(1) == 0
assert end_zeros(10) == 1
assert end_zeros(101) == 0
assert end_zeros(245) == 0
assert end_zeros(100100) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")
