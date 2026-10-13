class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sortedCandidates = sorted(candidates)
        result = []
        def backTrack(curTarget, curSet, idx):
            if curTarget == 0:
                result.append(curSet.copy())
                return
            while idx < len(sortedCandidates):
                if sortedCandidates[idx] > curTarget:
                    break
                curSet.append(sortedCandidates[idx])
                backTrack(curTarget-sortedCandidates[idx], curSet, idx)
                curSet.pop()
                idx+=1
                
        backTrack(target, [], 0)
        return result
        