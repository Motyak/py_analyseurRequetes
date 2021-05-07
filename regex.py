import re
from enum import Enum
from pathlib import Path

# Parse et analyse toutes les commandes valides d'un texte

class Type(Enum):
    LECTURE = 'LECTURE'
    PAUSE = 'PAUSE'
    REPRENDRE = 'REPRENDRE'

class Commande:
    def __init__(self, regexMatch):
        self.typeCmde = Commande._getMatchCommandType(regexMatch)
        self.sujet = regexMatch.group(5)

    @staticmethod
    def parserLesCommandes(texte):
        LECTURE = r'joue(?:s|r)?|lance(?:s|r)?|écouter'
        PAUSE = r'pause|arrêtes?|coupe(?:s|r)?|stop(?:pes|per|pe)?'
        REPRENDRE = r'repren(?:d|nes)|continue(?:s|r)?'
        ACTION = r'.*(?:(?P<LECTURE>{})|(?P<PAUSE>{})|(?P<REPRENDRE>{}))'.format(LECTURE, PAUSE, REPRENDRE)
        SUJET = r'[A-Za-z0-9\ ]*'
        COMMANDE = r'(?P<ACTION>{})\ ?(?P<SUJET>{})\.?'.format(ACTION, SUJET)

        matches =  re.finditer(COMMANDE, texte, re.IGNORECASE)

        return [Commande(match) for match in matches]

    @staticmethod
    def _getMatchCommandType(match):
        if match.group(2) != None:
            return Type.LECTURE
        elif match.group(3) != None:
            return Type.PAUSE
        else:
            return Type.REPRENDRE

    def __str__(self):
        if self.typeCmde == Type.LECTURE:
            return '{}: {}'.format(self.typeCmde.value, self.sujet)
        else:
            return self.typeCmde.value

if __name__ == '__main__':
    texte = Path('inputs.txt').read_text()

    commandes = Commande.parserLesCommandes(texte)

    for commande in commandes:
        print(commande)
