import itertools
import string

def generate_passwords(charset, max_length):
    # Generator care produce toate combinațiile posibile de parole alfanumeric până la lungimea 10.
    for length in range(1, max_length + 1):
        for pwd_tuple in itertools.product(charset, repeat=length):
            yield ''.join(pwd_tuple)
