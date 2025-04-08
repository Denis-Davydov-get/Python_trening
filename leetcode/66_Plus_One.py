# Вам дается большое целое число, представленное в виде цифр целочисленного массива, где каждая цифра [i]
# - это цифра целого числа. Цифры упорядочены от наиболее значимых до наименьших значительных
# в правом порядке. Большое целое число не содержит никаких ведущих 0.
#
# Увеличьте большое целое число на один и верните полученное множество цифр.
#
# Example 1:
#
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:
#
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# Example 3:
#
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].


class Solution:
    def plus_one(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):  # в обратном порядке
            # Если цифра меньше 9, просто увеличиваем её и возвращаем результат
            if digits[i] <= 9:
                digits[i] += 1
                return digits


if __name__ == '__main__':
    test = Solution()
    # digits_1 = [1, 2, 3]
    # digits_2 = [4, 3, 2, 1]
    # digits_3 = [9]
    digits_4 = [9, 9]
    # assert test.plus_one(digits_1) == [1, 2, 4]
    # assert test.plus_one(digits_2) == [4, 3, 2, 2]
    # assert test.plus_one(digits_3) == [1, 0]
    print(test.plus_one(digits_4)) # [1, 0, 0]
