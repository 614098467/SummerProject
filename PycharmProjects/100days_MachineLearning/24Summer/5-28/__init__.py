def getRow(rowIndex: int):
    result = []
    row0 = [1]
    row1 = [1, 1]
    result.append(row0)
    result.append(row1)
    if rowIndex >= 2:
        for i in range(2, rowIndex+1):
            row_result = []
            row_result.append(result[i - 1][0])
            for j in range(1, len(result[i - 1])):
                number = result[i - 1][j - 1] + result[i - 1][j]
                row_result.append(number)
            row_result.append(result[i - 1][-1])
            result.append(row_result)
    return result[rowIndex]

print(getRow(3))
