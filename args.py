# *args : when you are not aware of the Number of arguments that you were passing

# def substraction(*args):

#     return sum(args)

# result = substraction(10,20,30,50,100,200,500)

# print(result)


# Lambda function : Simple one liner Functions
# without function name

# addition = lambda a,b:print(a+b)

# addition(10,20)


# # Map and filter : 
# # Map : accessing the Values and Manipulating the Values.

# numbers = [1,2,3,4,5,6,7,8,9,10]

# squaredNumbers = list(map(lambda x: x**2,numbers))

# print(squaredNumbers)


# evenNumbers = list(filter(lambda x: x % 2 == 0,numbers))

# print(evenNumbers)

values = ['a','b','c','d','a','b','a','c','g']
rl = list(filter(lambda x: x!='a',values))
print(rl)


# add= ['a','g','d','c','a','w','g','i','b','f']
# replacedvalues = list(map(lambda x: 'shreyas' if x=='a' else x,add))
# print(replacedvalues)