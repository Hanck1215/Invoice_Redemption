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
    
    seven = {}
    six = {}
    five = {}
    four = {}
    three = {}
    
    pointer = 1
    current_page = 1
    input_mode = False
    pages = {1:["對獎", "儲存", "搜尋", "刪除"], 2:["回上頁", "特別獎", "特獎", "頭獎", "二獎", "三獎", "四獎", "五獎", "六獎"], 3:["繼續", "返主頁"], 4:["繼續兌獎", "返主頁"]}
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
        if self.seven.get(number) is not None :
            return self.seven.get(number)
        else :
            return []
        
    def redemption_third_prize(self, number) :
        if self.six.get(number) is not None :
            return self.six.get(number)
        else :
            return []
        
    def redemption_fourth_prize(self, number) :
        if self.five.get(number) is not None :
            return self.five.get(number)
        else :
            return []
        
    def redemption_fifth_prize(self, number) :
        if self.four.get(number) is not None :
            return self.four.get(number)
        else :
            return []
        
    def redemption_sixth_prize(self, number) :
        if self.three.get(number) is not None :
            return self.three.get(number)
        else :
            return []
    
    def screen_update(self, num = "") :
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        #print(self.current_page, self.pointer)
        
        if self.input_mode is True :
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
        
        if self.input_mode is True :
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
        
        if self.input_mode is True :
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
        if self.input_mode is True :
            self.screen_update("1")
            
    def keyboard_3(self) :
        if self.input_mode is True :
            self.screen_update("3")
            
    def keyboard_4(self) :
        if self.input_mode is True :
            self.screen_update("4")
            
    def keyboard_5(self) :
        if self.input_mode is True :
            self.screen_update("5")
            
    def keyboard_6(self) :
        if self.input_mode is True :
            self.screen_update("6")
            
    def keyboard_7(self) :
        if self.input_mode is True :
            self.screen_update("7")
            
    def keyboard_9(self) :
        if self.input_mode is True :
            self.screen_update("9")
            
    def keyboard_backspace(self) :
        if self.input_mode is True and len(self.Input) > 9:
            str_len = len(self.Input)
            self.Input = self.Input[0:str_len-1]
            self.screen_update()
        
    def keyboard_enter(self) :
        if self.pointer == 1 and self.current_page == 1 and self.input_mode is False :
            self.current_page = 2
            self.screen_update()
            
        elif self.pointer == 2 and self.current_page == 1 and self.input_mode is False :
            self.input_mode = True
            self.Input = "請輸入八位數字: "
            self.screen_update()
            
        elif self.current_page == 2 and self.pointer == 1 and self.input_mode is False :
            self.current_page = 1
            self.screen_update()
            
        elif self.current_page == 3 and self.pointer == 1 and self.input_mode is False :
            self.input_mode = True
            self.current_page = 1
            self.pointer = 2 
            self.screen_update()
            
        elif self.current_page == 3 and self.pointer == 2 and self.input_mode is False :
            self.input_mode = False
            self.pointer = 1
            self.current_page = 1
            self.screen_update()
            
        elif self.current_page == 2 and self.pointer == 2 and self.input_mode is False :
            self.input_mode = True
            self.Input = "輸入特別獎八碼: "
            self.screen_update()
            
        elif self.current_page == 2 and self.pointer == 3 and self.input_mode is False :
            self.input_mode = True
            self.Input = "請輸入特獎八碼: "
            self.screen_update()
            
        elif self.current_page == 2 and self.pointer == 4 and self.input_mode is False :
            self.input_mode = True
            self.Input = "請輸入頭獎八碼: "
            self.screen_update()
            
        elif self.current_page == 2 and self.pointer == 5 and self.input_mode is False :
            self.input_mode = True
            self.Input = "請輸入二獎七碼: "
            self.screen_update()
            
        elif self.current_page == 2 and self.pointer == 6 and self.input_mode is False :
            self.input_mode = True
            self.Input = "請輸入三獎六碼: "
            self.screen_update()
            
        elif self.current_page == 2 and self.pointer == 7 and self.input_mode is False :
            self.input_mode = True
            self.Input = "請輸入四獎五碼: "
            self.screen_update()
            
        elif self.current_page == 2 and self.pointer == 8 and self.input_mode is False :
            self.input_mode = True
            self.Input = "請輸入五獎四碼: "
            self.screen_update()
            
        elif self.current_page == 2 and self.pointer == 9 and self.input_mode is False :
            self.input_mode = True
            self.Input = "請輸入六獎三碼: "
            self.screen_update()
            
        elif self.current_page == 4 and self.pointer == 1 and self.input_mode is False :
            self.input_mode = False
            self.current_page = 2
            self.pointer = 1
            self.screen_update()
            
            
        elif self.current_page == 4 and self.pointer == 2 and self.input_mode is False :
            self.input_mode = False
            self.pointer = 1
            self.current_page = 1
            self.screen_update()
            
        elif self.current_page == 1 and self.pointer == 3 and self.input_mode is False :
            self.input_mode = True
            self.Input = "輸入欲查詢號碼: "
            self.screen_update()
            
        elif self.current_page == 1 and self.pointer == 4 and self.input_mode is False :
            self.input_mode = True
            self.Input = "輸入欲刪除號碼: "
            self.screen_update()
            
        
        elif self.pointer == 2 and self.current_page == 1 and self.input_mode is True :
            if len(self.Input) != 17 :
                self.Input = "請輸入八位數字: 必須是八位數!"
                self.screen_update()
                time.sleep(2)
                self.Input = "請輸入八位數字: "
                self.screen_update()
            else :
                data = self.Input[9:17]
                self.store(data)
                self.Input = "儲存成功! 請放置在第" + str(self.data_posiotion.get(data)) + "儲存格"
                self.screen_update()
                time.sleep(1)
                self.input_mode = False
                self.current_page = 3
                self.pointer = 1
                self.Input = "請輸入八位數字: "
                self.screen_update()
                print("目前有: ", self.database.data)
                
        
        elif self.pointer == 2 and self.current_page == 2 and self.input_mode is True :
            if len(self.Input) != 17 :
                self.Input = "輸入特別獎八碼: 必須是八位數!"
                self.screen_update()
                time.sleep(2)
                self.Input = "輸入特別獎八碼: "
                self.screen_update()
            else :
                Special_Award = self.Input[9:17]
                position = self.redemption_Special_Award(Special_Award)
                
                if position == 0 :
                    self.Input = "沒有中獎"
                    self.screen_update()
                    time.sleep(2)
                    self.input_mode = False
                    self.current_page = 4
                    self.pointer = 1
                    self.Input = "輸入特別獎八碼: "
                    self.screen_update()
                else :
                    self.Input = "恭喜中獎! 中獎發票位在第" + str(position) + "格"
                    self.screen_update()
                    time.sleep(3)
                    self.input_mode = False
                    self.current_page = 4
                    self.pointer = 1
                    self.Input = "輸入特別獎八碼: "
                    self.screen_update()
                    
        elif  self.current_page == 2 and self.pointer == 3 and self.input_mode is True :
            if len(self.Input) != 17 :
                self.Input = "請輸入特獎八碼: 必須是八位數!"
                self.screen_update()
                time.sleep(2)
                self.Input = "請輸入特獎八碼: "
                self.screen_update()
            else :
                Secondary_Special_Award = self.Input[9:17]
                position = self.redemption_Secondary_Special_Award(Secondary_Special_Award)
                
                if position == 0 :
                    self.Input = "沒有中獎"
                    self.screen_update()
                    time.sleep(2)
                    self.input_mode = False
                    self.current_page = 4
                    self.pointer = 1
                    self.Input = "請輸入特獎八碼: "
                    self.screen_update()
                else :
                    self.Input = "恭喜中獎! 中獎發票位在第" + str(position) + "格"
                    self.screen_update()
                    time.sleep(3)
                    self.input_mode = False
                    self.current_page = 4
                    self.pointer = 1
                    self.Input = "請輸入特獎八碼: "
                    self.screen_update()
                    
        elif  self.current_page == 2 and self.pointer == 4 and self.input_mode is True :
            if len(self.Input) != 17 :
                self.Input = "請輸入頭獎八碼: 必須是八位數!"
                self.screen_update()
                time.sleep(2)
                self.Input = "請輸入頭獎八碼: "
                self.screen_update()
            else :
                Jackpot = self.Input[9:17]
                position = self.redemption_Jackpot(Jackpot)
                
                if position == 0 :
                    self.Input = "沒有中獎"
                    self.screen_update()
                    time.sleep(2)
                    self.input_mode = False
                    self.current_page = 4
                    self.pointer = 1
                    self.Input = "請輸入頭獎八碼: "
                    self.screen_update()
                else :
                    self.Input = "恭喜中獎! 中獎發票位在第" + str(position) + "格"
                    self.screen_update()
                    time.sleep(3)
                    self.input_mode = False
                    self.current_page = 4
                    self.pointer = 1
                    self.Input = "請輸入頭獎八碼: "
                    self.screen_update()
                    
        elif  self.current_page == 2 and self.pointer == 5 and self.input_mode is True :
            if len(self.Input) != 16 :
                self.Input = "請輸入二獎七碼: 必須是七位數!"
                self.screen_update()
                time.sleep(2)
                self.Input = "請輸入二獎七碼: "
                self.screen_update()
            else :
                second_prize = self.Input[9:16]
                nums = self.redemption_second_prize(second_prize)
                
                if len(nums) == 0 :
                    self.Input = "沒有中獎"
                    self.screen_update()
                    time.sleep(2)
                    self.input_mode = False
                    self.current_page = 4
                    self.pointer = 1
                    self.screen_update()
                else :
                    total = len(nums)
                    for i in range(total) :
                        self.Input = "恭喜中獎! 中獎發票位在第" + str(self.data_posiotion.get(nums[i])) + "格\n號碼為" + nums[i]
                        self.screen_update()
                        time.sleep(3)
                        if i != (total - 1) :
                            self.Input = "下一張..."
                            self.screen_update()
                            time.sleep(3)
                            
                    self.input_mode = False
                    self.current_page = 4
                    self.pointer = 1
                    self.screen_update()
                    
        elif  self.current_page == 2 and self.pointer == 6 and self.input_mode is True :
            if len(self.Input) != 15 :
                self.Input = "請輸入三獎六碼: 必須是六位數!"
                self.screen_update()
                time.sleep(2)
                self.Input = "請輸入三獎六碼: "
                self.screen_update()
            else :
                third_prize = self.Input[9:15]
                nums = self.redemption_third_prize(third_prize)
                
                if len(nums) == 0 :
                    self.Input = "沒有中獎"
                    self.screen_update()
                    time.sleep(2)
                    self.input_mode = False
                    self.current_page = 4
                    self.pointer = 1
                    self.screen_update()
                else :
                    total = len(nums)
                    for i in range(total) :
                        self.Input = "恭喜中獎! 中獎發票位在第" + str(self.data_posiotion.get(nums[i])) + "格\n號碼為" + nums[i]
                        self.screen_update()
                        time.sleep(3)
                        
                        if i != (total - 1) :
                             self.Input = "下一張..."
                             self.screen_update()
                             time.sleep(3)
                                    
                    self.input_mode = False
                    self.current_page = 4
                    self.pointer = 1
                    self.screen_update()
                    
        elif  self.current_page == 2 and self.pointer == 7 and self.input_mode is True :
            if len(self.Input) != 14 :
                self.Input = "請輸入四獎五碼: 必須是五位數!"
                self.screen_update()
                time.sleep(2)
                self.Input = "請輸入四獎五碼: "
                self.screen_update()
            else :
                fourth_prize = self.Input[9:14]
                nums = self.redemption_fourth_prize(fourth_prize)
                
                if len(nums) == 0 :
                    self.Input = "沒有中獎"
                    self.screen_update()
                    time.sleep(2)
                    self.input_mode = False
                    self.current_page = 4
                    self.pointer = 1
                    self.screen_update()
                else :
                    total = len(nums)
                    for i in range(total) :
                        self.Input = "恭喜中獎! 中獎發票位在第" + str(self.data_posiotion.get(nums[i])) + "格\n號碼為" + nums[i]
                        self.screen_update()
                        time.sleep(3)
                        
                        if i != (total - 1) :
                             self.Input = "下一張..."
                             self.screen_update()
                             time.sleep(3)
                                    
                    self.input_mode = False
                    self.current_page = 4
                    self.pointer = 1
                    self.screen_update()
                    
        elif  self.current_page == 2 and self.pointer == 8 and self.input_mode is True :
            if len(self.Input) != 13 :
                self.Input = "請輸入五獎四碼: 必須是四位數!"
                self.screen_update()
                time.sleep(2)
                self.Input = "請輸入五獎四碼: "
                self.screen_update()
            else :
                fifth_prize = self.Input[9:13]
                nums = self.redemption_fifth_prize(fifth_prize)
                
                if len(nums) == 0 :
                    self.Input = "沒有中獎"
                    self.screen_update()
                    time.sleep(2)
                    self.input_mode = False
                    self.current_page = 4
                    self.pointer = 1
                    self.screen_update()
                else :
                    total = len(nums)
                    for i in range(total) :
                        self.Input = "恭喜中獎! 中獎發票位在第" + str(self.data_posiotion.get(nums[i])) + "格\n號碼為" + nums[i]
                        self.screen_update()
                        time.sleep(3)
                        
                        if i != (total - 1) :
                             self.Input = "下一張..."
                             self.screen_update()
                             time.sleep(3)
                                    
                    self.input_mode = False
                    self.current_page = 4
                    self.pointer = 1
                    self.screen_update()
                    
        elif  self.current_page == 2 and self.pointer == 9 and self.input_mode is True :
            if len(self.Input) != 12 :
                self.Input = "請輸入六獎三碼: 必須是三位數!"
                self.screen_update()
                time.sleep(2)
                self.Input = "請輸入六獎三碼: "
                self.screen_update()
            else :
                sixth_prize = self.Input[9:12]
                nums = self.redemption_sixth_prize(sixth_prize)
                
                if len(nums) == 0 :
                    self.Input = "沒有中獎"
                    self.screen_update()
                    time.sleep(2)
                    self.input_mode = False
                    self.current_page = 4
                    self.pointer = 1
                    self.screen_update()
                else :
                    total = len(nums)
                    for i in range(total) :
                        self.Input = "恭喜中獎! 中獎發票位在第" + str(self.data_posiotion.get(nums[i])) + "格\n號碼為" + nums[i]
                        self.screen_update()
                        time.sleep(3)
                        
                        if i != (total - 1) :
                             self.Input = "下一張..."
                             self.screen_update()
                             time.sleep(3)
                                    
                    self.input_mode = False
                    self.current_page = 4
                    self.pointer = 1
                    self.screen_update()
                    
        elif  self.current_page == 1 and self.pointer == 3 and self.input_mode is True :
            if len(self.Input) != 17 :
                self.Input = "輸入欲查詢號碼: 必須是八位數!"
                self.screen_update()
                time.sleep(2)
                self.Input = "輸入欲查詢號碼: "
                self.screen_update()
            else :
                seek = self.Input[9:17]
                isExist = self.database.search(seek)
                if isExist is True :
                    self.Input = "此發票存在於第" + str(self.data_posiotion.get(seek)) + "格"
                    self.screen_update()
                    time.sleep(2)
                    self.Input = "返回主頁..."
                    self.screen_update()
                    time.sleep(2)
                    self.input_mode = False
                    self.current_page = 1
                    self.pointer = 1
                    self.screen_update()
                else :
                    self.Input = "此發票不存在QQ"
                    self.screen_update()
                    time.sleep(2)
                    self.Input = "返回主頁..."
                    self.screen_update()
                    time.sleep(2)
                    self.input_mode = False
                    self.current_page = 1
                    self.pointer = 1
                    self.screen_update()
                    
        elif  self.current_page == 1 and self.pointer == 4 and self.input_mode is True :
            if len(self.Input) != 17 :
                self.Input = "輸入欲刪除號碼: 必須是八位數!"
                self.screen_update()
                time.sleep(2)
                self.Input = "輸入欲刪除號碼: "
                self.screen_update()
            else :
                seek = self.Input[9:17]
                isExist = self.database.search(seek)
                if isExist is True :
                    self.database.delete(seek)
                    self.data_posiotion.pop(seek)
                    self.seven.get(seek[1:8]).remove(seek)
                    self.six.get(seek[2:8]).remove(seek)
                    self.five.get(seek[3:8]).remove(seek)
                    self.four.get(seek[4:8]).remove(seek)
                    self.three.get(seek[5:8]).remove(seek)
                    self.Input = "成功刪除"
                    self.screen_update()
                    time.sleep(2)
                    self.Input = "返回主頁..."
                    self.screen_update()
                    time.sleep(2)
                    self.input_mode = False
                    self.current_page = 1
                    self.pointer = 1
                    self.screen_update()
                else :
                    self.Input = "此發票不存在QQ"
                    self.screen_update()
                    time.sleep(2)
                    self.Input = "返回主頁..."
                    self.screen_update()
                    time.sleep(2)
                    self.input_mode = False
                    self.current_page = 1
                    self.pointer = 1
                    self.screen_update()
                
                

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
        keyboard.on_press_key("BackSpace", lambda _:self.keyboard_backspace())
        keyboard.on_press_key("enter", lambda _:self.keyboard_enter())
        self.input_mode = True
        self.Input = "歡迎使用發票對獎機!"
        self.screen_update()
        time.sleep(2)
        self.input_mode = False
        self.pointer = 1
        self.current_page = 1
        self.screen_update()
        
    
a = InvoiceRedemptionMachine()

        
            
    

    
       
        
        
        
        
       
    