class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_value={}
        freq=[[]for i in range(len(nums)+1)]
        for n in nums:
            count_value[n]=1+count_value.get(n,0)
        for n,c in count_value.items():
            freq[c].append(n)
        result=[]
        i=len(nums)
        print(freq)
        while k!=0 :
            if len(freq[i])!=0:
                result=result+freq[i]
                k=k-len(freq[i])
            i-=1
        return result
            
                
        
