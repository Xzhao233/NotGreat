# 定义一个递归函数，返回第n项斐波那契数
def fib(n):
    if n <= 1: # 基本情况
        return n
    else: # 递归情况
        return fib(n-1) + fib(n-2)

# 定义返回斐波那契列表的函数

def fib_list(u):
    list_for_fib = []
    for i in range(u+1):
        list_for_fib.append(fib(i))
    return list_for_fib
        
