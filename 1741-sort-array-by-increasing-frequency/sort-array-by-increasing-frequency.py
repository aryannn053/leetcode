class Solution:
    def sort(self,nums: list)-> list:
        i=0
        while(i<len(nums)):
            swapped=0
            j=0
            while(j<len(nums)-i-1):
                if nums[j]>nums[j+1]:
                    
                    nums[j+1],nums[j]=nums[j],nums[j+1]
                    swapped=1
                j+=1
            if swapped==0:
                break
            i+=1
        return(nums)

    def frequencySort(self, nums: List[int]) -> List[int]:
        dic=dict()
        res=[]
        new=[]
        
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1

        for i in dic:
            if dic[i] not in res:
                res.append(dic[i])
        res=Solution.sort(self,res)

        for i in res:
            temp=[]
            for j in dic:
                if dic[j]==i:
                    temp+=[j]*i
            if len(temp)>1:
                temp=Solution.sort(self,temp)
                temp.reverse()
            new+=temp
        return new   