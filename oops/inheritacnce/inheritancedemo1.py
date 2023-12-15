class Color:
    
    colorcode = 0
    
    def getColorData(self):
        print("Color code: ", self.colorcode)



class Red(Color):
    
    colorValue = "Red"
    
    def getRedColorValue(self):
        print("Color value: ", self.colorValue)   
        print("color code of red = ",self.colorcode + 100)     
    
    

r = Red()
r.getRedColorValue()
r.getColorData()
    
    