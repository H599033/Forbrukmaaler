from typing import List
from Regning import Regning

class Konto:
    
    def __init__(self, konto_nr: int, regninger= None, faste_regninger = None,inntekt = None ):
        self.konto_nr = konto_nr
        self.regninger = regninger if regninger is not None else []
        self.faste_regninger = faste_regninger if faste_regninger is not None else []
        self.inntekt = inntekt if inntekt is not None else 0
    
    
    def Finn_faste_regninger(regninger):
        return List
    
    def Finn_inntekt(regninger):
        return float
    
    def Finn_kontont(regninger):
        return int