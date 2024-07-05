import wmi

c = wmi.WMI()

for class_name in c.classes:
    print(class_name)
