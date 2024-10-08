def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        result = 1 
        for i in range(2, x + 1):
            result *= i
        return result
    
def virashenie(n, m):
    fact_n = factorial(n)
    fact_m = factorial(m)
    fact_n_minus_m = factorial(n - m)

    result = (fact_n + fact_m) / fact_n_minus_m
    return result

n = 5
m = 3
gotovi_result = virashenie(n, m)
print(gotovi_result)