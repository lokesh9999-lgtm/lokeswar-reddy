try:
    num=int(input("enter a number :"))
    result=10/num
    print("Result:",result)
except ValueError:
    print("Error:invaild input! please vaild number")
except ZeroDivisionError:
    print("Error:division by zero!")
