from itertools import combinations

def subsequences(arr):
    result = []
    for r in range(len(arr)+1):
        result.extend(combinations(arr, r))
        print(result)
    r = [sum(sub) for sub in result]
    return r

# 示例
my_list = [1, 2, 3]
result = subsequences(my_list)
print(result)