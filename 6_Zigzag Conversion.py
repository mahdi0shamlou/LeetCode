class Solution:
    def convert(self, s: str, numRows: int) -> str:

        result = []
        numRows_counter = 0
        numRows_counter_way = 1

        for i in s:
            result.append("")
            result[numRows_counter] = str(result[numRows_counter]) + str(i)

            if numRows_counter + 1 == numRows:
                numRows_counter_way = -1
            if numRows_counter - 1 < 0:
                numRows_counter_way = +1

            if numRows_counter_way == 1:
                numRows_counter = numRows_counter + 1
            else:
                numRows_counter = numRows_counter - 1

        final_res = ""
        for i in result:
            final_res = final_res + i
        print(result)
        return final_res



x = Solution()
r = x.convert(s = "PAYPALISHIRING", numRows = 4)
print("%" * 100)
print(r)
print('PINALSIGYAHRPI')

x = Solution()
r = x.convert(s = "AB", numRows = 2)
print("%" * 100)
print(r)
print('AB')