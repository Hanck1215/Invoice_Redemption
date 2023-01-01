import keyboard
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont
import time
from board import SCL, SDA


class InvoiceRedemptionMachine :
    
    i2c = busio.I2C(SCL, SDA)
    display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

    width, height = 128, 64
    image = Image.new("1", (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    
    current_y = 0
    current_x = 0
    
    def Print(self, content, nextline = False) :
        self.draw.text((self.current_x, self.current_y), content, font=self.font, fill=1)
        self.display.image(self.image)
        self.display.show()
        if nextline is True :
            self.current_x = 0
            self.current_y = self.current_y + 10
        else :
            self.current_x = self.current_x + len(content)*6.2
            
    def display_clear(self) :
        self.current_y = 0
        self.current_x = 0
        self.image = Image.new("1", (self.width, self.height))
        self.draw = ImageDraw.Draw(self.image)
        self.display.image(self.image)
        self.display.show()
        
    
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
    pages = {1:["Redemption", "Store", "Search", "Delete", "end"], 2:["return", "Unique", "Special", "Jackpot", "Second prize", "Thirth prize", "Fourth prize", "Fifth prize", "Sixth prize"], 3:["Continue", "Home page"], 4:["Continue rdt", "Home page"]}
    Input = ""
    
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
        self.display_clear()
        #print(self.current_page, self.pointer)
        
        if self.input_mode is True :
            self.Input = self.Input + num
            self.Print(self.Input)
            return True
        
        catalog = self.pages.get(self.current_page)
        ctlog = ""
        for i in range(1, len(catalog)+1) : #len(catalog)+1
            if self.pointer > 4   and i < 4:
                continue
            if self.pointer > 7   and i < 7:
                continue
            ctlog = ctlog + str(i) + "." + catalog[i-1]
            if i == self.pointer :
                ctlog = ctlog + " <--"
            ctlog = ctlog + "\n"
        print(ctlog)
        self.Print(ctlog)
        
    def keyboard_up(self) :
        
        if self.input_mode is True :
            self.screen_update("8")
            return True
        
        if self.pointer == 1 :
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
            return False
        else :
            self.pointer = self.pointer + 1
            self.screen_update()
            return True
        
    def keyboard_0(self) :
        if self.input_mode is True :
            self.screen_update("0")
        
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
            self.Input = "8 digits:"
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
            self.Input = "Unique : "
            self.screen_update()
            
        elif self.current_page == 2 and self.pointer == 3 and self.input_mode is False :
            self.input_mode = True
            self.Input = "Special: "
            self.screen_update()
            
        elif self.current_page == 2 and self.pointer == 4 and self.input_mode is False :
            self.input_mode = True
            self.Input = "Jackpot: "
            self.screen_update()
            
        elif self.current_page == 2 and self.pointer == 5 and self.input_mode is False :
            self.input_mode = True
            self.Input = "7 digits:"
            self.screen_update()
            
        elif self.current_page == 2 and self.pointer == 6 and self.input_mode is False :
            self.input_mode = True
            self.Input = "6 digits:"
            self.screen_update()
            
        elif self.current_page == 2 and self.pointer == 7 and self.input_mode is False :
            self.input_mode = True
            self.Input = "5 digits:"
            self.screen_update()
            
        elif self.current_page == 2 and self.pointer == 8 and self.input_mode is False :
            self.input_mode = True
            self.Input = "4 digits:"
            self.screen_update()
            
        elif self.current_page == 2 and self.pointer == 9 and self.input_mode is False :
            self.input_mode = True
            self.Input = "3 digits:"
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
            self.Input = "Search : "
            self.screen_update()
            
        elif self.current_page == 1 and self.pointer == 4 and self.input_mode is False :
            self.input_mode = True
            self.Input = "Delete : "
            self.screen_update()
            
        elif self.current_page == 1 and self.pointer == 5 and self.input_mode is False :
            self.input_mode = True
            self.Input = "Thanks "
            self.screen_update()
            time.sleep(5)
            self.display_clear()
            
        
        elif self.pointer == 2 and self.current_page == 1 and self.input_mode is True :
            if len(self.Input) != 17 :
                self.Input = "8 digits: must be \n8 digits!"
                self.screen_update()
                time.sleep(2)
                self.Input = "8 digits:"
                self.screen_update()
            else :
                data = self.Input[9:17]
                self.store(data)
                self.Input = "Successfully! \nPlease put it \nin " + str(self.data_posiotion.get(data)) + " grid"
                self.screen_update()
                time.sleep(5)
                self.input_mode = False
                self.current_page = 3
                self.pointer = 1
                self.Input = "8 digits:"
                self.screen_update()
                
                print("目前有: ", self.database.data)
                
        
        elif self.pointer == 2 and self.current_page == 2 and self.input_mode is True :
            if len(self.Input) != 17 :
                self.Input = "Unique : must be \n8 digits!"
                self.screen_update()
                time.sleep(2)
                self.Input = "Unique : "
                self.screen_update()
            else :
                Special_Award = self.Input[9:17]
                position = self.redemption_Special_Award(Special_Award)
                
                if position == 0 :
                    self.Input = "No"
                    self.screen_update()
                    time.sleep(2)
                    self.input_mode = False
                    self.current_page = 4
                    self.pointer = 1
                    self.Input = "Unique : "
                    self.screen_update()
                else :
                    self.Input = "You win a \nprize! The bill \nis in " + str(position) + " grid."
                    self.screen_update()
                    time.sleep(3)
                    self.input_mode = False
                    self.current_page = 4
                    self.pointer = 1
                    self.Input = "Unique : "
                    self.screen_update()
                    
        elif  self.current_page == 2 and self.pointer == 3 and self.input_mode is True :
            if len(self.Input) != 17 :
                self.Input = "Special: must be \n8 digits!"
                self.screen_update()
                time.sleep(2)
                self.Input = "Special: "
                self.screen_update()
            else :
                Secondary_Special_Award = self.Input[9:17]
                position = self.redemption_Secondary_Special_Award(Secondary_Special_Award)
                
                if position == 0 :
                    self.Input = "No"
                    self.screen_update()
                    time.sleep(2)
                    self.input_mode = False
                    self.current_page = 4
                    self.pointer = 1
                    self.Input = "Special: "
                    self.screen_update()
                else :
                    self.Input = "You win a \nprize! The bill \nis in " + str(position) + " grid."
                    self.screen_update()
                    time.sleep(3)
                    self.input_mode = False
                    self.current_page = 4
                    self.pointer = 1
                    self.Input = "Special: "
                    self.screen_update()
                    
        elif  self.current_page == 2 and self.pointer == 4 and self.input_mode is True :
            if len(self.Input) != 17 :
                self.Input = "Jackpot: must be \n8 digits!"
                self.screen_update()
                time.sleep(2)
                self.Input = "Jackpot: "
                self.screen_update()
            else :
                Jackpot = self.Input[9:17]
                position = self.redemption_Jackpot(Jackpot)
                
                if position == 0 :
                    self.Input = "No"
                    self.screen_update()
                    time.sleep(2)
                    self.input_mode = False
                    self.current_page = 4
                    self.pointer = 1
                    self.Input = "Jackpot: "
                    self.screen_update()
                else :
                    self.Input = "You win a \nprize! The bill \nis in " + str(position) + " grid."
                    self.screen_update()
                    time.sleep(3)
                    self.input_mode = False
                    self.current_page = 4
                    self.pointer = 1
                    self.Input = "Jackpot: "
                    self.screen_update()
                    
        elif  self.current_page == 2 and self.pointer == 5 and self.input_mode is True :
            if len(self.Input) != 16 :
                self.Input = "7 digits: must be \n7 digits!"
                self.screen_update()
                time.sleep(2)
                self.Input = "7 digits:"
                self.screen_update()
            else :
                second_prize = self.Input[9:16]
                nums = self.redemption_second_prize(second_prize)
                
                if len(nums) == 0 :
                    self.Input = "No"
                    self.screen_update()
                    time.sleep(2)
                    self.input_mode = False
                    self.current_page = 4
                    self.pointer = 1
                    self.screen_update()
                else :
                    total = len(nums)
                    for i in range(total) :
                        self.Input = "You win a \nprize! The bill \nis in " + str(self.data_posiotion.get(nums[i])) + " grid, number \nis" + nums[i]
                        self.screen_update()
                        time.sleep(3)
                        if i != (total - 1) :
                            self.Input = "next..."
                            self.screen_update()
                            time.sleep(3)
                            
                    self.input_mode = False
                    self.current_page = 4
                    self.pointer = 1
                    self.screen_update()
                    
        elif  self.current_page == 2 and self.pointer == 6 and self.input_mode is True :
            if len(self.Input) != 15 :
                self.Input = "6 digits: must be \n6 digits!"
                self.screen_update()
                time.sleep(2)
                self.Input = "6 digits:"
                self.screen_update()
            else :
                third_prize = self.Input[9:15]
                nums = self.redemption_third_prize(third_prize)
                
                if len(nums) == 0 :
                    self.Input = "No"
                    self.screen_update()
                    time.sleep(2)
                    self.input_mode = False
                    self.current_page = 4
                    self.pointer = 1
                    self.screen_update()
                else :
                    total = len(nums)
                    for i in range(total) :
                        self.Input = "You win a \nprize! The bill \nis in " + str(self.data_posiotion.get(nums[i])) + " grid, number \nis" + nums[i]
                        self.screen_update()
                        time.sleep(3)
                        
                        if i != (total - 1) :
                             self.Input = "next..."
                             self.screen_update()
                             time.sleep(3)
                                    
                    self.input_mode = False
                    self.current_page = 4
                    self.pointer = 1
                    self.screen_update()
                    
        elif  self.current_page == 2 and self.pointer == 7 and self.input_mode is True :
            if len(self.Input) != 14 :
                self.Input = "5 digits: must be \n5 digits!"
                self.screen_update()
                time.sleep(2)
                self.Input = "5 digits:"
                self.screen_update()
            else :
                fourth_prize = self.Input[9:14]
                nums = self.redemption_fourth_prize(fourth_prize)
                
                if len(nums) == 0 :
                    self.Input = "No"
                    self.screen_update()
                    time.sleep(2)
                    self.input_mode = False
                    self.current_page = 4
                    self.pointer = 1
                    self.screen_update()
                else :
                    total = len(nums)
                    for i in range(total) :
                        self.Input = "You win a \nprize! The bill \nis in " + str(self.data_posiotion.get(nums[i])) + " grid, number \nis" + nums[i]
                        self.screen_update()
                        time.sleep(3)
                        
                        if i != (total - 1) :
                             self.Input = "next..."
                             self.screen_update()
                             time.sleep(3)
                                    
                    self.input_mode = False
                    self.current_page = 4
                    self.pointer = 1
                    self.screen_update()
                    
        elif  self.current_page == 2 and self.pointer == 8 and self.input_mode is True :
            if len(self.Input) != 13 :
                self.Input = "4 digits: must be \n4 digits!"
                self.screen_update()
                time.sleep(2)
                self.Input = "4 digits:"
                self.screen_update()
            else :
                fifth_prize = self.Input[9:13]
                nums = self.redemption_fifth_prize(fifth_prize)
                
                if len(nums) == 0 :
                    self.Input = "No"
                    self.screen_update()
                    time.sleep(2)
                    self.input_mode = False
                    self.current_page = 4
                    self.pointer = 1
                    self.screen_update()
                else :
                    total = len(nums)
                    for i in range(total) :
                        self.Input = "You win a \nprize! The bill \nis in " + str(self.data_posiotion.get(nums[i])) + " grid, number \nis" + nums[i]
                        self.screen_update()
                        time.sleep(3)
                        
                        if i != (total - 1) :
                             self.Input = "next..."
                             self.screen_update()
                             time.sleep(3)
                                    
                    self.input_mode = False
                    self.current_page = 4
                    self.pointer = 1
                    self.screen_update()
                    
        elif  self.current_page == 2 and self.pointer == 9 and self.input_mode is True :
            if len(self.Input) != 12 :
                self.Input = "3 digits: must be \n3 digits!"
                self.screen_update()
                time.sleep(2)
                self.Input = "3 digits:"
                self.screen_update()
            else :
                sixth_prize = self.Input[9:12]
                nums = self.redemption_sixth_prize(sixth_prize)
                
                if len(nums) == 0 :
                    self.Input = "No"
                    self.screen_update()
                    time.sleep(2)
                    self.input_mode = False
                    self.current_page = 4
                    self.pointer = 1
                    self.screen_update()
                else :
                    total = len(nums)
                    for i in range(total) :
                        self.Input = "You win a \nprize! The bill \nis in " + str(self.data_posiotion.get(nums[i])) + " grid, number \nis" + nums[i]
                        self.screen_update()
                        time.sleep(3)
                        
                        if i != (total - 1) :
                             self.Input = "next..."
                             self.screen_update()
                             time.sleep(3)
                                    
                    self.input_mode = False
                    self.current_page = 4
                    self.pointer = 1
                    self.screen_update()
                    
        elif  self.current_page == 1 and self.pointer == 3 and self.input_mode is True :
            if len(self.Input) != 17 :
                self.Input = "Search : must be \n8 digits!"
                self.screen_update()
                time.sleep(2)
                self.Input = "Search : "
                self.screen_update()
            else :
                seek = self.Input[9:17]
                isExist = self.database.search(seek)
                if isExist is True :
                    self.Input = "This bill \nis in " + str(self.data_posiotion.get(seek)) + " grid"
                    self.screen_update()
                    time.sleep(2)
                    self.Input = "return..."
                    self.screen_update()
                    time.sleep(2)
                    self.input_mode = False
                    self.current_page = 1
                    self.pointer = 1
                    self.screen_update()
                else :
                    self.Input = "Not exist~ \nQQ"
                    self.screen_update()
                    time.sleep(2)
                    self.Input = "return..."
                    self.screen_update()
                    time.sleep(2)
                    self.input_mode = False
                    self.current_page = 1
                    self.pointer = 1
                    self.screen_update()
                    
        elif  self.current_page == 1 and self.pointer == 4 and self.input_mode is True :
            if len(self.Input) != 17 :
                self.Input = "Delete : must be \n8 digits!"
                self.screen_update()
                time.sleep(2)
                self.Input = "Delete : "
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
                    self.Input = "successful \nremoval."
                    self.screen_update()
                    time.sleep(2)
                    self.Input = "return..."
                    self.screen_update()
                    time.sleep(2)
                    self.input_mode = False
                    self.current_page = 1
                    self.pointer = 1
                    self.screen_update()
                else :
                    self.Input = "Not exist~ QQ"
                    self.screen_update()
                    time.sleep(2)
                    self.Input = "return..."
                    self.screen_update()
                    time.sleep(2)
                    self.input_mode = False
                    self.current_page = 1
                    self.pointer = 1
                    self.screen_update()
    
    def start(self) :
        while(True) :
            if self.Input == "Thanks " :
                break
            key = keyboard.read_key()
            time.sleep(0.15)
            if key == "0" :
                self.keyboard_0()
            elif key == "1" :
                #print(00000000000)
                self.keyboard_1()
            elif key == "3" :
                self.keyboard_3()
            elif key == "4" :
                self.keyboard_4()
            elif key == "5" :
                self.keyboard_5()
            elif key == "6" :
                self.keyboard_6()
            elif key == "7" :
                self.keyboard_7()
            elif key == "9" :
                self.keyboard_9()
            elif key == "8" :
                self.keyboard_up()
            elif key == "2" :
                self.keyboard_down()
            elif key == "backspace" :
                self.keyboard_backspace()
            elif key == "enter" :
                self.keyboard_enter()
                
    def __init__(self) :
        #keyboard.on_press_key("1", lambda _:self.keyboard_1())
        #keyboard.on_press_key("3", lambda _:self.keyboard_3())
        #keyboard.on_press_key("4", lambda _:self.keyboard_4())
        #keyboard.on_press_key("5", lambda _:self.keyboard_5())
        #keyboard.on_press_key("6", lambda _:self.keyboard_6())
        #keyboard.on_press_key("7", lambda _:self.keyboard_7())
        #keyboard.on_press_key("9", lambda _:self.keyboard_9())
        #keyboard.on_press_key("8", lambda _:self.keyboard_up())
        #keyboard.on_press_key("2", lambda _:self.keyboard_down())
        #keyboard.on_press_key("BackSpace", lambda _:self.keyboard_backspace())
        #keyboard.on_press_key("enter", lambda _:self.keyboard_enter())
        self.input_mode = True
        self.Input = "Welcome!"
        self.screen_update()
        time.sleep(2)
        self.input_mode = False
        self.pointer = 1
        self.current_page = 1
        self.screen_update()
        
a = InvoiceRedemptionMachine()
a.start()
