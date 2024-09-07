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

""" LYT SOLUTION """
def main():
    user_input = input("Enter your number: ").replace(" ", "")
    if check_valid(user_input):
        final_result = calculate(user_input)
        if int(final_result) % 10 == 0:
            print("Valid")
        else:
            print("Invalid")
        

def check_valid(user_input):
    if len(user_input) > 1 and user_input.isnumeric():
        return True

        
def calculate(user_input):
    result = 0
    for i in range(len(user_input)):
        if not(i % 2 == 0):
            after_calculate = int(user_input[i]) * 2
            if after_calculate > 9:
                after_calculate -= i
            result += after_calculate
        else:
            result += int(user_input[i])
    
    return result
        
    

if __name__ == "__main__":
    main()
""" END HERE """
    

