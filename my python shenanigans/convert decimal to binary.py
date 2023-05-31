def convert_to_base10(number, base):
	move = str(number)
	q = list(move)
	power = len(q) - 1
	# print(power)
	high = []
	for digit in q:
		digit = int(digit)
		figure = digit * (base ** power)
		# print(digit, base, power)
		high.append(figure)
		power = power - 1
	final = sum(high)
	# print(high)
	return final


def convert_from_base10(number, base):
	keeper = []
	while number >= base:
		j = number % base
		number = number // base
		keeper.append(j)
		# print(number, j)
	keeper.append(number)
	keeper.reverse()
	result = ''.join(str(item) for item in keeper)
	result = int(result)
	return result

# q = ["a", "b", "c"]
def vowels_in_a_string(string):
	# string = "I want to marry you today tomorrow and everyday"
	v1 = ord("a")
	v2 = ord("e")
	v3 = ord("i")
	v4 = ord("o")
	v5 = ord("u")
	v6 = ord("A")
	v7 = ord("E")
	v8 = ord("I")
	v9 = ord("O")
	v10 = ord("U")
	vowels = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10]
	q = list(string)
	# print(v1, v2, v3, v4, v5)
	count = 0
	for alphabet in q:
		for n in vowels:
			if ord(alphabet) == n:
				count = count + 1
	return count			

g = convert_to_base10(100000000, 2)
print(g)
	