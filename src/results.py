import sys
import serial
import time
import csv

record = []
header = ['aX', 'aY', 'aZ', 'gX', 'gY', 'gZ']
samples = 3000
counter = 0
filename = sys.argv[1]

ser = serial.Serial(port = '/dev/ttyACM0', baudrate=9600, timeout=1) 
print("Connected")
print(header)

f = open(filename, 'w', encoding='UTF8')
writer = csv.writer(f)
#writer.writerow(header)

while(counter < samples):
    
    data = ser.readline().decode('utf-8').replace('\r', "").replace('\n', "")
    data = data.split(',')
     
       
    writer.writerow(data)
    print(data)
        
    counter+=1

