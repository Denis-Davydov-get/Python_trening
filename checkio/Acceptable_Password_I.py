def is_acceptable_password(password: str) -> bool:
    ### длина пароля должна быть больше 6.
    if len(password) <= 6:
        return False
    else:
        return True


print("Example:")
print(is_acceptable_password("short"))

# These "asserts" are used for self-checking
assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
