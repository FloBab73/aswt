# Advanced Software Engineering

Florian Babel, Daniel Schomburg

## Übersicht

Für den Programmentwurf haben wir ein Spiel mit Python entwickelt. Dafür wurden die Python Bibliothek _Pygame_ benutzt,
um einige Funktionen zur Ein und Ausgabe und der Interaktion zwischen Objekten zu Vereinfachen.

## Clean Architecture

### Schichten

Wir haben die Schichten Core, Adapter und Plugin umgesetzt.
Im Core sind alle Klassen enthalten die für die Spielmechaniken wichtig sind.
Bei Adapter ist nur ein klasse, die für die Blockerstellung verwendet wird.
Plugin behinhaltet alles was nötig ist um die Spielemechaniken mit der Ein- und Ausgabe zu verbinden.
Dabei haben wir darauf geachte, dass die Abhäigkeiten immer vom Core zur Aplication zu Plugin eingehalten werden um dem Model zu ensprechen.

## Entwurfsmuster

Wir haben versuche mehere Entwurfsmuster umzusetzten. Zum Beispiel haben wir als Eventhandler einen Observer eingesetzt. Dieser ermöglicht die interaktion zwischen klassen und ein Dynamisches Verhalten auf ein Event. Die Klasse "EventHandler" ist der Observer die als innere Klasse "Events" hat. Sie hat die Methoden add und remove um die Events zu verwalten. Um ein Event auzulösen wird die Instanz des Eventhandlers einfach mit dem event und eventuelle Parameter aufgerufen.
Dann werden alle Funktionen die für das Event regestriert wurden, ausgefürht und die Parameter weitergeleitet. 

## Programming Principles

## Tests

## Refactoring