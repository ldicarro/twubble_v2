# Twubble version 2

A collection of Python scripts that run on a Raspberry Pi. The Pi is has a screen plugged into the HDMI and a bubble machine connected to its GPIO. The scripts use PyGame to generate the window for the screen. GPIO pin 18 connects to a transistor which connects to a hacked bubble machine to turn it on and off.

When the app is run, after set-up, it goes out to the internet and gets a searched tweet (#thoughttwubble) from a PHP script. If the new tweet does not match the old tweet, it will trigger the process to blow bubbles and display the tweet on the screen. In this version, LEDs were added to flash when the bubbles are activated.

During the loop, translucent circles are drawn on the screen and moved up to look like bubbles. The last tweet is also drawn to the screen. If there is not a last tweet, one will be pulled from the default_tweets array.

The PHP files need to be put on a web server. I have put them on my own web server to avoid firewall issues, but this may be moot now.
