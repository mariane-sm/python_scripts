#
def x_to_the_power_of_y(x,y):
	if y == 0:
		return 1
	elif y < 0:
		y = -y
		x = 1.0 / x
	
	acc = x
	for i in range(1,y):
		acc = x * acc 
	return acc

print x_to_the_power_of_y(3,4) #81
print x_to_the_power_of_y(3,0) #1
print x_to_the_power_of_y(3.0/2.0,-2) #4/9 (0.444444...)
