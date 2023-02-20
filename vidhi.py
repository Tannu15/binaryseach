# Python program to find the
# maximum of two numbers


def maximum(a, b):
	
	if a >= b:
		return a
	else:
		return b
	
# Driver code
a = input("Enter First Number: ")
b = input("Enter Second Number: ")
print(maximum(a, b))
