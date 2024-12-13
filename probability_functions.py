from math import factorial

# Binomial coefficient for use with hypergeometric calculation
def binomial_coefficient(n, r):
    try:
        result = factorial(n) / (factorial(r) * factorial(n-r))
        return result
    except:
        pass

def hypergeometric_probability(N, K, n, k):
    result = (binomial_coefficient(K, k) * binomial_coefficient(N-K, n-k)) / binomial_coefficient(N, n)
    result = round(result, 2)
    return result