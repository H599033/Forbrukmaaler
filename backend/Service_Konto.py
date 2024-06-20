from typing import List
from datetime import datetime
from Konto import Konto
from Regning import Regning
from Maaned import Maaned
from Aar import Aar

class Service_Konto:
    
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
        """ legger til regninger i riktig måned og år for en konto.

        Args:
            konto (Konto objekt): Konto objektet
            t_linje (list): verdiene til en linje i cvs tranaksjons filen
            linjer (int): linjen som blir lest av hos cvs filen.
        """
        linje =1
        år = Aar(self.finn_år(t_linje))
        mnd = Maaned(self.finn_måned(t_linje))
        
        while(linje<len(linjer)-1):
            neste_år = self.finn_år(t_linje)
            if år.Aar != neste_år:
                print(" inne i år")
                konto.alle_aar.append(år)
                år = Aar(neste_år)
            
            regning = self.lag_regning(t_linje)
            mnd.regninger.append(regning)
            if regning.type =="Lønn":
                print("inne i mnd")
                år.maaner.append(mnd)
                print(len(år.maaner))
                mnd = Maaned(self.finn_måned(t_linje))
            
            linje +=1
            t_linje = self.Les_linje(linjer,linje)
        
    def finn_år(self, t_linje):
        """finner hvilket år som linjen er basert på
        Args:
            t:linje(list) linjen som skal sjekkes
        Returns:
            datetime: året som blir funnet
        """
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
        """finner hvilken måned som linjen er basert på
        Args:
            t:linje(list) linjen som skal sjekkes
        Returns:
            datetime: måned som blir funnet
        """
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
    
    def første_inntekt_mnd(self, t_linje):
        
        
        return 
    
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

