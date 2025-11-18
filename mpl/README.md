# Modern Programming Languages"
1. dices.py
2. biggest.py 



The function **primes(n)** checks if a number is a prime number.

```python
def prime(n):
    is_prime = True
    if n == 1:
        return False
    else:
        for i in range(2, (int)(n//2)+1):
            if n % i == 0:
                is_prime = False
                break
        return is_prime        

```
In this loop we go to the half of n.

