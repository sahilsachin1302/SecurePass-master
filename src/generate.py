import random
import string


def password_generator():
    len_password = random.randint(8, 16)
    password = ''.join(random.choice(string.ascii_letters +
                       string.digits + string.punctuation) for i in range(len_password))
    return password


if __name__ == '__main__':
    password_generator()
