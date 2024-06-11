from typing import List

from Konto import Konto
from Regning import Regning


class Service:
    
    def lag_konto(self,cvs_fil):
        """ tar inn en Cvs konto fil og lager ett konto objekt. og lagerer alle regninger fra dennn filen
            som regning objekter i konto sin regniner liste
        Args:
            fil (cvs): konto filen

        Returns:
            Konto: kontoen som er laget
        """
        linje =1
        with open(cvs_fil, 'r', newline='') as csvfile:
            # Les alle linjene i filen
            linjer = csvfile.readlines()
            
        t_linje = self.Les_linje(linjer,linje)
        kontonummer = self.finn_konto(t_linje)
        konto = Konto(kontonummer)
        
        while(linje<len(linjer)-1):   
            regning = self.lag_regning(t_linje) 
            konto.regninger.append(regning)
            linje +=1
            t_linje = self.Les_linje(linjer,linje)
        return konto
    
    def lag_regning(self,Transaksjons_linje):
        """ Tar inn en linje fra transaksjonsfilen og lager en Regnings objekt basert på den

        Args:
            Transaksjons_linje (List): liste med verdiene fra en linje 

        Returns:
            Regning: regning laget av en linjen i transaksjonsfilen
        """
        tl = Transaksjons_linje
        regning = Regning(tl[0],tl[1],tl[2],tl[3],tl[4],tl[5],tl[6],tl[7],tl[8],tl[9])            
        return regning
    
    def Fordel_regninger_måner(self,kontoer):
        return List
    
    def Resault_måne(self,regninger):
        return List
    
    def finn_konto(self,linje_2):
        """ Tar inn linje 2 i Transaksjons filen og finner ut hvilken konto som filen er lastet ned fra. 

        Args:
            linje_2 (List): andre linje i Transaksjons filen

        Returns:
            int: kontonummeret til kontoen som transaksjons filen kommer fra
        """
        ut_av_konto = linje_2[5]
        fra_konto = linje_2[8]
        til_konto = linje_2[9]
        if(ut_av_konto != ""):
            return fra_konto
        return til_konto
         
    def Les_linje(self,lines,linje):
        """ Tar inn en linje fra cvs filen og returnerer verdiene som en liste. 

        Args:
            lines: linjen som skal sjekkes
            linje (int): hvilken linje som skal leses
        Returns:
            List: verdiene i linjen som ønskes å bli lest. 
        """
        
        # Sjekk at filen har minst to linjer (overskrift + én datalinje)
        if len(lines) >= 2:
            line= lines[linje].strip()  # .strip() fjerner eventuelle ledende og etterfølgende hvite tegn
            if line:
                # Split linjen på semikolon
                values = line.split(';')
                return values
            return None

