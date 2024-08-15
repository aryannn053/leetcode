class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        salary = {5: 0, 10: 0}

        for i in bills:
            if i == 5:
                salary[5] += 1
            elif i == 10:
                if salary[5] == 0:
                    return False
                salary[5] -= 1
                salary[10] += 1
            elif i == 20:
                if salary[10] > 0 and salary[5] > 0:
                    salary[10] -= 1
                    salary[5] -= 1
                elif salary[5] >= 3:
                    salary[5] -= 3
                else:
                    return False
        
        return True