#reverse the string
s="hello world"[::-1]
print(s)

#replace the string
s="hello world"
print(s.replace("hello world" ,"new string"))

#merge two string

s1="hello  "
s2="world"

print(s1 + s2)

#find char
s1="hello world"
a=s1.find('s')
if a ==(-1):
    print("FALSE")
else:
    print("TRUE")

#split string
s1="hello world"
print(s1.split())

#dictionry

shyam={'key1':10,'key2':20,'key3':30}
shyamm={
    'address':{
        'key7':20

}
}
shyam.update({'key4':40})
shyam.popitem()
shyam.pop('key2')
print(shyam)
shyam2=shyam.copy()
print(shyam2)
print(shyam2.get('key1'))
print(shyamm['address']['key7'])

#merge two dictionry
s1={'k1':10,'k2':20}
s2={'k3':30,'k4':40}
s3=s1.copy()
s3.update(s2)
print(s3)


a=int(input())
print(a)
l1=list()
for i in range(1,11):

    s=a*i
    l1.append(s)

print(l1)

#dictionry task

# employee={
#     'emp_id':input('Enter Employee ID: '),
#     'emp_name':input('Enter Employee Name:'),
#      'salary':int(input('Enter salary')),
#     'department':input('enter department:')
# }
# print(employee)

l2=list()
a=int(input("enter the no of students"))

for i in range(0,a):
    l2.append(input("enter name of student"))

print(l2)
l=list()
c=0
for j in l2:
   if j.__contains__('patel'):
       c=c+1


print(c)

