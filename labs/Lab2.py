# Name:
# Period:
#

# define a function getDiscountedPrice() that takes the original prince as a
# parameter and returns the price of the item after the discount is applied.

def getDiscountedPrice(price):
    if (price > 2000):
        return (price - ((price/100) * 10))
    if (price < 2000):
        return (price)
