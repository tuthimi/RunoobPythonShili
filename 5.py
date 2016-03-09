__author__ = 'Administrator'
l=[]

for i in range(3):
    temp = int(raw_input("Input the %dth number:" %i)) 
    l.append(temp)

l.sort()
print(l)