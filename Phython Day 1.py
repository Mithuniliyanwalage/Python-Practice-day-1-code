m1=int(input("Enter a mark for student 1;"))
m2=int(input("Enter a mark for student 2;"))
m3=int(input("Enter a mark for student 3;"))
m4=int(input("Enter a mark for student 4;"))
m5=int(input("Enter a mark for student 5;"))
average=(m1+m2+m3+m4+m5)/5
print("Average marks=",average)

r=float(input("Enter a value for radius:"))
Perimeter=(2*3.142857143*r)
Area=(3.142857143*r*r)
print("Perimeter equals:",Perimeter)
print("Area equals:",Area)

p=float(input("Enter a principle amount:"))
r=float(input("Enter an interest rate:"))
y=int(input("Enter no. of years:"))
Compound_Interest=p*((100+r)/100)**p
print("Compound Interest is equals to:",Compound_Interest)

b=float(input("Enter basic salary:"))
d=int(input("Enter no. of working days:"))
h=int(input("Enter extra hours:"))
total=(d*(b*0.05))+h*250
tax=total*0.12
Salary=total-tax
print("Salary is:",Salary)
