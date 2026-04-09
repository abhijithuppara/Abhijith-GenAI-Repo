print( list(map( lambda num: num*num, [1, 2, 3, 4, 5]))) # -- shortcut to below code logic

# numbers = [1, 2, 3, 4, 5]
# def square(num):
#     return num*num

# res = map(square, numbers)
# print(list(res))




# def outer(num1):

#     def inner(num2):
#         print(num1+num2)

#     return inner

# x = outer(100) # --> here x contains inner method
# res = x(200)






#Anonymous function - A funtion without a name 

# res = lambda num1: num1 * num1
# print(res(5))



# Recursion
# def factorial(n):

#     if(n ==1):
#         return 1
    
#     return n * factorial(n-1)

# print(factorial(5))



# def test_num():
#     return 100,200,300

# res = test_num()
# print(res)
# print(type(res))

# num1,num2,num3 = test_num()  #This is called unpacking
# print(num1,num2,num3)







# Arbitary Arguments - "*"

# def test_num(*nums):
#     print(nums)
#     print(sum(nums))
#     print(len(nums))
#     print(max(nums))

# test_num(10,20,30,40)




# def set_num():

#     user = "Abhijith"
#     password = "Chimmy"

#     if(user == "Abhijith" and password == "Chimmy"):
#         print("Rohan")
#     else:
#         print("Rishi")


# set_num()