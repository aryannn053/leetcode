class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]
        idx = 0

        while idx < len(formula):
            if formula[idx] == "(":
                stack.append(defaultdict(int))
                idx += 1

            elif formula[idx] == ")":
                count = stack.pop() 

                multi, idx = self.getCount(formula, idx)

                for key,value in count.items():
                    count[key] = value * multi
                
                for atom in count:
                    stack[-1][atom] += count[atom] 

            else:
                elem,idx = self.curElem(formula,idx) 
                no, idx = self.getCount(formula, idx) 
                if elem:
                    stack[-1][elem] += no

        result = ""
          
        for key,value in sorted(stack[0].items()):
            if value > 1:
                result += "{}{}".format(key,value)
            else:
                result += key 
        
        return result
    
    def curElem(self, formula, idx):
        elem = formula[idx]
        idx += 1

        while idx < len(formula) and formula[idx].islower():
            elem += formula[idx]
            idx += 1
        
        return elem, idx - 1 
    
    def getCount(self, formula, idx):
        count = 0
        idx += 1

        number = "" 
        while idx < len(formula) and formula[idx].isdigit():
            number += formula[idx]
            idx += 1
        
        if number:
            count = int(number)
        else:
            count = 1
        
        return count, idx