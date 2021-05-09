public class BackendApi
{
    private com.zeroc.Ice.Communicator iceCommunicator;
    private generatedIce.AnalyseurDeRequetesPrx analyseurRequetes;

    public static void main(String[] args)
    {
        BackendApi backend = new BackendApi();
        backend.afficherCommande("Jouer Hotel California");
        System.out.println();
        backend.afficherCommande("Arrête la musique.");
        
        backend.destroyIceCommunicator();
    }

    public BackendApi()
    {
        // Initialisation du communicateur Ice
        this.iceCommunicator = com.zeroc.Ice.Util.initialize(new String[]{});

        com.zeroc.Ice.ObjectPrx base = this.iceCommunicator.stringToProxy("AnalyseurDeRequetes:default -p 10000");
        this.analyseurRequetes = generatedIce.AnalyseurDeRequetesPrx.checkedCast(base);
        if(this.analyseurRequetes == null)
            throw new Error("AnalyseurDeRequetes: Invalid proxy");
    }

    public void destroyIceCommunicator()
    {
        this.iceCommunicator.destroy();
    }

    public void afficherCommande(String texte)
    {
        generatedIce.Commande cmde = this.analyseurRequetes.parserCommande(texte);
        
        System.out.print(cmde.match + "\n  \'-> " + cmde.type);
        if(cmde.type == "LECTURE")
            System.out.println(": " + cmde.sujet);
        System.out.println();
    }
}