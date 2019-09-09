import serial

class SerialReader:

    def __init__(self, port):

        self.ser = serial.Serial(port, 9600)
        self.ser.flushInput()

    def readSerial(self):

        serialValue = ord(self.ser.read(1))
        return serialValue

    def sendSerial(self, data):

        self.ser.write(data)
