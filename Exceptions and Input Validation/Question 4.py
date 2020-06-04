def GetIpAddress():
    isValid = False
    while not isValid:
        ip = input("Enter IP Address: ")
        parts = ip.split('.')
        isValid = len(parts) == 4
        if isValid:
            for n in parts:
                if not n.isnumeric() or int(n) < 0 or int(n) > 255:
                    isValid = False
                    break
    return ip

print(GetIpAddress())
