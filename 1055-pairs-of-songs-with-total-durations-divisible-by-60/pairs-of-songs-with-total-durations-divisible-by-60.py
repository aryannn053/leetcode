class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        arr=[0]*60
        count=0
        for i in range(len(time)):
            temp=time[i]%60
            count+=arr[-temp%60]
            arr[temp]+=1
        return count