import os
import sys

direction = '/sys/class/gpio/gpio67/direction'
onoff = '/sys/class/gpio/gpio67/value'

def status(file):
	dirf = open(direction, 'r')
	dirv = dirf.read()
	print 'Direction: {0}'.format(dirv)
	onoffr = open(onoff, 'r')
	onoffv = onoffr.read()
	print 'OnOff: {0}'.format(onoffv)


if __name__ == '__main__':
	if sys.argv
	status(file)
