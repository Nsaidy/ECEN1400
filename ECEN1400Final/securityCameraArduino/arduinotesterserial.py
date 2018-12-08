import serial, time, csv, decimal

#for Mac
port = '/dev/ttyUSB1'

ser = serial.Serial(port , baudrate=9600, bytesize=8, parity=serial.PARITY_NONE, stopbits=1, timeout=2)
a = 0
while True:
    a = a + 1
    time.sleep(2)

    if(a % 2 == 1):
        ser.write(b'True')
    else:
        ser.write(b'False')
'''
    data = data.split(',')

    if len(data) > 0:

        if data[0] != '2501':

            s = float( 1000 / float(data[0]) )

            print  'wind speed %.1f' %(round(float((2.5 * s)), 1))
            print 'wind direction', round((int(data[1]) - (50))  * .39, 0)
            print 'software version', data[2], '\n'             
        else:   
            print 'wind speed is zero'
            print 'wind direction', round((int(data[1]) - (50))  * .39, 0)
            print 'software version', data[2]
'''
ser.close()