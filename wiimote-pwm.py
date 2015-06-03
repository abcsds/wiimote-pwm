import cwiid
import time
from os import system


print 'Press 1 + 2 on your Wii Remote now ...'
time.sleep(1)

# Connect to the Wii Remote. If it times out
# then quit.
try:
    wii=cwiid.Wiimote()
except RuntimeError:
    print "Error opening wiimote connection"
    quit()

try:
    blaster = open('/dev/pi-blaster', 'w')
except RuntimeError:
    print "Error opening pi-blaster"
    quit()

print 'Wii Remote connected...\n'
print 'Press some buttons!\n'
print 'Press PLUS and MINUS together to disconnect and quit.\n'

wii.rpt_mode = wii.rpt_mode = cwiid.RPT_ACC

while True:

    x,y,z = wii.state['acc']

    x = float(x)/float(255)
    y = float(y)/float(255)
    z = float(z)/float(255)
    print x, y, z
    system('echo "18='+str(x)+'" > /dev/pi-blaster')
    system('echo "23='+str(y)+'" > /dev/pi-blaster')
    system('echo "24='+str(z)+'" > /dev/pi-blaster')
