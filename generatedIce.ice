module generatedIce
{
    class Commande
    {
        string match;
        string type;
        string sujet;
    }

    interface AnalyseurDeRequetes
    {
        Commande parserCommande(string texte);
    }

    sequence<byte> Bytes;

    interface SpeechToText
    {
        // void upload(string id, Bytes dataChunk);
        string getText(string id);
    }
}