from PIL import ImageGrab
import time
import keyboard
import pyautogui as pg
bb = (709, 747, 1191, 881)
bx1 = 160
bx2 = 200
by1 = 46
vx1 = 151
vy1 = 42
vy2 = 69
white = '(255, 255, 255)'
bolhas = '(68, 252, 234)'
verde = '(83, 250, 83)'
cc = (166, 130, 1571, 892)
cx1 = 74
cx2 = 1325
cy1 = 83
c = 0


b = 0

v = 1
while True:
    try:
        px2 = ImageGrab.grab(bbox=cc).load()    
        for i in range(cx1, cx2):
            for j in range(0,20):

                color = str(px2[i,cy1+(j*30)])


                if color == bolhas:
                    c = 1
        if c == 1:
            pg.click()
            time.sleep(0.2)
            w2 = 1
            while w2 == 1:
                px = ImageGrab.grab(bbox=bb).load()
                for i in range(bx1, bx2):
                    color = str(px[i,by1])
                    if color == white:
                        b = 1
                for z in range(vy1, vy2):
                    color3 = str(px[vx1,z])
                    if color3 == verde:
                        v = 1
                if v == 0:
                    w2 = 0
                    time.sleep(2)
                    pg.click()
                if b == 1:
                    pg.click()
                v = 0
                b = 0
        
    except:
        pass
    c = 0
