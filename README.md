## Compile source
```console
user@<>$ ./compile.sh
```

## Launch server (Speech to text)
```console
user@<>$ python3 serveurSpeechToText.py
```

## Launch server (analyseur requetes)
```console
user@<>$ python3 serveurAnalyseurRequetes.py
```

## Launch client
```console
user@<>/bin$ java -classpath ../lib/ice-3.7.2.jar:. BackendApi
```