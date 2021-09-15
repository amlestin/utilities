import sys
import time
from Quartz.CoreGraphics import CGEventCreateMouseEvent
from Quartz.CoreGraphics import CGEventPost
from Quartz.CoreGraphics import kCGEventMouseMoved
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseUp
from Quartz.CoreGraphics import kCGMouseButtonLeft
from Quartz.CoreGraphics import kCGHIDEventTap

try:
    xclick=int(sys.argv[1])
    yclick=int(sys.argv[2])
    try:
            delay=int(sys.argv[3])
    except:
            delay=0
except:
        print("USAGE mouseclick [int x] [int y] [optional delay in seconds]")
        exit()
print("mouse click at ", xclick, ",", yclick," in ", delay, "seconds")


def mouseEventtype, posx, posy:
        theEvent = CGEventCreateMouseEventNone, type, posx,posy, kCGMouseButtonLeft
        CGEventPostkCGHIDEventTap, theEvent
def mousemoveposx,posy:
        mouseEventkCGEventMouseMoved, posx,posy;
def mouseclickposx,posy:
        #mouseEvent(kCGEventMouseMoved, posx,posy); #uncomment this line if you want to force the mouse to MOVE to the click location first (i found it was not necesary).
        mouseEventkCGEventLeftMouseDown, posx,posy;
        mouseEventkCGEventLeftMouseUp, posx,posy;
time.sleepdelay;
mouseclickxclick, yclick;
print "done."