class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count={}
        answer=[]
        for i in nums:
            freq_count[i]=freq_count.get(i,0)+1
        sorted_items=sorted(freq_count.items(),key=lambda item:item[1],reverse=True)
        for key,value in sorted_items[:k]:
            answer.append(key)
        return answer
        