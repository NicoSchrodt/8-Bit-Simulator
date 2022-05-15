# 8-Bit-Simulator

## Installation:
Um den Simulator zu verwenden muss entweder Python 3.10 auf dem Rechner installiert sein, sowie das PyQt6 Package oder es muss (auf Windows) die gegebene Exe-Datei verwendet werden.
Die Handhabung der Exe-Datei funktioniert dabei wie folgt:

- Auswählen der gewünschten Exe-Datei
- Verschieben der Exe-Datei in das Basisverzeichnis des Projekts
- Ausführen der Exe
- Dabei ist wichtig, dass der "ui"-Ordner sowie dessen Inhalt an derselben Stelle ist (Code/ui), die restlichen Dateien werden für die Exe nicht benötigt

Diese Art das Programm auszuführen ist notwendig aufgrund von Pfadproblemen für die UI-Dateien der einzelnen Simulationsfenster.

UPDATE:
Exe-Dateien ab Commit "aa301f019aefec600f99d5c6997297e74bb93b0f" können ohne die oberen Bedingungen ausgeführt werden.