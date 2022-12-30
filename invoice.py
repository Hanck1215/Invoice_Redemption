# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 18:10:00 2022

@author: 88696
"""

class InvoiceRedemptionMachine :
        
    
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
        

        
        
        
        
            
    

    
       
        
        
        
        
       
    