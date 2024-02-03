class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        int_num=0
        roman_str=s

        for i in range(len(roman_str)):
            if i+1 <len(roman_str) and roman_dict[roman_str[i]]<roman_dict[roman_str[i+1]]:
                int_num-=roman_dict[roman_str[i]]
            else:
                int_num+=roman_dict[roman_str[i]]

        return int_num


s1=Solution()
print(s1.romanToInt('III'))
print(s1.romanToInt('LVIII'))
print(s1.romanToInt('MCMXCIV'))