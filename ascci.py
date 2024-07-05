import serial

# Open a serial port
ser = serial.Serial('/dev/ttyUSB0')  # This will vary depending on what port your device is connected to

# Write some ASCII code to the interface
ser.write(b'Hello World\n')  # The string literal is being converted to bytes using the b'' syntax

ser.close()
