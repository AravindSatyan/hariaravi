#--recursion--

result=[]
def rec_fibo(n):
    if n==1:
        result.append(0)
        result.append(1)
        return result
    else:
        rec_fibo(n-1)
    value=result[n-1]+result[n-2]
    result.append(value)
    return result
print('fibo series is: ', rec_fibo(5))