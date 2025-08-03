def is_prime(num):
    """
    Check if the number is prime
    """
    if num == 2 or num == 3 or num == 5 or num == 7:
        return True
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        return False
    return True


print(is_prime(73))
print(is_prime(75))
