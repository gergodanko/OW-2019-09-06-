while True:   
    try:
        ppl=int(input("How many people are there?"))
        pizza=int(input("How many pizzas do you have?"))
        slices=int(input("How many slices of pizza do you have?"))
        break
    except ValueError:
        print("Try again !")
divide=(pizza*slices)//ppl
leftover=(pizza*slices)%ppl
if divide==1 or divide==0:
    print("Each person gets {0} slice of pizza. \n".format(divide))
else:
    print("Each person gets {0} slices of pizza. \n".format(divide))

if leftover==1 or leftover==0:
    print("There are {0} leftover slices".format(leftover))
else:
    print("There are {0} leftover slices".format(leftover))

