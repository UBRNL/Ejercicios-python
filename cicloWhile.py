def sumTo(aBound):
    
    TheSum = 0
    aNumber = 1
    while aNumber <= aBound:
        TheSum = TheSum + aNumber
        aNumber = aNumber +2
        return TheSum

print(sumTo(4))
print(sumTo(40))
