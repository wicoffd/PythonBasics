print('inputs and if elif statements')


x = int(input("Enter and int: "))

if x < 0:
        print('This int is negative')
        print(x)

elif x==0:
        print(x)

elif x > 0:
        print('This int is positive')
        print(x)

else:
        print('Error or not an int')

print()



def switch(x):
    match x:
        case 4:
            print ('4')
            return "4"
        case -1:
            print('-1')
            return "-1"
        case _:
            print('Input not found in switch statement')
            print(x)
            return x

switch(x)

def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

input = int(input("Int used to find the nearest fibonacci number to input "))
fibonacci(input)
