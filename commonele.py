#Write a Python program that takes two lists as input and returns a new list containing elements that are common to both lists, without any duplicates.
a = [5,9,3,1,78,4]
b = [90,4,67,3,1,78]
c = set(a)
d = set(b)
print(d.intersection(c))