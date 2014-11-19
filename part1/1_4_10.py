def sumup_interger(a,b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        raise TypeError("can not use float")

result = sumup_interger(1.1,4)
print result
