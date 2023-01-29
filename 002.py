#loops

#for
s=0 #initialize the variable before execution
for i in range(3):
    x=int(input("enter the number"+str(i+1)+'::'))
    print(x)
    s=s+x
print("Addition is:",s)

#while
ans='y' #initializing variable before execution
while ans=='y':
    w=input("enter a string:")
    print(w)
    ans=input("Continue? y/n")
print("Out of the matrix")

#for for multiplication table
num=int(input("Enter a number:"))
for i in range(1,13):
    print(f"{num} * {i} = {num*i}")

#for for loop
for j in range(3):
    num=int(input("Enter a number:"))
    for i in range(1,13):
        print(f"{num} * {i} = {num*i}")

#here for a while loop

ans="y"
while ans=="y":
    num=int(input("Enter a number:"))
    for i in range(1,13):
        print(f"{num} * {i} = {num*i}")
    ans=input("Have a little pit stop? y/n")

#digits and sums

num=int(input("Enter a multi-digit Number: "))

count=0
digit=0
summ=0
n=num

while n!=0:
    digit=n%10
    count=count+1
    summ=summ+digit
    n=n//10

print(f"The total number of Digits in {num} is {count}")
print(f"The sum of digits in {num} is {summ}")
