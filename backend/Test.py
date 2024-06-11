from Økonomi import Økonomi
from Konto import Konto
from Regning import Regning
from Service import Service

konto_1 = "Test_filer/Transaksjoner-spare.csv"

service = Service()

konto = service.lag_konto(konto_1)

print (konto.konto_nr)
print(len(konto.regninger))
print(konto.regninger[len(konto.regninger)-1])