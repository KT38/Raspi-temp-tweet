import RPi.GPIO as GPIO
import dht11
import time
import datetime
import tweepy
# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key,access_secret)
api = tweepy.API(auth)                                      

# read data using pin 26
instance = dht11.DHT11(pin=26)

result = instance.read()
if result.is_valid():
    now = "Last valid input: " + str(datetime.datetime.now())
    temp = "Temperature: %d C" % result.temperature
    hum = "Humidity: %d %%" % result.humidity
    api.update_status(now + "\n" + temp + "\n" + hum)
    print(str(datetime.datetime.now()))
