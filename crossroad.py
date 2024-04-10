number = int(input ("Enter a number: ")) #gotta convert to a int

if number > 0:
    print("The number is positive.")
elif number == 0:                         #the problem was that there was only one equeals sign which is an assignment instead of a  checking
    print("The number is zero.")
else:                                      #else is going to automatically end so it wont take the variable, so you can either just do what i did, or switchh to an elif.
    print("The number is negative.")



   