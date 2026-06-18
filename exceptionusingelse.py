try:
    num=int(input("enter a number:"))
    result=10/num
except ValueError:
    print("Error:invalid input! please valid numbr")
except ZeroDivisionError:
    print("Error:division by zero!")
else:
    print("Result:",result)
