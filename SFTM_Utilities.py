def  get_deviceID():
    with open('settings.conf', 'r') as settings:
        for line in settings:
            key, value = line.strip().split(None, 1)
            if key == "deviceID:":
                deviceID = value.strip()
                print('The deviceID is: ' + deviceID)
    return deviceID

print(get_deviceID())