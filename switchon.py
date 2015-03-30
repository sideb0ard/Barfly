import os
import sys

devicenum = 67
device = '/sys/class/gpio/export'
direction = '/sys/class/gpio/gpio67/direction'
onoff = '/sys/class/gpio/gpio67/value'


def init():
	initf = open(device, 'w')
	initf.write(devicenum + '\n')


def status():
	dirf = open(direction, 'r')
	dirv = dirf.read()
	print 'Direction: {0}'.format(dirv)
	onofff = open(onoff, 'r')
        onoffv = onofff.read()
	print 'Val: {0}'.format(onoffv)

def setval(val):
        f = open(onoff, 'w')
        f.write(val)

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "status or on / off, buddy..."
		sys.exit(1)

	if sys.argv[1] == 'status':
		status()
        elif sys.argv[1] == 'set':
                setval(sys.argv[2])
