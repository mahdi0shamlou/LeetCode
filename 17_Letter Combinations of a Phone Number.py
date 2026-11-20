class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        phone_maps = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = [""]

        for digit in digits:

            new_result = []

            for combination in result:

                for letter in phone_maps[digit]:

                    new_result.append(combination + letter)

            result = new_result

        return result