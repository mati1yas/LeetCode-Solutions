class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        countA = 0
        deletions = 0
        for i in range(n - 1, -1, -1):
            if s[i] == 'a':
                countA += 1
            elif s[i] == 'b':
                if countA > 0:
                    countA -= 1
                    deletions += 1
        return deletions