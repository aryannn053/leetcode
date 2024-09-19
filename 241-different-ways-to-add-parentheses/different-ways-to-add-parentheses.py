class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        salida = []
        for i in range(1, len(expression)):
            op = expression[i]
            if op in '+-*/':
                m1 = expression[:i]
                m2 = expression[i+1:]
                l1 = self.diffWaysToCompute(m1)
                l2 = self.diffWaysToCompute(m2)
                for num1 in l1:
                    for num2 in l2:
                        todo = '%d%s%d'%(num1, op, num2)
                        salida.append(eval(todo))
        if len(salida)==0:
            return [int(expression)]
        return salida