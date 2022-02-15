def f():
	x=[1,2,3]
	y=[1,2,3]
	print(x is y)

	x=[1,2,3]
	y=[1,3,6]
	print(x is not y)
	print(x is y)

	a=["a",1,2]
	b=["b",7,8]
	print(x is not y)
f()