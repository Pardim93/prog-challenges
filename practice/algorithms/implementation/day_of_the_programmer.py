

def dayOfProgrammer(year):
    if(year == 1918):
        print("26.09.1918")
    elif(year < 1918):
        if(year % 4 == 0):
            print("12.09.", year, sep="")
        else:
            print("13.09.", year, sep="")
    else:
        if((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)):
            print("12.09.", year, sep="")
        else:
            print("13.09.", year, sep="")


dayOfProgrammer(1711)
