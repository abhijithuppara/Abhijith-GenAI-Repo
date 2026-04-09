# Arbitary Arguments - "*"

def test_num(*nums):
    print(nums)
    print(sum(nums))
    print(len(nums))
    print(max(nums))

test_num(10,20,30,40)




# def set_num():

#     user = "Abhijith"
#     password = "Chimmy"

#     if(user == "Abhijith" and password == "Chimmy"):
#         print("Rohan")
#     else:
#         print("Rishi")


# set_num()