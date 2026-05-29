num1=int(input("Enter a number"))
num2=int(input("Enter a number"))

if num1>num2:
    print(num1,"is the maximum number")
else:
    print(num2,"is the maximum number")
------------------------------------------------------------------
    
age=int(input("Enter your age;"))
if age>=18:
   print("You're eligible to vote.")
else:
    print("You're not eligible to vote.")


num=int(input("Enter a number"))
if num%2==0:
    print(num,"is an even number")
else:
    print(num,"is an odd number")

---------------------------------------------------------------------
y=int(input("Enter your number 2;"))
z=int(input("Enter your number 3;"))

if x>y and x>z:
    print("Max is",x)
elif y>x and y>z:
    print("Max is",y)
else:
    print("Max is",z)

------------------------------------------------------------------------    

x=int(input("Enter your number 1;"))
y=int(input("Enter your number 2;"))
z=int(input("Enter your number 3;"))

if x>y:
    if x>z:
        print("Max is",x)
    else:
        print("Max is",z)
else:
    if y>z:
        print("Max is",y)
