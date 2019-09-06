def addBit(a,b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

def subBit(a,b):
    while b != 0:
        borrow = (~a) & b
        a = a ^ b
        b = borrow << 1
    return a

print(addBit(3,1))
print(subBit(54,44))