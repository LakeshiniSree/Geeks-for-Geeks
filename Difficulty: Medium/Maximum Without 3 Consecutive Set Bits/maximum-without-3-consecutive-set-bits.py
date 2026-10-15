class Solution:
    def maxValue(self, n: int) -> int:
        # Convert the number to a list of bits (MSB to LSB)
        bits = [int(b) for b in bin(n)[2:]]

        # Scan from left to right to find triplets of 1s
        for i in range(len(bits) - 2):
            if bits[i] == 1 and bits[i+1] == 1 and bits[i+2] == 1:
                # Turn off the rightmost bit of the triplet to maximize value
                bits[i+2] = 0

        # Convert the bit list back to an integer
        ans = 0
        for b in bits:
            ans = (ans << 1) | b

        return ans
