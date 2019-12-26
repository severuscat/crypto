from RSA.encryptor import get_keys, pow_mod, encrypt


def decrypt(encrypted_message):
    d, n = get_keys(mode='private')
    message = pow_mod(encrypted_message, d, n)
    return message


def test():
    messages = (123, 12, 1, 89)
    for message in messages:
        print("message:", message,
              "\nencrypted:", encrypt(message),
              "\ndecrypted:", decrypt(encrypt(message)), "\n")
        assert decrypt(encrypt(message)) == message


if __name__ == '__main__':
    test()
