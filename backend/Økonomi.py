from typing import List
from datetime import date
from Konto import Konto
from Regning import Regning
import pandas as pd

class Økonomi:
    def __init__(self, kontoer: List[Konto], fast_utgift: float, inntekt: float,
                 regninger_måner: List[List[Regning]], resultat_måner: List[List[float]],
                 sparemål_mnd: int, sparemål_tot: int, sparemål_dato: date, spart: float):
        self.kontoer = kontoer
        self.fast_utgift = fast_utgift
        self.inntekt = inntekt
        self.regninger_måner = regninger_måner
        self.resultat_måner = resultat_måner
        self.sparemål_mnd = sparemål_mnd
        self.sparemål_tot = sparemål_tot
        self.sparemål_dato = sparemål_dato
        self.spart = spart
    
    
    def lag_konto(fil):
        
        
        
        return list 
    
    def lag_regning(Transaksjons_linje):
        return list
    
    def Fordel_regninger_måner(kontoer):
        return List
    
    def Resault_måne(regninger):
        return List
    
    def finn_konto(linje_2):
        """ Tar inn linje 2 i Transaksjons filen og finner ut hvilken konto som filen er lastet ned fra. 

        Args:
            linje_2 (List): andre linje i Transaksjons filen

        Returns:
            int: kontonummeret til kontoen som transaksjons filen kommer fra
        """
        ut_av_konto = linje_2[6]
        fra_konto = linje_2[9]
        til_konto = linje_2[10]
        if(ut_av_konto != ""):
            return fra_konto
        return til_konto
        
    
    def Les_linje(fil, linje):
        """ Leser er linje i transaksjons listen og returnerer den som en lsite. 

        Args:
            fil (fil.cvs): Transaksjons fil
            linje (int): hvilken linje som skal leses

        Returns:
            List: verdiene i linjen som ønskes å bli lest. 
        """
        with open('transaksjoner.csv', 'r', newline='') as csvfile:
            # Les alle linjene i filen
            lines = csvfile.readlines()

            # Sjekk at filen har minst to linjer (overskrift + én datalinje)
            if len(lines) >= 2:
                second_line = lines[linje].strip()  # .strip() fjerner eventuelle ledende og etterfølgende hvite tegn

                 # Split linjen på semikolon
                values = second_line.split(';')
                return values
