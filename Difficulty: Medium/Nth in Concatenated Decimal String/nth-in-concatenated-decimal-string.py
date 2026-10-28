class Solution:

    def nthCharacter(self, n):
        # code here
        digit = 1
        l = 9*10**(digit-1)*digit
        while n - l >= 0:
            n -= l
            digit += 1
            l = 9*10**(digit-1)*digit

        k = n//digit
        r = n%digit
        final_number = 10**(digit-1) - 1 + n//digit + (1 if r > 0 else 0)
        return str(final_number)[r-1]

