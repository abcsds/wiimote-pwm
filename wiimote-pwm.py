import cwiid
import time


button_delay = 0.1

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
    blaster.write('16='+str(x))
    blaster.write('18='+str(y))
    blaster.write('22='+str(z))
    # time.sleep(0.1)
    # 23  P1-16
    # 24  P1-18
    # 25  P1-22


    # {'acc': (126, 127, 152), 'led': 15, 'rpt_mode': 6, 'ext_type': 0, 'buttons': 0, 'rumble': 0, 'error': 0, 'battery': 147}
