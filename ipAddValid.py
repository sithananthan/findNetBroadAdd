def findNetworkAddress(ipAddressaslist, octetToModify, subnetValue):
    ipnew = [None] * 4
    for i in range(len(ipAddressaslist)):
        if i < (octetToModify - 1):
            ipnew[i] = str(ipAddressaslist[i])
        elif i == octetToModify - 1:
            ipnew[i] = str((ipAddressaslist[i]//int(subnetValue)) * int(subnetValue))
        else:
            ipnew[i] = str(0)

    network_add = ipnew[0] + "." +ipnew[1] + "." + ipnew[2] + "." + ipnew[3]

    return network_add, "borad"


print("This program will find if IP address is valid or not")

while True:
    try:
        ipAddress = input("Enter the IP address : ")
        ipAddressaslist = [int(x) for x in ipAddress.split('.')]
        validIp = 0
        if len(ipAddressaslist)==4:
            for x in ipAddressaslist:
                if (x >= 0 and x < 256 ):
                    validIp+= 1
        if validIp == 4:
            print("The IP address is valid")
        else:
            print ("Not an valid IP")

    except:
        print ("Not an Valid IP")

    subnetMask = int(input("Enter the subnet Mask as number ex. /12, /24, /18 (without slash): "))

    ipAddressWithMask = ipAddress +"/" + str(subnetMask)
    octetIndex = subnetMask//8
    octetIndexValue = subnetMask%8

    if octetIndexValue != 0:
        octetToModify = octetIndex + 1
    else:
        octetToModify = octetIndex

    bitValue = {'1':'128', '2':'64', '3':'32', '4':'16', '5':'8', '6':'4', '7':'2', '0':'1'}

    subnetValue = bitValue.get(str(octetIndexValue))

    networkAddress, broadcastAddress = findNetworkAddress(ipAddressaslist,octetToModify,subnetValue)


    print ("Number of subnets " + str(2**octetIndexValue))
    print ("Number of hosts per network " + str(2**(8 - octetIndexValue) - 2))
    print("Network address of " + str(ipAddressWithMask) + " is : " + networkAddress )
    print("Broadcast address of " + str(ipAddressWithMask) + " is : " + broadcastAddress )
    close = input("Do you want to continue yes/no : " )
    if close == "yes":
        exit(0)
    else:
        pass

    

