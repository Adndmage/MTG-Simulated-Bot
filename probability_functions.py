from math import factorial

# Binomial coefficient for use with hypergeometric calculation
def binomial_coefficient(a, x):
    try:
        result = factorial(a) / (factorial(x) * factorial(a-x))
        return result
    except:
        pass

def hypergeometric_probability(N, a, n, x):
    result = (binomial_coefficient(a, x) * binomial_coefficient(N-a, n-x)) / binomial_coefficient(N, n)
    result = round(result, 2)
    return result