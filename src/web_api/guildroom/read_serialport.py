import serial, configparser

class SerialReader:

    def __init__(self):

        config = configparser.ConfigParser()
        config.read("settings.ini")
        self.port = config.get("secret", "port")

        self.ser = serial.Serial(self.port, 9600)
        self.ser.flushInput()

    def readSerial(self):

        serialValue = ord(self.ser.read(1))
        return serialValue

    def sendSerial(self, data):

        self.ser.write(data)
