def subonefromip(ipnextSubnetnw, octetToModify):
    ipnew =[None] * 4
    if(int(ipnextSubnetnw[3]) == 0):
        ipnew[3] = str(255)
        ipnew[2] = str(int(ipnextSubnetnw[2]) - 1)
        ipnew[1] = ipnextSubnetnw[1]
        ipnew[0] = ipnextSubnetnw[0]
    else:
        ipnew[3] = str(int(ipnextSubnetnw[3]) - 1)
        ipnew[2] = ipnextSubnetnw[2]
        ipnew[1] = ipnextSubnetnw[1]
        ipnew[0] = ipnextSubnetnw[0]

    if(int(ipnew[2]) < 0):
        ipnew[2] = str(255)
        ipnew[1] = str(int(ipnextSubnetnw[1]) - 1)
        ipnew[0] = ipnextSubnetnw[0]

    if(int(ipnew[1]) < 0):
        ipnew[1] = str(255)
        ipnew[0] = str(int(ipnextSubnetnw[0]) - 1)

    return ipnew

def findNetworkAddress(ipAddressaslist, octetToModify, subnetValue):
    ipnew = [None] * 4

    for i in range(len(ipAddressaslist)):
        if i < (octetToModify - 1):
            ipnew[i] = str(ipAddressaslist[i])
        elif i == octetToModify - 1:
            ipnew[i] = str((ipAddressaslist[i]//int(subnetValue)) * int(subnetValue))
        else:
            ipnew[i] = str(0)

    ipnextSubnetnw = [None] * 4
    incre = 0
    for i in range(len(ipAddressaslist)):
        if i < (octetToModify - 1):
            ipnextSubnetnw[i] = str(ipAddressaslist[i])
        elif i == octetToModify - 1:
            ipnextSubnetnw[i] = str((ipAddressaslist[i]//int(subnetValue)) * int(subnetValue) + int(subnetValue))
            if int(ipnextSubnetnw[i]) > 255:
                ipnextSubnetnw[i] = str(0)
                ipnextSubnetnw[i-1] = str(int(ipnextSubnetnw[i-1]) + 1)
        else:
            ipnextSubnetnw[i] = str(0)

    ipnextSubnetnw = subonefromip(ipnextSubnetnw, octetToModify)

    network_add = ipnew[0] + "." +ipnew[1] + "." + ipnew[2] + "." + ipnew[3]
    broad_add = ipnextSubnetnw[0] + "." + ipnextSubnetnw[1] + "." + ipnextSubnetnw[2] + "." + ipnextSubnetnw[3]

    return network_add, broad_add

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
            exit(0)

    except:
        print ("Not an Valid IP")
        exit(0)

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
    close = input("Press enter to continue : " )
    if close == "no":
        exit(0)
    else:
        pass