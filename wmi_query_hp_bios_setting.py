import wmi

c = wmi.WMI(namespace='wmi')

for bios in c.HP_BIOSSetting():
    print(bios.Name, bios.Value)