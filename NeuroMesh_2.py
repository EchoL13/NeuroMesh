class Solution:
    def ParenthesesMatch(self, source: str):
        # Write your code here
        res = [" "  for _ in range(len(source))]
        left_parethesese_num = 0
        for i in range(len(source)):
            if source[i] == "(":
                left_parethesese_num += 1
            if source[i] == ")":
                if left_parethesese_num > 0:
                    left_parethesese_num -= 1
                else:
                    res[i] ='?'
        right_parenthese_num = 0
        for i in range(len(source)-1, -1, -1):
            if source[i] == ")":
                right_parenthese_num += 1
            if source[i] == "(":
                if right_parenthese_num > 0:
                    right_parenthese_num -= 1
                else:
                    res[i] ='x'
        print(source)
        print("".join(res))
if __name__ == '__main__':
    solution = Solution()
    result1 = solution.ParenthesesMatch("bge)))))))))")
    result2 = solution.ParenthesesMatch("((IIII))))))")
    result3 = solution.ParenthesesMatch("()()()()(uuu")
    result3 = solution.ParenthesesMatch("))))UUUU((()")
