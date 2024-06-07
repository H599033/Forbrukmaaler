from datetime import date

class Regning:
    def __init__(self, bokført: str, rentedato: str, transaksjonstype: str, beskrivelse: str, melding: str,
                 ut_av_konto: float, inn_på_konto: float, valutasort: str, fra_konto: int, til_konto: int):
        self.bokført = date.strptime(bokført, '%Y-%m-%d') if bokført else None
        self.rentedato = date.strptime(rentedato, '%Y-%m-%d') if rentedato else None
        self.transaksjonstype = transaksjonstype
        self.beskrivelse = beskrivelse
        self.melding = melding
        self.ut_av_konto = float(ut_av_konto) if ut_av_konto else None
        self.inn_på_konto = float(inn_på_konto) if inn_på_konto else None
        self.valutasort = valutasort
        self.fra_konto = int(fra_konto) if fra_konto else None
        self.til_konto = int(til_konto) if til_konto else None

    def __repr__(self):
        return (f"Regning(bokført={self.bokført}, rentedato={self.rentedato}, transaksjonstype='{self.transaksjonstype}', "
                f"beskrivelse='{self.beskrivelse}', melding='{self.melding}', ut_av_konto={self.ut_av_konto}, "
                f"inn_på_konto={self.inn_på_konto}, valutasort='{self.valutasort}', fra_konto={self.fra_konto}, "
                f"til_konto={self.til_konto})")