# Advanced Software Engineering

Florian Babel, Daniel Schomburg

## Übersicht

Für den Programmentwurf haben wir ein Spiel mit Python entwickelt. Dafür wurden
die Python Bibliothek _Pygame_ benutzt, um einige Funktionen zur Ein- und
Ausgabe und der Interaktion zwischen Objekten zu vereinfachen.

## Clean Architecture

### Schichten

Wir haben die Schichten Domain, Application, Adapter und Plugin umgesetzt. In
der Domain sind alle Klassen enthalten, die das Spiel selbst ausmachen. Das sind
die GameBlocks inklusive einiger abgeleiteten Klassen und das Level. In der
Application sind alle Klassen enthalten, die den Ablauf eines Spiels regeln und
Interaktionen zwischen verschiedenen Objekten regeln. Der Adapter enthält
Klassen, die ein Datenmodel oder ein bestimmtes Funktionsset in ein anderes
übersetzt. Der BlocksGenerator wandelt ein Array aus Bildpunkten in ein Array
aus GameBlocks um, die im Spiel genutzt werden. PygameGameEngine ist der einzige
Kontaktpunkt zu Pygame. Dort werden die benötigten Funktionen von Pygame
abstrahiert, sodass diese ohne Abhängigkeit überall genutzt werden können. Im
Plugin sind Klassen definiert, die leicht austauschbar sein sollen. So ist es
sehr einfach einen anderen EventHandler oder einen anderen extractor
hinzuzufügen. Dabei haben wir darauf geachtet, dass die Abhängigkeiten immer vom
Core zur Application zu Plugin eingehalten werden, um dem Model zu entsprechen.

## Entwurfsmuster

Wir haben versuche mehrere Entwurfsmuster umzusetzen. Zum Beispiel haben wir als
Eventhandler einen Observer eingesetzt. Dieser ermöglicht die Interaktion
zwischen klassen und ein dynamisches Verhalten auf ein Event. Die Klasse "
EventHandler" ist der Observer die als innere Klasse "Events" hat. Sie hat die
Methoden add und remove um die Events zu verwalten. Um ein Event auszulösen wird
die Instanz des Eventhandlers einfach mit dem event und eventuelle Parameter
aufgerufen. Dann werden alle Funktionen, die für das Event registriert wurden,
ausgeführt und die Parameter weitergeleitet.

## Programming Principles

## Tests

In der Application wurden 12 Unit-Tests für zwei Klassen umgesetzt. Für die
CollisionDetection sind 8 Tests vorhanden, um Kollisionen in alle vier
Richtungen zu testen. Dafür gibt es für jede Richtung zwei Tests, da die
detection mit und ohne border ausgeführt werden kann. Da das gewünschte
Verhalten nicht Intuitiv zu programmieren ist, ist ein Test hier besonders
wichtig, um das korrekte Verhalten sicherzustellen. An dieser Stelle hat der
Test auch einmal einen Fehler erkannt. Während der Implementation der
GameEngine, wurden Variablen durch einen Tippfehler falsch übergeben. Dadurch
entstand ein Fehler, der beim Spielen nicht sofort offensichtlich war. Der Test
hat aber angeschlagen, sodass der Fehler schnell gefunden und beseitigt werden
konnte.

## Refactoring