#Exercise 1


def exercise1():
    height=float(input("Height in meters: "))
    weight=float(input("Weight in kilograms: "))

    #Calculate BMI
    #BMI=weight/height^2

    bmi=weight/(exponential(height,2))
    print("Your BMI is: ",bmi)
    print("DIAGNOSIS:")
    if(bmi>40):
        print("third degree obesity (extreme)")
    elif(bmi>35):
        print("second degree obesity (clinical)")
    elif(bmi>30):
        print("first degree obesity")
    elif(bmi>25):
        print("overweight")
    elif(bmi>18.5):
        print("correct weight")
    elif(bmi>17):
        print("underweigt")
    elif(bmi>16):
        print("emacination")
    else:
        print("starvation")

    #calculate the correct interval for your height
    x=0 #starting kg
    tmp=x
    while(tmp<18.5):
        x=x+1
        tmp=x / (exponential(height, 2))

    y=200#starting kg
    tmp=y
    while (tmp>25):
        y = y - 1
        tmp = y / (exponential(height, 2))
    print("You should weight between: ",x,"kg and ",y,"kg")


def exponential(x,y):
    tmp=x
    for i in range(y-1):
        tmp=tmp*x

    return tmp

exercise1()

#print(exponential(4,9))