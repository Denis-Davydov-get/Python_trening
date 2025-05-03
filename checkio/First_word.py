# Дана строка и нужно найти ее первое слово.
# Строка состоит только из английских символов и пробелов.
# В начале и в конце строки пробелов нет.

# input: string (str).
# output: string (str).

# Пример:
# assert first_word("Hello world") == "Hello"
# assert first_word("a word") == "a"
# assert first_word("greeting from CheckiO Planet") == "greeting"
# assert first_word("hi") == "hi"

def first_word(text: str) -> str:
    return text.split()[0]


print("Example:")
print(first_word("Hello world"))

# These "asserts" are used for self-checking
assert first_word("Hello world") == "Hello"
assert first_word("a word") == "a"
assert first_word("greeting from CheckiO Planet") == "greeting"
assert first_word("hi") == "hi"

print("The mission is done! Click 'Check Solution' to earn rewards!")