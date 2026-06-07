class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = defaultdict()
        ans =[]
        for n in nums:
            if n in res:
                res[n] +=1
            else:
                res[n] = 1
        
        for i in range(k):
            max_f = max(res, key=res.get)
            ans.append(max_f)
            res[max_f] = 0

        return ans