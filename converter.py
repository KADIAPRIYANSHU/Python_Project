v = int(input("What work do you want: Enter 1 to perform Rome To Decimal: Enter 2 to perform Decimal to Rome: "))

if v==1:
    s=input('Enter roman value: ').upper()
    def Roman_To_Int(s):
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            # specify more numerals if you wish
        }
        ans=0

        for i in range(len(s)):
            if i+1!=len(s) and d[s[i]] < d[s[i+1]]:
                ans = ans - d[s[i]]
            else:
                ans = ans + d[s[i]]
        return ans

    print(Roman_To_Int(s))

elif v==2:
    s=int(input('Enter decimal value: '))
    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num
    print(int_to_Roman(s))

