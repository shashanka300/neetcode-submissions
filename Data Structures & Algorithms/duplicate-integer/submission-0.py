class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        set_=set()
        for i in nums:
            if i in set_:
                return True
            set_.add(i)

        return False            

        
        