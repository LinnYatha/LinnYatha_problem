# WHT's solution for Luhn problem in WHT_branch
class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ","")

    def valid(self):
        total = 0
        if len(self.card_num) <= 1 or not self.card_num.isdigit():
            return False
        reversed_num = self.card_num[::-1]
        for j in reversed_num[::2]:
            total+= int(j)
        for i in reversed_num[1::2]:
            digit = int(i)
            double = digit* 2
            if double > 9:
                total += double-9
            else:
                total += double
            
        return total%10 == 0
    
# WHT's solution ends