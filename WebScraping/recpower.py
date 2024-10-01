def powerfun(a,b):
    if b == 0:
        return 1
    elif b>0:
        if b%2==0:
            result=powerfun(a,b//2)
            return result*result
        else:
            result=powerfun(a,(b-1)//2)
            return a*result*result

