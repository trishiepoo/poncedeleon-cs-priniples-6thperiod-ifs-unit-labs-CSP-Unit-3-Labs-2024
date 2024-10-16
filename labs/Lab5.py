# Name:
# Period:
# Date:

# Write the function calcFedIncTax() that takes the individuals taxable
# income as a parameter and calculates the individuals federal income tax.

def calcFedIncTax(money):
    if money<= 9000:
        newmoney = money * 0.1
        return "The federal income tax for a taxable income of $" + str(money) + " is " + str(newmoney) + "."
    if money<= 37450:
        newmoney = (money + 0.15) * 922.5
        return "The federal income tax for a taxable income of $" + str(money) + " is " + str(newmoney) + "."
    if money<= 90750:
        newmoney = (money + 0.25) * 5156.25
        return "The federal income tax for a taxable income of $" + str(money) + " is " + str(newmoney) + "."
    if money<= 189300:
        newmoney = (money + 0.28) * 18381.25
        return "The federal income tax for a taxable income of $" + str(money) + " is " + str(newmoney) + "."
    if money<= 411500:
        newmoney = (money + 0.33) * 46075.25
        return "The federal income tax for a taxable income of $" + str(money) + " is " + str(newmoney) + "."
    if money<= 413200:
        newmoney = (money + 0.33) * 119401.25
        return "The federal income tax for a taxable income of $" + str(money) + " is " + str(newmoney) + "."
    else:
        newmoney = (money + 39.6) * 119996.5
        return "The federal income tax for a taxable income of $" + str(money) + " is " + str(newmoney) + "."