class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        l = len(scores)
        ageScoreComb = [[ages[i], scores[i]] for i in range(l)]
        ageScoreComb = sorted(ageScoreComb, key = lambda x : (x[0], x[1]))
        dp = [i[1] for i in ageScoreComb]

        for i in range(l):
            for j in range(0, i):
                if ageScoreComb[j][1] <= ageScoreComb[i][1]:
                    dp[i] = max(dp[i], ageScoreComb[i][1] + dp[j])
                elif ageScoreComb[i][0] == ageScoreComb[j][0]:
                    dp[i] = max(dp[i], ageScoreComb[i][1] + dp[j])

        return max(dp)