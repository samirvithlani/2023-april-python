class Gov:
    
    tax = 18.0
    

class StateGov(Gov):
    
    grant = 1000000.0
    
    def getStateData(self):
        print("State Tax: ", self.tax +2.0)
        print("Satte Grant: ", self.grant)    
        
class AMC(StateGov):
    
    roadTax = 1000
    def getAMCData(self):
        print("AMC Tax: ", self.tax + 3.0)
        print("AMC Grant: ", self.grant + 100000.0)
        print("AMC Road Tax: ", self.roadTax)


s = StateGov()
s.getStateData()   

a  = AMC()
a.getAMCData()
a.getStateData()     