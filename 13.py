class Solution:
    def romanToInt(self, s: str) -> int:
        ans, temp = 0, 0
        rom_to_dec = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in s[::-1]:
            if rom_to_dec[i] >= temp:
                ans += rom_to_dec[i]
            else:
                ans -= rom_to_dec[i]
            temp = rom_to_dec[i]
        return ans
