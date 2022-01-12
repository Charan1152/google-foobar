# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 00:15:39 2021

@author: Charan
"""
import random as r
import pyautogui as p
p.moveTo(1095,1052 ,2)
p.click()
p.moveTo(1381,849,5)
p.click()
while True:
    inp= r.choice(['Karuvu ki namaskaram','Nibbas and Nibbis','Cringe and Awkward','Bull Shit'])
    p.write(inp,interval=0.25)
    p.press('enter') 