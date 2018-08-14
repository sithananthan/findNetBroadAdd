print("This program will find if IP address is valid or not")

ipAddress = input("Enter the IP address : ")

try:
    values = [int(x) for x in ipAddress.split('.')]
    validIp = 0
    if(len(values)==4):
        for x in values:
            if (x >= 0 and x < 256 ):
                validIp+= 1
    if (validIp == 4):
        print("The IP address is valid")
    else:
        print ("Not an valid IP")

except:
    print ("Not an Valid IP")

close = input("Close the window yes/no : " )
if (close == "yes"):
    exit(0)
    

