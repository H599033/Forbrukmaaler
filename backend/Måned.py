from datetime import datetime

class Måned:
    def __init__(self, måned: datetime.month, regninger= None, faste_regninger = None,inntekt = None ):
        self.måned = måned
        self.regninger = regninger if regninger is not None else []
        self.faste_regninger = faste_regninger if faste_regninger is not None else []
        self.inntekt = inntekt if inntekt is not None else 0
    
    
    
    