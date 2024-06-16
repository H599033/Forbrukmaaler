from Økonomi import Økonomi
from Konto import Konto
from Regning import Regning
from Service import Service
from Maaned import Maaned


konto_1 = "Test_filer/Transaksjoner-spare.csv"

service = Service()

konto = service.lag_konto(konto_1)

print (konto.alle_aar[1].maaner[0].regninger[0])

