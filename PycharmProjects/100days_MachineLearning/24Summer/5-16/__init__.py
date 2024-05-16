
def differenceOfSum(nums) -> int:
    sum_num = sum(nums)
    nums_2 = []
    for i in range(len(nums)):
        if nums[i] < 10:
            nums_2.append(nums[i])
        elif nums[i] == 10:
            nums_2.append(1)
        elif 10 < nums[i] < 100:
            nums_2.append(int(nums[i] / 10))
            nums_2.append(nums[i] % 10)
        elif nums[i] == 100:
            nums_2.append(1)
        elif 100 < nums[i] < 1000:
            nums_2.append(int(nums[i] / 100))
            rest = nums[i] % 100
            nums_2.append(int(rest / 10))
            nums_2.append(rest % 10)

    sum_num2 = sum(nums_2)
    return abs(sum_num - sum_num2)


print(differenceOfSum([1, 15, 6, 3]))

