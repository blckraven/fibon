
def fibonacci(n): 
    if n<0 or type(n) != int: 
        print("Incorrect input") 
    elif n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        return fibonacci(n-1)+fibonacci(n-2)

print("Welcome in Fibon!\nThat program will show you\nthe number you want from the Fibonacci sequence.\n")
n=int(input("My choose is number: "))
n+=1
print("The",n-1,"number of Fibbonacci sequence is:",fibonacci(n))