import sys
import Ice

Ice.loadSlice('generatedIce.ice')
import generatedIce

with Ice.initialize(sys.argv) as communicator:
    anayseurDeRequetes = generatedIce.AnalyseurDeRequetesPrx.checkedCast(communicator.stringToProxy("AnalyseurDeRequetes:default -h localhost -p 10000"))
    commande = anayseurDeRequetes.parserCommande('Jouer Hotel California.')
    print(commande.match, commande.type, commande.sujet)