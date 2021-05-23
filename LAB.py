number=input("enter the number you want to check ") 
sum=0 
for i in str(number): 
    j=int(i) 
    i=j**3 
    sum+=i 
if sum==int(number): 
    print("True") 
else : 
    print("false")
