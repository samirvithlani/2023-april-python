class InvalidString(Exception):
    
    def __init__(self, msg):
        self.msg = msg
        super().__init__(self.msg)
    

class InvalidAge(Exception):
    
    def __init__(self, msg):
        self.msg = msg
        super().__init__(self.msg)    

        