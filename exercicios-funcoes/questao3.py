def divisor(num1, num2):
    if num1 % num2 == 0:
        print(0)
    else:
        while True:
            if num1 % num2 != 0:
                num2 += 1
            else:
                print(num2)
                break
