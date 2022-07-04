import random, string

chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + "%&$£/!=?^.;,:_-<>*+@#"

print(''.join(random.choice(chars) for i in range(15)))
