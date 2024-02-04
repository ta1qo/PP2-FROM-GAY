# def spy_game(nums):
#     x = False
#     y = False
#     for num in nums:
#         if num == 0 and not x:
#             x = True
#             z = False
#             continue
#         if num == 0:
#             y = True
#         if num == 7 and x and y:
#             z = True
#     return x and y and z


# print(spy_game([1, 2, 4, 0, 0, 7, 5]))
# print(spy_game([1, 0, 2, 4, 0, 5, 7]))
# print(spy_game([1, 7, 2, 0, 4, 5, 0]))

# print(spy_game(list(map(int, input().split()))))


def spy_game(nums):
    check = [0, 0, 7]
    i = 0

    for j in range(len(nums)):
        if check[i] == nums[j]:
            i += 1

    print(True if i == 3 else False)

spy_game(list(map(int, input().split())))
