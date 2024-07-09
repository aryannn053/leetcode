class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait=0
        total=0
        n=len(customers)
        for arri,time in customers:
            if(wait<=arri):
                wait=arri+time
            else:
               wait=wait+time
            total+=wait-arri
        return total/n