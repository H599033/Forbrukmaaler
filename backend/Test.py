from Økonomi import Økonomi
from Konto import Konto
from Regning import Regning
from Service_Konto import Service_Konto
from Maaned import Maaned


konto_1 = "Test_filer/Transaksjoner-bruks.csv"

sk = Service_Konto()

konto = sk.lag_konto(konto_1)
lengde = len(konto.alle_aar[1].maaner[0].regninger)-1
print(len(konto.alle_aar))
print (konto.alle_aar[2].maaner[1].regninger[0].bokført)
print (konto.alle_aar[2].maaner[1].regninger[lengde].bokført)

