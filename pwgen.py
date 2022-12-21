import random, string
from sys import argv

include_special_chars: bool = False
strlen = 15

if len(argv) >= 2:
	for a in argv:
		if a == "--special-chars":
			include_special_chars = True
		elif "-len=" in a:
			strlen = int(a.split("=")[1])

chars = string.ascii_lowercase + string.ascii_uppercase + string.digits

if include_special_chars:
	chars += "%&$£/!=?^.;,:_-<>*+@#"

print(''.join(random.choice(chars) for i in range(strlen)))
