def cal(num1,num2,opr):
 if opr=="+":
  return num1+num2
 elif opr=="-":
  return num1-num2
 elif opr=="/":
  return num1/num2
 elif opr=="*":
  return num1*num2
 else:
   print("ERROR:Invalid Input")

def main():
 num1= float(input("Enter Your First Number: "))
 opr= input("Enter Operator to be used: ")
 num2= float(input("Enter Your Second Number: "))
 result=cal(num1,num2,opr)

 print(result)
 
main()