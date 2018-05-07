class Solution:
    # @param A : tuple of strings
    # @return an integer
   

    def isValidSudoku(self, A):
       
        for i in range(9):
            if not self.checklist([A[i][j] for j in range(9)]) or \
               not self.checklist([A[j][i] for j in range(9)]):
                return 0
        for i in range(3):
            for j in range(3):
                if not self.checklist([A[m][n] for n in range(3 * j, 3 * j + 3) \
                                                     for m in range(3 * i, 3 * i + 3)]):
                    return 0
        return 1

    def checklist(self, lis):
        lis = filter(lambda x: x != '.', lis)
        return len(set(lis)) == len(lis)
