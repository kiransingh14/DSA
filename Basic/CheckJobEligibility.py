def checkEligibilityOfJob(age):
    #if else statement
    # if (age < 18):
    #     print("not eligible for job")
    # elif(age <= 54):
    #     print("eligible for job")
    # elif(age <=57):
    #     print("eligible for job, but retirement soon")
    # else:
    #     print("retirement time")
    
    # nested if statement 
    if (age < 18):
        print("not eligible for job")
    elif(age <=57):
        
        print("eligible for job")
        if(age >=55):
            print("but retirement soon")
    else:
        print("retirement time")
age = int(input("Enter your age:"))
checkEligibilityOfJob(age)
