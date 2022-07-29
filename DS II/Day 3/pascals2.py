class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return [int(factorial(rowIndex) / (factorial(rowIndex-i)*factorial(i))) for i in range(rowIndex + 1)]
