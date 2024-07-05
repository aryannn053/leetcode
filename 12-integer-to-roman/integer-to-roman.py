class Solution:
    def intToRoman(self, num: int) -> str:
        d1={
            1000:"M",
            900:"CM",
            500:"D",
            400:"CD",
            100:'C',
            90:"XC",
            50:"L",
            40:"XL",
            10:"X",
            9:"IX",
            5:'V',
            4:"IV",
            1:"I"
        }
        out = ""
        while num > 0:
            if num <= 3:
                out += num*d1[1]
                return out
            for i in d1:
                while num >= i:
                    num -= i
                    out += d1[i]
        return out