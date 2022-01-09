def getdate():
    import datetime
    return datetime.datetime.now()
def kp_d():
    """To enter diet data""" 
    print("What you eat today")
    value = str(input())
    with open("kp_d.txt","a") as f:
        f.write(str([str(getdate())])+":"+value+"\n")
    print("successfull")
def jay_d():
    """To enter diet data"""
    print("What you eat today")
    value = str(input())
    with open("jay_d.txt","a") as f:
        f.write(str([str(getdate())])+":"+value+"\n")
    print("successfull")
def digu_d():
    """To enter diet data"""
    print("What you eat today")
    value = str(input())
    with open("digu_d.txt","a") as f:
        f.write(str([str(getdate())])+":"+value+"\n")
    print("successfull")
def kp_e():
    """To enter exersise data"""
    print("What exercise you do today")
    value = str(input())
    with open("kp_e.txt","a") as f:
        f.write(str([str(getdate())])+":"+value+"\n")
    print("successfull")
def jay_e():
    """To enter exersise data"""
    print("What exercise you do today")
    value = str(input())
    with open("jay_e.txt","a") as f:
        f.write(str([str(getdate())])+":"+value+"\n")
    print("successfull")
def digu_e():
    """To enter exersise data"""
    print("What exercise you do today")
    value = str(input())
    with open("digu_e.txt","a") as f:
        f.write(str([str(getdate())])+":"+value+"\n")
    print("successfull")
def kp_dr():
    """To read diet data"""
    with open("kp_d.txt") as f:
        print(f.read())
def jay_dr():
    """To read diet data"""
    with open("jay_d.txt") as f:
        print(f.read())
def digu_dr():
    """To read diet data"""
    with open("digu_d.txt") as f:
        print(f.read())
def kp_er():
    """To read exersise data"""
    with open("kp_e.txt") as f:
        print(f.read())
def jay_er():
    """To read exersise data"""
    with open("jay_e.txt") as f:
            print(f.read())
def digu_er():
    """To read exersise data"""
    with open("digu_e.txt") as f:
        print(f.read())


def kp():
    """Main Function"""
    """what type of data you want to enter"""
    print("Type:1.read 2.write")
    a = int(input())
    if a==1:
        print("What type of data you want to read:1.diet 2.exercice")
        b = int(input())
        if b==1:
            kp_dr()
        elif b==2:
            kp_er()
        else:
            print("invalid input")
         
    elif a==2:
        print("What type of data you want to enter:1.diet 2.exercice")
        b = int(input())
        if b==1:
            kp_d()
        elif b==2:
            kp_e()
        else:
            print("invalid input")
    
    else:
        print("invalid input")
        
def jay():
    """what type of data you want to enter"""
    print("Type:1.read 2.write")
    a = int(input())
    if a==1:
        print("What type of data you want to read:1.diet 2.exercice")
        b = int(input())
        if b==1:
            jay_dr()
        elif b==2:
            jay_er()
        else:
            print("invalid input")
         
    elif a==2:
        print("What type of data you want to enter:1.diet 2.exercice")
        b = int(input())
        if b==1:
            jay_d()
        elif b==2:
            jay_e()
        else:
            print("invalid input")

    else:
        print("invalid input")

def digu():
    """what type of data you want to enter"""
    print("Type:1.read 2.write")
    a = int(input())
    if a==1:
        print("What type of data you want to read:1.diet 2.exercice")
        b = int(input())
        if b==1:
            digu_dr()
        elif b==2:
            digu_er()
        else:
            print("invalid input")
         
    elif a==2:
        print("What type of data you want to enter:1.diet 2.exercice")
        b = int(input())
        if b==1:
            digu_d()
        elif b==2:
            digu_e()
        else:
            print("invalid input")

    else:
        print("invalid input")
        
print("Whom data you want to add:1.kp 2.jay 3.digu")
a = int(input())
if a==1:
    kp()
elif a==2:
    jay()
elif a==3:
    digu()
else:
    print("invalid input")