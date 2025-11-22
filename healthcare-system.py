
while True:
    
    height=float(input("Enter height in meters"))

    weight=float(input("enter weight in kilograms"))

    BMI =(weight/(height*height))
    print(f"your body mass index bmi is {BMI}")
    if (BMI<=18.5):
        print("you are underweight eat nutritious food")
    elif(BMI <=24.9):
        print("you are healthy ")
    elif(BMI<=29.9):
        print("you are overweight do exercise regularly and eat an healthy food")
    else:
        print("you are obese meet the doctor")
    userwantstocontinue =input("do you want to continue? yes or no ")
    if(userwantstocontinue == 'no'):
        print("over")
        break
                     
