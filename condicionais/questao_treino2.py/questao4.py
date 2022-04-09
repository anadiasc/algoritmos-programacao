num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 > num2 and num1 > num3:
    print(f'o numero {num1} é o maior')
elif num2 > num1 and num2 > num3:
     print(f'o numero {num2} é o maior')
else:
     print(f'o numero {num3} é o maior')