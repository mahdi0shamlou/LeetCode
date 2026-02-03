class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # اندازه‌های رشته و الگو
        m, n = len(s), len(p)
        
        # ساخت ماتریس my_matrix
        my_matrix = [[False] * (n + 1) for _ in range(m + 1)]
        
        # مقداردهی اولیه
        my_matrix[0][0] = True  # رشته و الگوی خالی با هم تطبیق دارند
        
        # رسیدگی به الگوهایی که شامل '*' هستند
        # در اینجا الگو هایی که رشته ی ورودی طولی با ۰ دارد رو درست قرار میدهیم 
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                my_matrix[0][j] = my_matrix[0][j - 2]
            print(my_matrix)
        
        # پر کردن ماتریس my_matrix
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    my_matrix[i][j] = my_matrix[i - 1][j - 1]
                elif p[j - 1] == '*':
                    my_matrix[i][j] = my_matrix[i][j - 2] or (my_matrix[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
        
        return my_matrix[m][n]

x = Solution()
x.isMatch(s="aaaa", p="a*b*")