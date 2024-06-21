class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n=len(customers)
        ans=mx=temp=0
        for i in range(n):
            if not grumpy[i]:
                ans+=customers[i]
                customers[i]=0
            else:
                temp+=customers[i]
            if i>=minutes:
                temp-=customers[i-minutes] 
            mx=max(mx,temp)
        return ans+mx