li = [5,7,10,12,15,18,20]
m = 35

li2 = []
l = len(li)
n = 2**l

for i in range(n):
	temp = []*l
	li2.append(temp)

c = 2
d = 1
for x in range(l):
	t=0
	for y in range(t, n, c):
		t = y
		if t<n:
			for p in range(d):
				li2[t].insert(0,0)
				t+=1
			for j in range(d):
				li2[t].insert(0,1)
				t+=1

	# print(li2,"\n")
	c*=2
	d *= 2

for x in li2:
	for y in range(l):
		if x[y]:
			x[y] = li[y]

	print(x)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
temp1 = []
for x in li2:
	sum = 0
	temp = []
	for y in x:
		if y:
			temp.append(y)
			sum += y
			if sum==m and temp not in temp1:
				temp1.append(temp)
				print(temp,"",sum)




