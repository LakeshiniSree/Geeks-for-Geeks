class Solution:
    def searchWord(self, mat, word):
            from itertools import product
            n, m, k = len(mat), len(mat[0]), len(word) - 1

            def is_match(x, y, dx, dy):
                if not (0 <= x + k * dx < n and 0 <= y + k * dy < m):
                    return False
                for i, c in enumerate(word):
                    if mat[x + i * dx][y + i * dy] != c:
                        return False
                return True

            locations = []
            diffs = [x for x in product([-1, 0, 1], repeat = 2) if x != (0, 0)]
            for x in range(n):
                for y in range(m):
                    for dx, dy in diffs:
                        if is_match(x, y, dx, dy):
                            locations.append((x, y))
                            break
            return locations
        
        