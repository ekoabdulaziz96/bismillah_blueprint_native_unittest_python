# keyword : bilangan prima, prime,
def check_is_prime(n: int) -> bool:
    """function to check is `n` is prime number
    """
    try:
        is_prime = True
        if n <= 1:
            return False

        p = 2
        while p*p <= n:
            if n in range(p*p, n+1, p):
                is_prime = False
                break
            p += 1

        return is_prime

    except Exception as e:
        raise BaseException(e)
