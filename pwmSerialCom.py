import serial
with serial.Serial('/dev/ttyACM1', 9600, timeout = 1) as ser:
	msg = bytearray([0xFF, 0x00, 0x00, 0x50, 0x50, 0x00, 0xA0])
	print([str(x) for x in msg]);
	ser.write(msg)
	print([str(x) for x in ser.read(7)]);
	