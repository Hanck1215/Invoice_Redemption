# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 18:29:22 2022

@author: 88696
"""

import keyboard

while True:
    if keyboard.read_key() == "9":
        print("You pressed p")
        break

while True:
    if keyboard.is_pressed("r"):
        print("You pressed q")
        break
        
keyboard.on_press_key("5", lambda _:print("You pressed r"))