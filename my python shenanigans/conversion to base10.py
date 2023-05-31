# a = "maker"
# print(a)

# def seperate(a):
# 	mod = 10 ** i
# 	b = (a % 10) // 1
# 	a = a - b
# 	c =  (a % 100) // 10
# 	a = a - c
# 	d = (a % 1000) // 100
# 	return d, c, b
# q = list(seperate(101))
# print(q)




def convert_to_base10(number, base):
	def seperate(number):
		b = str(number)
		c = list(b)
		q = []
		# wahala = "number does not exist in base"
		for d in c:
			e = int(d)
			q.append(e)
		return q
	q = seperate(number)
	rang = len(q)
	bulk = 0
	fin = 0
	final = []
	for item in q:
		rang = rang - 1
		bulk = base ** rang
		fin = item * bulk
		final.append(fin)
	answer = sum(final)
	return answer
def seperate(number):
		b = str(number)
		c = list(b)
		print(c)
		q = []
		# wahala = "number does not exist in base"
		for d in c:
			e = int(d)
			q.append(e)
		return q
r = convert_to_base10(100000000, 2)
print(r)
# h = seperate(200)
# print(h)