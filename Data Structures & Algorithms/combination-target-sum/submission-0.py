class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        res=[]
        def bt(i,curr,total):
            if  total == target:
                res.append(curr.copy())
                return
            for j in range(i,n):
                if total+nums[i]>target:
                    return
                curr.append(nums[j])
                bt(j,curr,total+nums[j])
                curr.pop()
            
        

        bt(0,[],0)

        return res