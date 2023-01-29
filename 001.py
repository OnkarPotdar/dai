print("Hello World")

#this is a comment
name=input("Enter your name")

#this is a second comment
print(name)

#this is the third comment, I'm tired
x=int(input("Enter number:"))
if x>6 and x<80:
    print ("Valid",x)
else :
    print ("Invalid",x)

#changing print
for j in range(5):
    for i in range(5):
        print(i,end="\t",sep="**")
    print()

#formatted strings
y=int(input('Enter another number:'))
print(x+y)
z=x+y
print(f"addition:{z}")
print("Addition:",z)
w=int(input('Enter the third number:'))

#ternary operator
v=x if x>y else y
print(f"Maximum value by ternary: {v}")

#nested loops for maximum of w,x,y
if w>x and w>y:
    print(f'The maximum value is {w}')
else:
    if x>y:
        print(f'The maximum value is {x}')
    else:
        print(f'The maximum value is {y}')
