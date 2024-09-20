try:
   a= int(input("Enter your number: "))
   for  i in range (1, 3): 
      print (i/a)
except ZeroDivisionError:
    print(" You cannot divide by 0")
        