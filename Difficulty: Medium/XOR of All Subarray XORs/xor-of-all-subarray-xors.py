class Solution:
    def subarrayXor(self, arr):
        ret=0
        lth=len(arr)
        for ix,ve in enumerate(arr):
            if (ix+1)*(lth-ix)&1:
                ret^=ve
        return ret