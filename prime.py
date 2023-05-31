def ispr(n):
    """
    判断一个整数n是否是质数

    参数：
    n -- 要判断的整数

    返回值：
    如果n是质数，返回True；否则，返回False。
    """

    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

def getpr(a, b=1):
    primes = []
    addpr = []
    for j in range(a-b):
        addpr.append(a - b + j - 1)
    for i in addpr:
        if ispr(i) == True:
            primes.append(i)
    return primes
