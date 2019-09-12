convfactor=0.09290304
a=input("Would you like to give the length and the width in feet or in meter?\n Press 'f' for feet or 'm' for meters!")
if a=="f":
    while True:
        try:
            length=float(input("What is the length of the room in feet? : ")) 
            width=float(input("What is the width of the room in feet? : "))
            break
        except ValueError:
            print("Type in a floating point or an integer type number!")

    formulameter=(length*width)*convfactor
    formulafeet=length*width
    print("You entered dimensions of {0} feet by {1} feet.".format(length, width))
    print("The area is \n {0:.4f} square feet \n {1:.4f} square meters.".format(formulafeet,formulameter))
elif a=="m":
    while True:
        try:
            length=float(input("What is the length of the room in meter? : ")) 
            width=float(input("What is the width of the room in meter? : "))
            break
        except ValueError:
            print("Type in a floating point or an integer type number!")
    formulafeet=((length*3.280839895)*(width*3.280839895))
    formulameter=length*width
    print("You entered dimensions of {0} meter by {1} meter.".format(length, width))
    print("The area is \n {0:.4f} square feet \n {1:.4f} square meters.".format(formulafeet,formulameter))