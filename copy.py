#Write a Python program that takes a list as input and creates a shallow copy of the list using the copy() method or the slicing technique [:].
a = [3,8,9,2,6]
#b = a[:]
b = a.copy()
print(b)