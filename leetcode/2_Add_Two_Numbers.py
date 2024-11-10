# Вам даны два непустых связанных списка, представляющих два неотрицательных целых числа.
# Цифры хранятся в обратном порядке, и каждый из их узлов содержит одну цифру.
# Сложите два числа и верните сумму в виде связанного списка.
#
# Вы можете предположить, что эти два числа не содержат ведущих нулей, кроме самого числа 0.
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
def add_two_numbers(l1: list, l2: list) -> list:
    for i in range(0, len(l1)):
        for j in range(0, len(l2)):
            result = l1[i] + l2[j]
            res_list = []
            res_list.append(result)
            return res_list


class Solution:
    pass

s = Solution()
l1, l2 = [5, 6, 4], [2, 4, 3]
print(add_two_numbers(l1, l2))
