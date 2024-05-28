class Solution:
    def MinNumberSubsequences(self, source: str, target: str)->int:
        # Write your code here
        source_len = len(source)
        target_len = len(target)
        if set(target) & set(source) != set(target):
            return -1
        pos_t = 0
        res = 0
        while pos_t < target_len:
            res+=1
            pos_s = 0
            # one iteration over source means using this once
            while pos_s < source_len and pos_t < target_len:
                if source[pos_s] == target[pos_t]:
                    pos_t += 1
                pos_s += 1
        return res
if __name__ == '__main__':
    solution = Solution()
    result1 = solution.MinNumberSubsequences("abc","abcbc")
    result2 = solution.MinNumberSubsequences("abc","acdbc")
    result3 = solution.MinNumberSubsequences("xyz","xzyxz")
    print(result1,result2,result3)
