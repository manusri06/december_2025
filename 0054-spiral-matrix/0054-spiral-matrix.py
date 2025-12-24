class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        n = len(matrix)
        m = len(matrix[0])
        
        rs, cs = 0, 0          
        rd, cd = n - 1, m - 1  
        result = []

        while rs <= rd and cs <= cd:
           
            for i in range(cs, cd + 1):
                result.append(matrix[rs][i])
            rs += 1

           
            for i in range(rs, rd + 1):
                result.append(matrix[i][cd])
            cd -= 1

            
            if rs <= rd:
                for i in range(cd, cs - 1, -1):
                    result.append(matrix[rd][i])
                rd -= 1

           
            if cs <= cd:
                for i in range(rd, rs - 1, -1):
                    result.append(matrix[i][cs])
                cs += 1

        return result
