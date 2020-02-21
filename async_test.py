def highest_prime_below(x):
    print("Highest Prime below {}".format(x))
    for y in range(x-1, 0, -1):
        if is_prime(y):
    
def main():
    highest_prime_below(100000)
    highest_prime_below(10000)
    highest_prime_below(1000)    
