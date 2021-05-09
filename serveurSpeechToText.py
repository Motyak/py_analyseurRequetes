import signal
import sys
import Ice

Ice.loadSlice('generatedIce.ice')
import generatedIce

class SpeechToText(generatedIce.SpeechToText):
    def getText(self, texte, context=None):
        return 'Joue Hotel California'

if __name__ == "__main__":
    with Ice.initialize(sys.argv) as communicator:
        signal.signal(signal.SIGINT, lambda signum, frame: communicator.shutdown())
        adapter = communicator.createObjectAdapterWithEndpoints("SpeechToTextAdapter", "default -h localhost -p 10001")
        adapter.add(SpeechToText(), Ice.stringToIdentity("SpeechToText"))
        adapter.activate()
        communicator.waitForShutdown()