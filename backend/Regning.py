from datetime import date

class Regning:
    def __init__(self, Konto_Fra: int, Konto_Til: int, ut_av_konto: float, inn_på_konto: float, valuta: str,
                 bokført: date, rentedato: date, type: str, beskrivelse: str, Melding: str, fast_regning: bool):
        self.Konto_Fra = Konto_Fra
        self.Konto_Til = Konto_Til
        self.ut_av_konto = ut_av_konto
        self.inn_på_konto = inn_på_konto
        self.valuta = valuta
        self.bokført = bokført
        self.rentedato = rentedato
        self.type = type
        self.beskrivelse = beskrivelse
        self.Melding = Melding
        self.fast_regning = fast_regning
    
    def __repr__(self):
        return (f"Transaksjon(Konto_Fra={self.Konto_Fra}, Konto_Til={self.Konto_Til}, ut_av_konto={self.ut_av_konto}, "
                f"inn_på_konto={self.inn_på_konto}, valuta='{self.valuta}', bokført={self.bokført}, "
                f"rentedato={self.rentedato}, type='{self.type}', beskrivelse='{self.beskrivelse}', "
                f"Melding='{self.Melding}', fast_regning={self.fast_regning})")