class Solution:
    def formCoils(self, n: int) -> list[list[int]]:
        # code here

        m = 4*n
        value = lambda r, c: r*m + c + 1
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        top, bottom = 0, m-1
        left, right = 0, m-1
        r0, c0, dir0 = -1, 0, 0
        r1, c1, dir1 = m, m-1, 2
        cnt = 0
        ret1, ret2 = [], []

        def walk(r, c, dir, ret):
            nonlocal top, bottom, left, right
            dr, dc = dirs[dir]
            cnt = 0
            match dir:
                case 0: 
                    while r + dr <= bottom:
                        r += dr
                        ret.append(value(r, c))
                        cnt += 1
                    left += 1
                case 1:
                    while c + dc <= right:
                        c += dc
                        ret.append(value(r, c))
                        cnt += 1
                    bottom -= 1
                case 2:
                    while r + dr >= top:
                        r += dr
                        ret.append(value(r, c))
                        cnt += 1
                    right -= 1
                case 3:
                    while c + dc >= left:
                        c += dc
                        ret.append(value(r, c))
                        cnt += 1
                    top += 1
            return r, c, (dir+1)%4, cnt
        cnt = 0
        while cnt < m*m:
            r0, c0, dir0, cnt0 = walk(r0, c0, dir0, ret1)
            cnt += cnt0
            r1, c1, dir1, cnt1 = walk(r1, c1, dir1, ret2)
            cnt += cnt1
        return [ret1, ret2]