##set doesnt allows duplicate elements (Unique Collection) ,Unordered Collection,  Mutable



s1 = {1,2,3}
s1.add((4,5)) ##(4,5) is considered as a single element, thats why it is being added
print(s1)

s1 = {1,2,3}
s1.add([4,5])  ## Error bcz [4,5] is list - check whether it is mutable or immutable
print(s1)


# list1 = [1,2,3]
# list2 = [2,3,4]

# print(set(list1) & set(list2))

# s1 = frozenset([1,2,3])
# s1.add(4)





# s1 = {1,2,3}
# s2 = {1,2}

# print(s1.issubset(s2))
# print(s1.issuperset(s2))

# s1 = {1,2,3}
# s2 = {3,4,5}

# print(s1 - s2) ##Substraction of sets

# print(s1 | s2)  ##Union 

# print(s1 & s2) ##Intersestion

# print(s1 ^ s2)  ##Symmetric

#s1 = {1,2}
#s1.add(3)   ## For adding single element
#s1.update([4,5])  ## For adding multiple elements
#print(s1)

#s1 = {1,2,3}
#s2 = set[(1,2,3)]
#s3 = set()
#print(s1, s2, s3)