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
}