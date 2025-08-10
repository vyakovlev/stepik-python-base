import random
from string import ascii_lowercase, ascii_uppercase

chars = ascii_lowercase + ascii_uppercase
random.seed(1)

N = int(input())
# N = 8


def random_email(max_size: int):
    while True:
        rnd_email = ""
        for i in range(0, max_size):
            rnd_email += chars[random.randint(0, len(chars)-1)]
        yield rnd_email + "@mail.ru"

emails = random_email(N)
for i in range(0, 5):
    print(next(emails))
