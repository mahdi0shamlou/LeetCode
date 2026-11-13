class Solution:
    def intToRoman(self, num: int) -> str:

        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]

        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        result = ""

        for i in range(len(values)):

            count = num // values[i]

            result += symbols[i] * count

            num = num % values[i]

            if num == 0:
                break

        return result
