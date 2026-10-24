class Solution:
    def isPossible(self, n: int, m: int, s: str) -> bool:
        max_x = max_y = min_x = min_y = x = y = 0
        for c in s:
            match c:
                case "U":
                    x += 1
                    max_x = max(max_x, x)
                case "D":
                    x -= 1
                    min_x = min(min_x, x)
                case "L":
                    y -= 1
                    
                    min_y = min(min_y, y)
                case "R":
                    y += 1
                    max_y = max(max_y, y)
        return max_x - min_x < n and max_y - min_y < m