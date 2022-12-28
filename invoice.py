# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 18:10:00 2022

@author: 88696
"""
from pynput import keyboard

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
    Jackpot_To_SixthPrize = []  #頭獎~六獎
    
    eight = set()
    seven = {}
    six = {}
    five = {}
    four = {}
    three = {}


    def store(self) :
        
        while(True) :
            number = input("請輸入欲存入的兌獎八碼: ")
            
            if number == "-" :
                print("回上頁")
                break 
            
            if len(number) != 8 :
                print("須為八個數字!")
                continue
            else :
                if self.database.search(number) is True :
                    print("此數字已存在")
                    continue
                
                self.database.save(number)
                
                self.eight.add(number)
                
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
                print("儲存成功")
                continue
    
    def redemption(self) :
        
        
            
    

    
       
        
        
        
        
       
    