def update():
	global copy, oldcopy, pinpushed

	try:
		filehandler = urllib2.urlopen('http://www.mackaos.com/twitter_test/index.php')
		copy = filehandler.read()
	except:
		copy = defaultTweets[randint(0,len(defaultTweets) - 1)]

	if copy == oldcopy and pinpushed == True:
		copy = defaultTweets[randint(0,len(defaultTweets) - 1)]

	if copy != oldcopy:
		# do gpio stuff here
		GPIO.output(BUBBLES,True)
		for i in range(10):
			randomLED()
		
		GPIO.output(BUBBLES,False)
		for i in range(10):
			randomLED()

		GPIO.output(BUBBLES,True)
		for i in range(10):
			randomLED()

		GPIO.output(BUBBLES,False)
		oldcopy = copy

	pinpushed = False
	shutoffLED()

def randomLED():
	for i in range(len(LEDPINS)):
		GPIO.output(LEDPINS[i],False)
	
	GPIO.output(LEDPINS[randint(0,len(LEDPINS) - 1)], True)
	time.sleep(.5)

def shutoffLED():
	for i in range(len(LEDPINS)):
		GPIO.output(LEDPINS[i],False)

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