import keyword


def print_kws():
	for word in keyword.kwlist:
		print(word)

# print(keyword.kwlist)

a = 4 > 3

print(a) # returns True

print(type(a)) # returns bool

print(4 > 3) # returns true

print(type(4 > 3)) # returns bool

print("\n\n")

d = {
	'Name' : 'Angela Merkel',
	'Country': 'Germany',
	'Profession' : 'Chancelor',
	'Age' : 64
}

print(d['Name'],d['Age'])

print('Hello','World')

print('Hello'+'World')

print("\n\n")