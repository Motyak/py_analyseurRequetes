public class BackendApi
{
    private com.zeroc.Ice.Communicator iceCommunicator;
    private generatedIce.SpeechToTextPrx speechToText;
    private generatedIce.AnalyseurDeRequetesPrx analyseurRequetes;

    public static void main(String[] args)
    {
        BackendApi backend = new BackendApi();

        // retournera 'Joue Hotel California'
        String texte = backend.speechToText(null);

        backend.afficherCommande(texte);
        
        backend.destroyIceCommunicator();
    }

    public BackendApi()
    {
        // Initialisation du communicateur Ice
        this.iceCommunicator = com.zeroc.Ice.Util.initialize(new String[]{});

        // Init proxy speech to text
        com.zeroc.Ice.ObjectPrx base = this.iceCommunicator.stringToProxy("SpeechToText:default -p 10001");
        this.speechToText = generatedIce.SpeechToTextPrx.checkedCast(base);
        if(this.speechToText == null)
            throw new Error("SpeechToText: Invalid proxy");

        // Init proxy analyseur de requetes
        base = this.iceCommunicator.stringToProxy("AnalyseurDeRequetes:default -p 10000");
        this.analyseurRequetes = generatedIce.AnalyseurDeRequetesPrx.checkedCast(base);
        if(this.analyseurRequetes == null)
            throw new Error("AnalyseurDeRequetes: Invalid proxy");
    }

    public void destroyIceCommunicator()
    {
        this.iceCommunicator.destroy();
    }

    public String speechToText(byte[] audio)
    {
        // // Generate random string id
        // String id = "xxx";

        // // upload every 64KB chunk
        // int nbOfChunks = audio.length / 65536 + 1;
        // int indexStartChunk = 0;
        // for(int i = 1 ; i < nbOfChunks ; ++i)
        // {
        //     byte[] chunk = java.util.Arrays.copyOfRange(audio, indexStartChunk, indexStartChunk + 65536);
        //     this.speechToText.upload(id, chunk);
        //     indexStartChunk += 65536;
        // }
        // byte[] chunk = java.util.Arrays.copyOfRange(audio, indexStartChunk, audio.length);
        // this.speechToText.upload(id, chunk);

        // retournera 'Joue Hotel California'
        return this.speechToText.getText("id");
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