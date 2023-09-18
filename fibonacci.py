nterms= int(input("Enter any positive number: "))


number1, number2 = 0 ,1
count = 0 

if(nterms == 1):
    print(nterms)
else:
    while(count<nterms):
        print(number1)
        nth = number1+ number2
        number1 = number2
        number2 = nth
        count += 1

def finbonacci(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return 