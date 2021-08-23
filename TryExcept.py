try:
	x=int(input("Type number here"))
except (TypeError,ValueError):
	print("invalid input")