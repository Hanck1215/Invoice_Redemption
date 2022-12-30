# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 18:29:22 2022

@author: 88696
"""

import keyboard
import time

#keyboard.on_press_key("num lock", lambda _:print("You pressed r"))

class oled_displayer :
    cursor = 1
    current_page = 1
    pages = {1:["對獎", "儲存"], 2:["回上頁", "特別獎", "特獎", "頭獎", "二獎", "三獎", "四獎", "五獎", "六獎"], 3:["繼續", "返主頁"]}
    Input = "請輸入八位數字: "
        #
        #
    def screen_update(self, num = "") :
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(self.current_page, self.cursor)
        
        if self.cursor is False :
            self.Input = self.Input + num
            print(self.Input)
            return True
        
        catalog = self.pages.get(self.current_page)
        for i in range(1, len(catalog)+1) :
           
            print(i, ".", catalog[i-1], end = "")
            if i == self.cursor :
                print(" <--", end = "")
            print()
        
    def keyboard_up(self) :
        
        
        if self.cursor is False :
            self.screen_update("8")
            return True
        
        if self.cursor == 1 :
            self.screen_update()
            return False
        else :
            self.cursor = self.cursor - 1
            self.screen_update()
            return True
        
    
    def keyboard_down(self) :
        
        if self.cursor is False :
            self.screen_update("2")
            return True
        
        catalog = self.pages.get(self.current_page)
        length = len(catalog)
        
        if self.cursor == length :
            self.screen_update()
            return False
        else :
            self.cursor = self.cursor + 1
            self.screen_update()
            return True
        
        
    def keyboard_enter(self) :
        if self.cursor == 1 and self.current_page == 1 :
            print(100)
            self.current_page = 2
            self.screen_update()
            
        elif self.cursor == 2 and self.current_page == 1 :
            self.cursor = False
            self.current_page = 1
            self.screen_update()
            
            
        elif self.current_page == 2 and self.cursor == 1 :
            self.current_page = 1
            self.screen_update()
            
        elif self.current_page == 3 and self.cursor == 1 :
            self.cursor = False
            self.current_page = 1
            self.screen_update()
            
        elif self.current_page == 3 and self.cursor == 2 :
            self.cursor = 1
            self.current_page = 1
            self.screen_update()
        
        elif self.cursor is False :
            if len(self.Input) != 17 :
                self.Input = "請輸入八位數字: 必須是八位數!"
                self.screen_update()
                time.sleep(5)
                self.Input = "請輸入八位數字: "
                self.screen_update()
            else :
                if self.current_page == 1 :
                    self.Input = "儲存成功!"
                    self.screen_update()
                    time.sleep(3)
                    self.current_page = 3
                    self.cursor = 1
                    self.Input = "請輸入八位數字: "
                    self.screen_update()
                    
                    
        
        

    def __init__(self) :
        keyboard.on_press_key("8", lambda _:self.keyboard_up())
        keyboard.on_press_key("2", lambda _:self.keyboard_down())
        keyboard.on_press_key("enter", lambda _:self.keyboard_enter())
        print("歡迎使用發票對獎機!")
        time.sleep(2)
        self.screen_update()
        
        
        
        
        



a = oled_displayer()



