from array import *
a=array ('i',[10,20,30,40,50])
print(a)
print(a[2])
print(a[-1])
print(a[2:4])
print(a[:2])
print(a[2:])
a.append(40)
print(a)
a.extend([38,44,55])
print(a)
a.remove(38)
print(a)
a.pop(2)
print(a)