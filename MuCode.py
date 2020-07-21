from pyatcrobo2.parts import DCMotor
import time
import ufirebase as firebase
from pystubit_iot import *
import machine
from pystubit.board import *
from pystubit_iot import *
from pyatcrobo2.parts import *
import time
#from sb_config import *
import network
#import sb_config

#enter your wifi SSID and the password respectively within ""  on line 15
res = wifi_connect("", "", trytime=10)


if not res:
    display.scroll('Err')
    exit()

#print(WIFI_SSID + " Connected")

display.show("OK", color=(10,0,0))
display.clear()

m1 = DCMotor('M1')
m2 = DCMotor('M2')
turnedLeft=False
turnedRight=False
result={'PIC': {'character': '"S"'}}

while True:
    # response = firebase.get('https://ai-camera-5f64e.firebaseio.com/')
    result=firebase.get("ai-camera-5f64e")
    print(result)

    if result=={'PIC': {'character': '"S"'}}:
        # stop
        m1.power(0)
        m2.power(0)
        m1.ccw()
        m2.ccw()
        #time.sleep(2)

    elif result=={'PIC': {'character': '"F"'}}:
        # forward
        m1.power(100)
        m2.power(100)
        m1.ccw()
        m2.ccw()
        #time.sleep(2)

    elif result=={'PIC': {'character': '"B"'}}:
        # backward
        m1.power(50)
        m2.power(55)
        m1.cw()
        m2.cw()
        #time.sleep(2)

    elif result=={'PIC': {'character': '"L"'}}:
        turnedRight=False
        # turn left
        if turnedLeft:
            m1.stop()
            m2.stop()
        else:
            m1.power(0)
            m2.power(50)
            m1.ccw()
            m2.ccw()
            time.sleep(4.5)
            turnedLeft=True


    elif result=={'PIC': {'character': '"R"'}}:
        turnedLeft=False
        # turn right
        if turnedRight:
            m1.stop()
            m2.stop()
        else:
            m1.power(0)
            m2.power(50)
            m1.ccw()
            m2.ccw()
            time.sleep(4.5)
            turnedLeft=True
