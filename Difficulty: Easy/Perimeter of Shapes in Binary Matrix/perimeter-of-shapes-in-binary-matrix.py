class Solution:
     def findPerimeter(self, mat):
          # code here
          n = len(mat)
          m = len(mat[0])
          p = 0

          for i in range(n):
               row = mat[i]
               for j in range(m):
                    if row[j] == 1:
                         p += 4

                         if i+1 < n and mat[i+1][j] == 1:
                              p -= 2
                         if j+1 < m and row[j+1] == 1:
                              p -= 2
          return p