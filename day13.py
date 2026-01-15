'''def my_function():
    for i in range(1,21):
        if i==20:
            print("you got it buddy")

my_function()

try:
    num1=int(input("enter the number:"))
    num2=int(input("enter the number:"))
    print(num1/num2)
except ZeroDivisionError:
    print("you can't divide by zero")
except ValueError:
    print("you can't divide by zero  make changes in value")
else:
    print("division succeed")
finally:
    print("divisio operation completed")

def odd_or_even(number):
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."
odd_or_even(20)'''