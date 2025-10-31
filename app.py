print("hello world")
#primitive 
a = 30 # integer
b = "56" #string
c = True# boolen
#non primitive
e = (23,35,18)# tuple
f = [23,54,89]#list
print(type(f))
j = {23,90,12}#set
print(type(j))
h = {id : '23'}#dict
print(type(h))

print(e)

def app(a,b):
   
    return print(a+b)
app(23,25)
age = int(input("Enter your age "))
if(age>=18):
    print("eligible for vote")
else:
    print("Not eligible for vote")

