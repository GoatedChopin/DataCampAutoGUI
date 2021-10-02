import pyautogui as pag
import time
import os
from PIL import ImageGrab, Image
import numpy as np
import cv2 as cv

# load in DataCamp images: ("Take Hint", "Show Answer", "got it", "Run Solution", play, etc.)
max_x, max_y = pag.size();

if os.getcwd() != 'Picture Directory':
    os.chdir('Picture Directory')

confidenceLevel = 0.7

continueButton = cv.imread('continue.png')
playButton = cv.imread('playButton.png')
gotIt = cv.imread('gotIt.png')
takeHint = cv.imread('takeHint.png')
showAnswer = cv.imread('showAnswer.png')
runSolution = cv.imread('runSolution.png')
skip = cv.imread('skip.png')
stars = cv.imread('stars.png')
star = cv.imread('star.png')
dArrow = cv.imread('dArrow.png')
submitAnswer = cv.imread('submitAnswer.png')
bubble = cv.imread('bubble.png')
filledBubble = cv.imread('filledBubble.png')

currentMatch = None

def onScreen(image, region = (0, 0, max_x - 1, max_y - 1)):
    global currentMatch
    screen = ImageGrab.grab(bbox=region)
    screen_cv = cv.cvtColor(np.array(screen), cv.COLOR_RGB2BGR)
    res = cv.matchTemplate(screen_cv, image, cv.TM_CCOEFF_NORMED)
    if (res >= confidenceLevel).any():
        currentMatch = res
    return (res >= confidenceLevel).any()

def find(image, region = (0, 0, max_x - 1, max_y - 1)):
    global currentMatch
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(currentMatch)
    return max_loc

def press(tuple):
    pag.moveTo(tuple)
    pag.click(tuple)

time.sleep(5)

# Main Loop
run = True
while run:
    
    if onScreen(continueButton):
        press(find(continueButton))
    
    if onScreen(playButton):
        press(find(playButton))
        time.sleep(295)
        press(find(gotIt))
        

    if onScreen(takeHint):
        press(find(takeHint))
    
    if onScreen(showAnswer):
        press(find(showAnswer))
        if onScreen(submitAnswer):
            press(find(submitAnswer))
            pag.press('enter')
            
    if onScreen(runSolution):
        press(find(runSolution))
        time.sleep(3)
        pag.press('enter')
    
    if onScreen(skip):
        press(find(skip))
    
    if onScreen(stars):
        starList = list(pag.locateAllOnScreen(star))
        fiveStar = starList[-1]
        press(fiveStar)
    
    if onScreen(dArrow):
        arrowList = list(pag.locateAllOnScreen(dArrow))
        for i in arrowList:
            pag.moveTo(pag.center(i))
            pag.mouseDown()
            time.sleep(1)
            pag.mouseUp()
        
    if onScreen(filledBubble):
        pag.press('enter')
        bubbleTime = True
        attempts = 0
        while bubbleTime:
            if onScreen(bubble):
                x_coord, y_coord = find(bubble)
                x_coord += int(bubble.shape[0] / 2)
                y_coord += int(bubble.shape[1] / 2)
                press((x_coord, y_coord))
                time.sleep(0.3)
                pag.press('enter')
            else:
                bubbleTime = False
            
            attempts += 1
            
            if attempts >= 10:
                bubbleTime = False

    if onScreen(bubble):
        for i in range(1, 4):
            pag.press('num' + str(i))
            pag.press('enter')
    
    

    pag.moveTo(int(max_x / 2), 0, 0.5)
    pag.press('enter')
    pag.hotkey('ctrl','shift','enter')
