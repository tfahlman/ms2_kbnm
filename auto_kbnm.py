import pyautogui
import win32gui
import time
import sys
import timeit
import math

pyautogui.PAUSE = 1.5
pyautogui.FAILSAFE = True #moving mouse to upper left corner will stop pyautogui
pyautogui.MINUMUM_DURATION = 0.1
pyautogui.MAXIMUM_DURATION = 1.5
print("your screen res is %sx%s" %(pyautogui.size()[0], pyautogui.size()[1]))
print("IMPORTANT: DO NOT Minimize MapleStory 2 window")
#TODO: set different mouse cordinates for different screen res

window_name = "Untitled - Paint"
whnd = win32gui.FindWindowEx(None,None,None, window_name)
if (whnd != 0 ):
    win32gui.SetForegroundWindow(whnd)
    print("FOUND")
    #TODO: work around if MapleStory window is Minimized
else:
    print("NOPE")

for i in list(range(2))[::-1]:
    print(i+1)
    time.sleep(1)

i = 0
while i < 5:
    print(pyautogui.position())
    # while:
    #1st click(1750,239) From starting position to upper platform
    start = timeit.default_timer()
    pyautogui.moveTo(1750, 239, 1, pyautogui.easeOutQuad)
    pyautogui.mouseDown(button='left')
    pyautogui.mouseUp(button='left')
    # time.sleep(1)
    pyautogui.press('5')
    # time.sleep(0.5)

    #2nd click(1600,830) Go from upper platform to lower platform
    pyautogui.moveTo(1600, 830, 1, pyautogui.easeOutQuad)
    pyautogui.mouseDown(button='left')
    pyautogui.mouseUp(button='left')
    # time.sleep(1)

    #3rd click(1850,830) Finish going to lower platform
    pyautogui.moveTo(1850, 830, 1, pyautogui.easeOutQuad)
    pyautogui.mouseDown(button='left')
    pyautogui.mouseUp(button='left')
    # time.sleep(1)
    # pyautogui.press('5')
    # tim5e.sleep(0.5)

    #4th click(510,610) Move to upper left platform
    pyautogui.moveTo(510, 610, 1, pyautogui.easeOutQuad)
    pyautogui.mouseDown(button='left')
    pyautogui.mouseUp(button='left')
    # time.sleep(2)
    #5th click(380,610) Move to original position
    pyautogui.moveTo(380, 610, 1, pyautogui.easeOutQuad)
    pyautogui.mouseDown(button='left')
    pyautogui.mouseUp(button='left')
    # pyautogui.press('5')
    end = timeit.default_timer()

    loop_time = math.floor(end-start)
    print(loop_time)
    i += 1
    print(i)

#685_loop
# sys.exit(0)
# (461194, 'nodejs')
# (459054, 'Realtek Audio Console')
# (525052, 'Realtek Audio Console')
# (132258, 'Settings')
# (66526, 'Skype for Business Basic')
# (131700, 'Settings')
# (393538, 'Calculator')
# (132108, 'Calculator')
# (65988, 'Sticky Notes')
# (66476, 'Spotify')
# (131396, 'Program Manager')
