# all set methods in python
# 1.add()

x={1,2,3,"dog","cat","ant"}
x.add("flipcart")
print("1)",x)


#2.clear()
def f():
	x={1,2,3,"dog","cat","ant"}
	x.clear()
	print("2)",x)
f()

#3.copy()
def f():
	x={1,2,3,"dog","cat","ant"}
	x.copy()
	print("3)",x)
f()

#4.difference()
def f():
	x={1,2,3,"dog","cat","ant"}
	y={1,2,3,"dog","cat","hen"}
	z=x.difference(y)
	print("4)",z)
f()


#5.difference update()
def f():
	x={1,2,3,"dog","cat","ant"}
	y={1,2,3,"dog","cat","hen"}
	z=x.difference_update(y)
	print("5)",z)
f()


#6.discard()
def f():
	x={1,2,3,"dog","cat","ant"}
	y={1,2,3,"dog","cat","hen"}
	x.discard("dog")
	print("6)",x)
f()
	
#7.intersection()
def f():
	x={1,2,3,"dog","cat","ant"}
	y={1,2,3,"dog","cat","hen"}
	z=x.intersection(y)
	print("7)",z)
f()

#8.intersection update()
def f():
	x={1,2,3,"dog","cat","ant"}
	y={1,2,3,"dog","cat","hen"}
	x.intersection_update(y)
	print("8)",y)
f()

#9.update()
def f():
	x={1,2,3,"dog","cat","ant"}
	y={1,2,3,"dog","cat","hen"}
	x.update(y)
	print(x)
f()










