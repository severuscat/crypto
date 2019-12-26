def gcdex(a, b):
    if a == 0:
        x = 0
        y = 1
        return x, y, b
    x1, y1, d = gcdex(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return x, y, d


def get_reverse_by_mod(public_exponent, phi_n):
    d, y, v = gcdex(public_exponent, phi_n)
    d = (d + phi_n) % phi_n
    return d


def get_keys(mode):  # get private, public exponent and modulo
    p = 31
    q = 43
    public_exponent = 131

    n = p * q
    phi_n = (p - 1) * (q - 1)

    if mode == 'public':
        return public_exponent, n
    if mode == 'private':
        private_exponent = get_reverse_by_mod(public_exponent, phi_n)
        assert (public_exponent * private_exponent) % phi_n == 1
        return private_exponent, n


def pow_mod(a, p, n):  # fast pow
    if p == 0:
        return 1
    x = pow_mod(a, p // 2, n)
    if (p % 2) == 1:
        return (x * ((x * a) % n)) % n
    return (x * x) % n


def encrypt(message):
    e, n = get_keys(mode='public')
    c = pow_mod(message, e, n)
    return c
