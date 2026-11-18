class Solution:
    def findXOR(self, l: int, r: int) -> int:

           def xor_up_to(n: int) -> int:
               match n % 4:
                   case 0: return n
                   case 1: return 1
                   case 2: return n + 1
                   case 3: return 0

           return xor_up_to(r) ^ xor_up_to(l - 1)