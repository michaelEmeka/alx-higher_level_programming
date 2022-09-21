#!/usr/bin/python3
for n in range(0, 99):
	print("{} = 0x".format(n), end="")
	if n < 10:
		print(n)
	elif n < 16:
		print(chr(97 + n % 10))
	else:
		print(n // 16, end="")
		if n % 16 > 9:
			print(chr((97 + (n % 16 % 10))))
		else:
			print(n % 16)
