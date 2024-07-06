
l = [1,3,5,6]
target = 2

def test(nums,target):
    left = 0
    right = len(nums)

    while left <= right:
        middle = int((left + right) / 2)
        if target < nums[middle]:
            right = middle
        elif target > nums[middle]:
            left = middle
        else:
            return middle

test(l,target)