class Solution:
    def findMax(self, n):
            if n <= 9:
                return n
            s = str(n)
            m = len(s)
            if s[1] >= "8" and all(s[i] == "9" for i in range(2, m)):
                return n
            i = 1
            while s[i] == "9":
                i += 1
            output = [s[:i - 1]]
            output.append(chr(ord(s[i - 1]) - 1))
            output.append("9" * (m - i))
            return int("".join(output))
