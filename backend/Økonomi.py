from datetime import date
from typing import List
from Konto import Konto
from Regning import Regning
import pandas as pd

class Økonomi:
    def __init__(self, kontoer: List[Konto], fast_utgift: float, inntekt: float, inntekt_dato: date,
                 regninger_måner: List[List[Regning]], resultat_måner: List[List[float]],
                 sparemål_mnd: int, sparemål_tot: int, sparemål_dato: date, spart: float):
        self.kontoer = kontoer if kontoer else []
        self.fast_utgift = fast_utgift if fast_utgift else None
        self.inntekt = inntekt if inntekt else None
        self.inntekt_dato = inntekt_dato if inntekt_dato else None
        self.regninger_måner = regninger_måner if regninger_måner else []
        self.resultat_måner = resultat_måner if resultat_måner else []
        self.sparemål_mnd = sparemål_mnd if sparemål_mnd else None
        self.sparemål_tot = sparemål_tot if sparemål_tot else None
        self.sparemål_dato = sparemål_dato if sparemål_dato else None
        self.spart = spart
    