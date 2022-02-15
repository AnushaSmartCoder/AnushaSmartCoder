x=['abc',"amazon",2,3]
x.append("grape")
print(x)

#2.clear()
x.clear()
print(x)

#3.copy()
x=['abc',"amazon",2,3]
y=x.copy()
print(y)

#4.count()
x=['abc',"amazon",2,3]
y=x.count("abc")
z=x.count("2")
print(z)
print(y)

#5.extend()
x=x=['abc',"amazon"]
y=['flicart',"myntra"]
z=x.extend(y)
print(x)

#6.index()
x=['abc',"amazon",2,3]
print(x[0])
print(x[0:2])
print(x[0:])

#7.insert()
x=['abc',"amazon",2,3]
x.insert(0,"gova")
print(x)

#8.pop()
x=['abc',"amazon",2,3]
x.pop()
print(x)

x.pop(0)
print(x)
#9.remove()
x=['abc',"amazon",2,3]
x.remove("amazon")
print(x)

#10.reverse()
x=['abc',"amazon",2,3]
x.reverse()
print(x)

#11.sort()
x=["abc","amazon","cat","book"]
x.sort()
print(x)






