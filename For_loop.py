#iterable 

list = [1,2,3]

for i in list:
	print(i)

print("--------------------")

for i in list:
	print("Hello")

print("--------------------")

for num in list:
	if num%2==0:
		print(num)
	else:
		print("Odd Num :",num)	

print("--------------------")

sum = 0

for num in list:
	sum += sum + num

print("Sum :",sum)

print("--------------------")


str ="Hello World"

for letter in str:
	print(letter)


print("--------------------")


for letter in 'Hello World':
	print(letter)


print("--------------------")

tup = (1,2,3)

for item in tup:
	print(item)

print("--------------------")

list = [(1,2),(3,4),(5,6),(7,8),(9,10)]

for item in list:
	print(item)


print("--------------------")

list = [(1,2),(3,4),(5,6),(7,8),(9,10)]

print(len(list))

print("--------------------")

for a,b in list:
	print(b)
print("--------------------")
for a,b in list:
	print(a)

print("--------------------")

list = [(1,2,3),(4,5,6),(7,8,9),(10,11,12)]

for item in list:
	print(item)

print("--------------------")

for a,b,c in list:
	print(b)
print("--------------------")


d = {'k1':1,'k2':2 ,'k3':3}
for item in d:
	print(item)


print("--------------------")


d = {'k1':1,'k2':2 ,'k3':3}
for item in d.items():
	print(item)

print("--------------------")


d = {'k1':5,'k2':2 ,'k3':3}
for value in d.values():
	print(value)


print("--------------------")


d = {'k1':5,'k2':2 ,'k3':3}
for key,value in d.items():
	print(key,value)