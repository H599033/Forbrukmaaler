from typing import List
from Regning import Regning
from Maaned import Maaned
from typing import List, Optional
class Konto:
    
    def __init__(self, konto_nr: int, alle_aar = None, faste_regninger = None,inntekt = None ):
        self.konto_nr = konto_nr
        self.alle_aar = alle_aar if alle_aar is not None else []
        self.faste_regninger = faste_regninger if faste_regninger is not None else []
        self.inntekt = inntekt if inntekt is not None else 0
    
    
    def Finn_sist_måned(self):
        
        if self.alle_aar[0].maaner[1] is None:
            return self.alle_aar[1].maaner[11]
        return self.alle_aar[0].maaner[1]
    
    def Finn_faste_regninger(regninger):
        return List
    
    def Finn_inntekt(regninger):
        return float
    
    def Finn_kontont(regninger):
        return int