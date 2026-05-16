import random
import string

def generate_short_code(length=6):
    char = string.ascii_letters + string.digits
    short_url = "".join(random.choice(char)
                        for _ in range(length))
    return short_url