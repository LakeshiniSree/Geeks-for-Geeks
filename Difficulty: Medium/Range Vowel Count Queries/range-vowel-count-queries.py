class Solution:
    def countVowels(self, s: str, queries: list[list[int]]) -> list[int]:
        # code here
        pre = [0] * len(s)
        res = []

        for i in range(len(s)):
            if s[i] in {'a','i','e','u','o'}:
                if i == 0:
                    pre[i] +=1
                else:
                    pre[i] = pre[i-1]+1

            elif i:
                pre[i]= pre[i-1]

        for i,j in queries:
            count = pre[j] - pre[i]

            if s[i] in {'a','i','e','u','o'}:
                count+=1

            res.append(count)


        return res

