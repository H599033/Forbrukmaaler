from typing import List
from datetime import datetime
from Konto import Konto
from Regning import Regning
from Måned import Måned


class Service:
    
    def lag_konto(self,cvs_fil):
        """ tar inn en Cvs konto fil og lager ett konto objekt. og lagerer alle regninger fra dennn filen
            som regning objekter i konto sin regniner liste
        Args:
            fil (cvs): konto filen
        Returns:
            Konto: kontoen som er laget
        """
      
        with open(cvs_fil, 'r', newline='') as csvfile:
            # Les alle linjene i filen
            linjer = csvfile.readlines()
            
        t_linje = self.Les_linje(linjer,1)
        kontonummer = self.finn_konto(t_linje)
        konto = Konto(kontonummer)
        
        self.legg_til_regninger(konto,t_linje,linjer)
       
        return konto
    
    def legg_til_regninger(self, konto, t_linje,linjer):
        linje =1
        list_år = []
        år = self.finn_år(t_linje)
        mnd = Måned(self.finn_måned(t_linje))
        
        while(linje<len(linjer)-1):
            neste_år = self.finn_år(t_linje)
            
            if år != neste_år:
                konto.år.append(list_år)
                år =neste_år
                list_år = []
            neste_mnd = self.finn_måned(t_linje)
            
            if mnd.måned != neste_mnd:
                list_år.append(mnd)
                mnd = Måned(neste_mnd)
            
            regning = self.lag_regning(t_linje)
            
            mnd.regninger.append(regning)
            linje +=1
            t_linje = self.Les_linje(linjer,linje)
        
    def finn_år(self, t_linje):
        # Sjekk at linjen ikke er tom og har nok elementer
        if t_linje and len(t_linje) > 0:
            try:
                # Hent datoen fra første kolonne
                dato_str = t_linje[0]
                
                # Konverter datoen til et datetime-objekt
                dato = datetime.strptime(dato_str, '%d.%m.%Y')
                
                # Ekstraher året fra datetime-objektet
                år = dato.year
                
                return år
            except ValueError as e:
                print(f"Feil ved konvertering av dato: {e}")
                return None
        else:
            print("Linjen er tom eller har ikke nok elementer.")
            return None
        
    def finn_måned(self, t_linje):
        # Sjekk at linjen ikke er tom og har nok elementer
        if t_linje and len(t_linje) > 0:
            try:
                # Hent datoen fra første kolonne
                dato_str = t_linje[0]
                
                # Konverter datoen til et datetime-objekt
                dato = datetime.strptime(dato_str, '%d.%m.%Y')
                
                # Ekstraher året fra datetime-objektet
                måned = dato.month
                
                return måned
            except ValueError as e:
                print(f"Feil ved konvertering av dato: {e}")
                return None
        else:
            print("Linjen er tom eller har ikke nok elementer.")
            return None
        
    
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

