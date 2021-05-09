from regex import Type, Commande

import signal
import sys
import Ice

Ice.loadSlice('generatedIce.ice')
import generatedIce

class AnalyseurDeRequetes(generatedIce.AnalyseurDeRequetes):
    def parserCommande(self, texte, context=None):
        commandes = Commande.parserLesCommandes(texte)
        if len(commandes) == 0:
            return None
        else:
            cmde = commandes[0]
            return generatedIce.Commande(cmde.match, cmde.typeCmde.value, cmde.sujet)

if __name__ == "__main__":
    with Ice.initialize(sys.argv) as communicator:
        signal.signal(signal.SIGINT, lambda signum, frame: communicator.shutdown())
        adapter = communicator.createObjectAdapterWithEndpoints("AnalyseurDeRequetesAdapter", "default -h localhost -p 10000")
        adapter.add(AnalyseurDeRequetes(), Ice.stringToIdentity("AnalyseurDeRequetes"))
        adapter.activate()
        communicator.waitForShutdown()