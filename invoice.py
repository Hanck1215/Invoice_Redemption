# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 18:10:00 2022

@author: 88696
"""
import keyboard
import time

class InvoiceRedemptionMachine :
    
    data_posiotion = {}
    cursor = 1 
    index_limit = 5 
       
    Special_Award = ""  #特別獎
    Secondary_Special_Award = ""  #特獎
    Jackpot = ""  #頭獎八位數
    second_prize = ""  #七位數
    third_prize = ""  #六位數
    fourth_prize = ""  #五位數
    fifth_prize = ""  #四位數
    sixth_prize = ""  #三位數
    
    seven = {}
    six = {}
    five = {}
    four = {}
    three = {}
    
    pointer = 1
    current_page = 1
    pages = {1:["對獎", "儲存"], 2:["回上頁", "特別獎", "特獎", "頭獎", "二獎", "三獎", "四獎", "五獎", "六獎"], 3:["繼續", "返主頁"]}
    Input = "請輸入八位數字: "
    
    class DataBase :
        data = set()
        
        def save(self, number) :
            self.data.add(number)
            
        def delete(self, number) :
            self.data.discard(number)
            
        def size(self) :
            return len(self.data)
        
        def search(self, number) :
            if number in self.data :
                return True
            else :
                return False
            
    database =  DataBase()
    
    def store(self, number) :
        if len(number) != 8 :
            return 0 #非八位數
        else :
            if self.database.search(number) is True :
                return 1 #此數字已存在
            
            self.database.save(number)
            
            if self.seven.get(number[1:8]) is None :
                self.seven.setdefault(number[1:8], [number])
            else :
                self.seven.get(number[1:8]).append(number)
            
            if self.six.get(number[2:8]) is None :
                self.six.setdefault(number[2:8], [number])
            else :
                self.six.get(number[2:8]).append(number)
                
            if self.five.get(number[3:8]) is None :
                self.five.setdefault(number[3:8], [number])
            else :
                self.five.get(number[3:8]).append(number)
                
            if self.four.get(number[4:8]) is None :
                self.four.setdefault(number[4:8], [number])
            else :
                self.four.get(number[4:8]).append(number)
                
            if self.three.get(number[5:8]) is None :
                self.three.setdefault(number[5:8], [number])
            else :
                self.three.get(number[5:8]).append(number)
                
            self.data_posiotion.setdefault(number, self.cursor)
            self.cursor += 1
            
            if self.cursor == (self.index_limit + 1) :
                self.cursor = 1
                
            return 2 #儲存成功
    
    def redemption_Special_Award(self, number) :
        if self.database.search(number) is True :
            return self.data_posiotion.get(number)
        else :
            return 0
        
    def redemption_Secondary_Special_Award(self, number) :
        if self.database.search(number) is True :
            return self.data_posiotion.get(number)
        else :
            return 0
        
    def redemption_Jackpot(self, number) :
        if self.database.search(number) is True :
            return self.data_posiotion.get(number)
        else :
            return 0
        
    def redemption_second_prize(self, number) :
        seven_num = number[1:8]
        if self.seven.get(seven_num) is not None :
            return self.seven.get(seven_num)
        else :
            return []
        
    def redemption_third_prize(self, number) :
        six_num = number[2:8]
        if self.six.get(six_num) is not None :
            return self.six.get(six_num)
        else :
            return []
        
    def redemption_fourth_prize(self, number) :
        five_num = number[3:8]
        if self.five.get(five_num) is not None :
            return self.five.get(five_num)
        else :
            return []
        
    def redemption_fifth_prize(self, number) :
        four_num = number[4:8]
        if self.four.get(four_num) is not None :
            return self.four.get(four_num)
        else :
            return []
        
    def redemption_sixth_prize(self, number) :
        
        three_num = number[5:8]
        if self.three.get(three_num) is not None :
            return self.three.get(three_num)
        else :
            return []
    
    def screen_update(self, num = "") :
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        #print(self.current_page, self.pointer)
        
        if self.pointer is False :
            self.Input = self.Input + num
            print(self.Input)
            return True
        
        catalog = self.pages.get(self.current_page)
        for i in range(1, len(catalog)+1) :
           
            print(i, ".", catalog[i-1], end = "")
            if i == self.pointer :
                print(" <--", end = "")
            print()
            
    def keyboard_up(self) :
        
        if self.pointer is False :
            self.screen_update("8")
            return True
        
        if self.pointer == 1 :
            self.screen_update()
            return False
        else :
            self.pointer = self.pointer - 1
            self.screen_update()
            return True
        
    
    def keyboard_down(self) :
        
        if self.pointer is False :
            self.screen_update("2")
            return True
        
        catalog = self.pages.get(self.current_page)
        length = len(catalog)
        
        if self.pointer == length :
            self.screen_update()
            return False
        else :
            self.pointer = self.pointer + 1
            self.screen_update()
            return True
        
    def keyboard_1(self) :
        if self.pointer is False :
            self.screen_update("1")
            
    def keyboard_3(self) :
        if self.pointer is False :
            self.screen_update("3")
            
    def keyboard_4(self) :
        if self.pointer is False :
            self.screen_update("4")
            
    def keyboard_5(self) :
        if self.pointer is False :
            self.screen_update("5")
            
    def keyboard_6(self) :
        if self.pointer is False :
            self.screen_update("6")
            
    def keyboard_7(self) :
        if self.pointer is False :
            self.screen_update("7")
            
    def keyboard_9(self) :
        if self.pointer is False :
            self.screen_update("9")
        
    def keyboard_enter(self) :
        if self.pointer == 1 and self.current_page == 1 :
            print(100)
            self.current_page = 2
            self.screen_update()
            
        elif self.pointer == 2 and self.current_page == 1 :
            self.pointer = False
            self.current_page = 1
            self.screen_update()
            
            
        elif self.current_page == 2 and self.pointer == 1 :
            self.current_page = 1
            self.screen_update()
            
        elif self.current_page == 3 and self.pointer == 1 :
            self.pointer = False
            self.current_page = 1
            self.screen_update()
            
        elif self.current_page == 3 and self.pointer == 2 :
            self.pointer = 1
            self.current_page = 1
            self.screen_update()
            
        elif self.current_page == 2 and self.pointer != 1 :
            self.pointer = False
            self.screen_update()
        
        elif self.pointer is False :
            if len(self.Input) != 17 :
                self.Input = "請輸入八位數字: 必須是八位數!"
                self.screen_update()
                time.sleep(2)
                self.Input = "請輸入八位數字: "
                self.screen_update()
            else :
                if self.current_page == 1 :
                    self.store(self.Input[9:17])
                    print(self.pointer)
                    self.Input = "儲存成功!"
                    self.screen_update()
                    time.sleep(1)
                    self.current_page = 3
                    self.pointer = 1
                    self.Input = "請輸入八位數字: "
                    self.screen_update()
                    print("目前有: ", self.database.data)
                elif self.current_page == 2 :
                    if self.pointer == 2 :
                        print()

    def __init__(self) :
        keyboard.on_press_key("1", lambda _:self.keyboard_1())
        keyboard.on_press_key("3", lambda _:self.keyboard_3())
        keyboard.on_press_key("4", lambda _:self.keyboard_4())
        keyboard.on_press_key("5", lambda _:self.keyboard_5())
        keyboard.on_press_key("6", lambda _:self.keyboard_6())
        keyboard.on_press_key("7", lambda _:self.keyboard_7())
        keyboard.on_press_key("9", lambda _:self.keyboard_9())
        keyboard.on_press_key("8", lambda _:self.keyboard_up())
        keyboard.on_press_key("2", lambda _:self.keyboard_down())
        keyboard.on_press_key("enter", lambda _:self.keyboard_enter())
        self.pointer = False
        self.Input = "歡迎使用發票對獎機!"
        self.screen_update()
        time.sleep(2)
        self.pointer = 1
        self.current_page = 1
        self.Input = "請輸入八位數字: "
        self.screen_update()
        
    
a = InvoiceRedemptionMachine()

        
            
    

    
       
        
        
        
        
       
    