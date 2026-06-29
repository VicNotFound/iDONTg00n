weight= float(input("What is your weight: "))
type= input("Kg(K) or Lb(L) : ")
 
if type== "l" or type=="L":
   weight= weight*10
   print("Weight in Kg: "+str(weight))
elif type== "k" or "K":
   weight= weight/10
   print("Weight in Lb: "+str(weight))