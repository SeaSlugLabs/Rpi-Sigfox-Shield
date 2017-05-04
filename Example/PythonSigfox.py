
from gpiozero import LED
from time import sleep
import serial

red=LED(18)#GPIO pin for USer LED


#Initialize Serial Port
ser=serial.Serial("/dev/ttyS0")
ser.baudrate=9600
##----------

def SigfoxInfo():

        if ser.isOpen:                   #Check if port is open
                print("port is open")
                ser.write("AT\r\n")      #Write AT Command
                data=ser.read(2)         #Response Should be OK
                print(data)

                print("Get ID")
                ser.write("AT$I=10\r\n") #Send Command to Get ID
                data=ser.read(10)
                print(data)

                print("Get PAC")
                ser.write("AT$I=11\r\n") #Send Command to Get ID
                data=ser.read(18)
                print(data)

def SigfoxSend():
                #Initiate a Transmission
                print("Init Transmission")
                sleep(1)
                ser.write("AT$SF=AABBCCDD\r\n")
                sleep(6)
                data=ser.read(4)        #We should get a OK response
                print(data)



red.on()
sleep(1)
red.off()
sleep(1)
SigfoxInfo()

SigfoxSend()
ser.close()
