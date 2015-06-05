#!usr/bin/python

import pygame,sys,urllib2,thread,time,socket
import TextRectException
#import RPi.GPIO as GPIO
from random import randint
from functions import *

pygame.init()

screenx		= pygame.display.Info().current_w
screeny		= pygame.display.Info().current_h
#screen		= pygame.display.set_mode((screenx,screeny),pygame.FULLSCREEN)
#bg		= pygame.image.load("img/background.jpg").convert()
#bg		= pygame.transform.scale(bg,(screenx,screeny))
black		= (0,0,0)
white		= (255,255,255)
TRANSPARENT	= (255,0,255)
count		= 20
copy		= ''
oldcopy		= ''
font		= pygame.font.SysFont("freesans", 32, bold = 1)
bubble_list	= []
done		= False # Loop until user clicks close button
clock		= pygame.time.Clock() # Used for screen updates timing
BUBBLES		= 18
MANUALPIN	= 23
pinpushed	= False
LEDPINS 	= (24,25,8,7,11)
INPROGRESS	= False
maxcount	= 0

defaultTweets = (
"Thinking of you!",
"Have a wonderful day!",
"Babymetal is the best!!",
"Looking forward to seeing you soon!",
"You brighten my day!",
"Blow some bubbles.",
"Look at the bubbles floating in the air!"
)

print ">>> SETUP <<<"

def is_connected():
	try:
		# see if we can resolve the host name -- tells us if there is
		# a DNS listening
		host = socket.gethostbyname(REMOTE_SERVER)
		# connect to the host -- tells us if the host is actually
		# reachable
		s = socket.create_connection((host, 80), 2)
		return True
	except:
		pass
		return False

def update():
	global copy, oldcopy, pinpushed,INPROGRESS

	try:
		filehandler = urllib2.urlopen('http://www.mackaos.com/twitter_test/index.php')
		copy = filehandler.read()
		print 'found tweet on network'
	except:
		copy = defaultTweets[randint(0,len(defaultTweets) - 1)]
		print 'pulling tweet from default'

	if copy == oldcopy and pinpushed == True:
		copy = defaultTweets[randint(0,len(defaultTweets) - 1)]
		print 'copy matches and button was pushed'
	else:
		print 'tweets match'

	if copy != oldcopy:
		INPROGRESS = True
		# do gpio stuff here
		#GPIO.output(BUBBLES,True)
		print '>turning on bubbles'
		for i in range(10):
			randomLED()
		
		#GPIO.output(BUBBLES,False)
		print '>turning off bubbles'
		for i in range(10):
			randomLED()

		#GPIO.output(BUBBLES,True)
		print '>turning on bubbles'
		for i in range(10):
			randomLED()

		#GPIO.output(BUBBLES,False)
		print '>turning off bubbles'
		oldcopy = copy
		INPROGRESS = False

	pinpushed = False
	shutoffLED()

def randomLED():
	print "randomLED"
	#for i in range(len(LEDPINS)):
		#GPIO.output(LEDPINS[i],False)
		#print '>setting LEDPIN %s to off' %LEDPINS[i]
	
	#GPIO.output(LEDPINS[randint(0,len(LEDPINS) - 1)], True)
	#print '>setting LEDPIN %s to ON' %LEDPINS[randint(0,len(LEDPINS) - 1)]
	time.sleep(.5)

def shutoffLED():
	print 'shutoffLED'
	#for i in range(len(LEDPINS)):
		#GPIO.output(LEDPINS[i],False)
		#print '>setting LEDPIN %s to off' %LEDPINS[i]

def createBubbles(i):
	x = randint(0, screenx)
	y = screeny
	z = randint(10, 100)
	a = randint(10, 70)
	s = randint(1, 5)

	copy = i
	
	if i < len(bubble_list):
		bubble_list[i] = [x, y, z, a, s]
	else:
		bubble_list.append([x, y, z, a, s])

# first - check if we have an internet connection
if is_connected:
	print '>>> connection======>>>'
	maxcount = 30
else:
	maxcount = 100


#GPIO.setmode(GPIO.BCM)
#GPIO.setup(BUBBLES,GPIO.OUT)
#GPIO.setup(MANUALPIN,GPIO.IN)
#GPIO.setmode(GPIO.BCM)

for i in range(len(LEDPINS)):
	#GPIO.setup(LEDPINS[i],GPIO.OUT)
	print '>setting LEDPIN %s to off' %LEDPINS[i]

for i in range(10):
	createBubbles(i)


#------------------ Main Loop -----------------------------
while done == False:
	print '>>> LOOP <<< %s'%count
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			#GPIO.cleanup()
			done = True
		elif event.type == pygame.KEYDOWN:
			#print event.key
			if event.key == 113 or event.key == 27:
				#GPIO.cleanup()
				done = True
			if event.key == 114:
				update()
	
	if INPROGRESS == False:
		if count == maxcount: # or GPIO.input(MANUALPIN) == True:
			#if GPIO.input(MANUALPIN) == True:
			#	pinpushed = True
			print 'count = %s' %count
			thread.start_new_thread(update,())
			count = 0
		else:
			count += 1
	
	# drawing
	#screen.fill(black)
	#screen.blit(bg,[0,0])
	
	#for i in range(len(bubble_list)):
	#	tempsurf = pygame.Surface((200,200))
	#	tempsurf.fill(TRANSPARENT)
	#	tempsurf.set_colorkey(TRANSPARENT)
	#	pygame.draw.circle(tempsurf, white, [bubble_list[i][2],bubble_list[i][2]], bubble_list[i][2])
	#	tempsurf.set_alpha(bubble_list[i][3])
	#	screen.blit(tempsurf,[bubble_list[i][0],bubble_list[i][1]])
	#	bubble_list[i][1] = bubble_list[i][1] - bubble_list[i][4]

	#	if(bubble_list[i][1] < -200):
	#		createBubbles(i)

	#my_rect = pygame.Rect((40, screeny / 2, screen.get_width() - 40, (screeny / 2) - 40))
	#rendered_text = TextRectException.render_textrect(copy, font, my_rect, (216, 216, 216), (0, 0, 0), 1)
	#rendered_text.set_colorkey((0,0,0))

	#screen.blit(rendered_text, my_rect.topleft)

	#pygame.display.flip()

	# 20 frames
	#clock.tick(120)
	time.sleep(.5)
# end event loop

pygame.quit()