l=list(range(20))
print(l)
l[11]='cspit'
print(l)
print(l[2:15:4])
print(l[14:1:-4])
print(l[-1:-24:-1])
l.append(10)
print(l)
# l.insert(0,200)
# l.insert(0,300)
# l.insert(0,400)
print(l)
l=l+[1000,2000,3000,4000]
l.insert(6,'charusat')
print(l)
l.remove('cspit')
l.pop()
del l[0]
print(l)
a,b,*c,d,e=l
print(d)
print(5 in l)
print(l.index(5))
print(l.count(5)) #how many times 5 is present in list
l.reverse()
print(l)
l.remove('charusat')
l.sort(reverse=True)
print(l)
l2=sorted(l)# l is remaing same it is but it create new l2 with sorted
print(l2)


