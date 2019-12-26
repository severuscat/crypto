import random

L = 40


class Encryptor:
    def __init__(self, key):
        self.block_size = 256
        self.i = 0
        self.j = 0
        self.s = list()
        self.key = key

        for ind in range(self.block_size):
            self.s.append(ind)
        ind_for_change = 0
        for ind in range(self.block_size):
            ind_for_change = (ind_for_change + self.s[ind] + key[ind % L]) % self.block_size
            a, b = self.s[ind_for_change],\
                   self.s[ind]
            self.s[ind], self.s[ind_for_change] = a, b

    def generate_k(self):
        self.i = (self.i + 1) % self.block_size
        self.j = (self.j + self.s[self.i]) % self.block_size
        self.s[self.i], self.s[self.j] = self.s[self.j], self.s[self.i]
        t = (self.s[self.i] + self.s[self.j]) % self.block_size
        return self.s[t]

    def encode(self, msg):
        return self.generate_k() ^ msg


class Decryptor:
    def __init__(self, key):
        self.block_size = 256
        self.i = 0
        self.j = 0
        self.s = list()
        self.key = key

        for ind in range(self.block_size):
            self.s.append(ind)
        ind_for_change = 0
        for ind in range(self.block_size):
            ind_for_change = (ind_for_change + self.s[ind] + key[ind % L]) % self.block_size
            self.s[ind], self.s[ind_for_change] = self.s[ind_for_change], self.s[ind]

    def generate_k(self):
        self.i = (self.i + 1) % self.block_size
        self.j = (self.j + self.s[self.i]) % self.block_size
        self.s[self.i], self.s[self.j] = self.s[self.j], self.s[self.i]
        t = (self.s[self.i] + self.s[self.j]) % self.block_size
        return self.s[t]

    def decode(self, e_msg):
        return self.generate_k() ^ e_msg


def gen_key():
    return [random.randint(-127, 128) for i in range(L)]


def print_by_bit(m):
    for i in range(8):
        print(m & (1 << i), sep='')


def test():
    key = gen_key()
    encoder = Encryptor(key)
    decoder = Decryptor(key)
    print([print_by_bit(k) for k in key], sep='')
    msg = 'But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and ' \
          'I will give you a complete account of the system, and expound the actual teachings of the great explorer ' \
          'of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, ' \
          'because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter ' \
          'consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to ' \
          'obtain pain of itself, because it is pain, but because occasionally'
    for c in msg:
        a = ord(c)
        enc = encoder.encode(a)
        dec = decoder.decode(enc)
        print('msg:', c,
              'encr:', chr(enc),
              'decr:', chr(dec))
        assert c == chr(dec)


if __name__ == '__main__':
    test()
