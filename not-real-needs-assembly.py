import win32com.client

strComputer = "."
objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
objSWbemServices = objWMIService.ConnectServer(strComputer, "root\cimv2")
colItems = objSWbemServices.ExecQuery("SELECT * FROM Win32_BIOS")

for objItem in colItems:
    print(f"BIOS Version: {objItem.BIOSVersion}")
