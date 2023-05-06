# Advanced Software Engineering

Florian Babel, Daniel Schomburg

## Übersicht

Für den Programmentwurf haben wir ein Spiel mit Python entwickelt. Dafür wurden die Python Bibliothek
_Pygame_ benutzt, um einige Funktionen zur Ein- und Ausgabe und der Interaktion zwischen Objekten zu vereinfachen.

## Clean Architecture

### Schichten

Wir haben die Schichten Domain, Application, Adapter und Plugin umgesetzt. Alle Abhängigkeiten verlaufen von außen nach innen.

#### Domain

In der Domain sind alle Klassen enthalten, die das Spiel selbst ausmachen, da elementare Bestandteile implementiert werden. In der Domain findet sich zunächst das Level, das während des Spiels die Blöcke verwaltet und bei der Initialisierung verschiedenen Events zuordnet. Des weiteren befinden sich dort die GameBlocks sowie die daraus abgeleiteten Klassen. Als letztes sind hier zwei Interfaces zu finden, die in der Application implementiert werden.

#### Application

In der Application sind alle Klassen enthalten, die den Ablauf eines Spiels regeln und Interaktionen zwischen verschiedenen Objekten regeln. Zunächst der GameManager, der den Übergang zwischen den Levels und das Menu verwaltet. Als nächstes der GameLoop, der dauerhaft läuft und den User Input empfängt und fürs Spiel relevante Events auslöst. Das Interface der GameEngine befindet sich hier und wird im Plugin implementiert. Die restlichen Klassen sind jeweils für die Berechnung der Physik und die Grafikausgabe zuständig.

#### Adapter

Der Adapter enthält Klassen, die ein Datenmodel oder ein bestimmtes Funktionsset in ein anderes übersetzt. Der BlocksGenerator wandelt ein Array aus Bildpunkten in ein Array aus GameBlocks um, die im Spiel genutzt werden. PygameGameEngine ist der einzige Kontaktpunkt zu Pygame. Es implementiert das gameEngine Interface aus der Application. Hier werden die benötigten Funktionen von Pygame abstrahiert, sodass diese ohne Abhängigkeit überall genutzt werden können, indem auf das Interface zugegriffen wird.

#### Plugin

Im Plugin sind Klassen definiert, die leicht austauschbar sein sollen. So ist es sehr einfach einen anderen EventHandler oder einen anderen extractor hinzuzufügen. Dabei haben wir darauf geachtet, dass die Abhängigkeiten immer vom Core zur Application zu Plugin eingehalten werden, um dem Model zu entsprechen.

## Entwurfsmuster

Wir haben als Entwurfsmuster den Observer umgesetzt. Dafür wurde ein Event Handler implementiert. Dieser ermöglicht die Interaktion zwischen mehreren Klassen und dynamisches Verhalten auf Events. Die Klasse _EventHandler_ hat als innere Klasse _Events_. Für die Verwaltung der Events gibt es die Methoden _add_ und _remove_. Beim Hinzufügen eines Events, wird die übergebenen Methode in der entsprechenden Eventliste gespeichert. Um ein Event auszulösen wird die Instanz des Eventhandlers mit dem Event und eventuelle Parameter aufgerufen. Dann werden alle Funktionen in der Eventliste ausgeführt und die Parameter weitergeleitet. Dies entspricht dem klassichen Beobachter Entwurfsmuster.

## Programming Principles

### SOLID

#### S - Single Responsibility

Rund um die Physik Berechnung erfüllen die Klassen das Single Responsibility Prinzip, indem jede Methode mit einer eigenen Aufgabe in eine eigene Klasse ausgelagert ist. Zunächst wird der
_PhysicsEngine_ die Geschwindigkeit der Blöcke ausgerechnet. An dieser Stelle gibt es noch zwei Methoden, da die Berechnung der Geschwindigkeit des
_Player_ Tastatureingaben berücksichtigen muss. Die Berechnung des
_Enemies_ braucht aber eine eigene Methode, da sich dieser auch ohne Eingaben Bewegen muss. Während dieser Berechnung wird abgefragt, ob der entsprechende Block Kollisionen mit anderen Blöcken hat und sich somit nicht weiter in diese Richtung bewegen kann. Die Kollisionserkennung ist in einer eigenen Klasse implementiert und wird von beiden Methoden genutzt. Die Aufgabe ist nur aus einem Subjekt und einer Liste aus Blöcken alle Kollisionen zurückzugeben. Sobald die Geschwindigkeit berechnet wurde müssen die Blöcke bewegt werden. Da beim Bewegen noch Kollisionen auftreten können, braucht es eine extra Methode, die die Blöcke um ihre Geschwindigkeit bewegen, aber im Falle einer Kollision dahin den Block nicht weiter bewegen.

#### O - Open/Closed

Die Arten von Blöcken sind leicht erweiterbar, ohne bestehende Blockarten zu ändern. Dafür gibt es zunächst ein Enum, in dem alle Block Arten von Blöcken definiert werden. Wird eine neue Art von Block implementiert, muss in das Enum ein neuer Eintrag erfolgen. Während der Generation der Karte in
_BlocksGenerator_ müssen dem Block die Basis Eigenschaften zugeordnet werden, indem ein weiteres if hinzugefügt wird. Falls der Block nur passive Eigenschaften hat reicht es in den aktiven Blöcken die Reaktionen auf einen solchen Block zu implementieren. Falls der Block eigene Funktion haben soll, kann die Vererbungskette von
_GameBlock_ an einer beliebigen Stelle genutzt werden, um dem neuen Block aktiv zu machen. An dieser Stelle kann der Block Events empfangen und darauf reagieren. Falls neue Events gebraucht werden, kann auch dort einfach eine neue Eventart hinzugefügt werden und an der benötigten Stelle genutzt werden.

#### L - Liskov Substitution

GameEngine

#### I - Interface Segregation

Innerhalb der GameBlock Vererbungskette existiert das Interface
_MovingGameBlock_, das von GameBlock erbt. Dabei wird zur übernommenen Funktionalität die Möglichkeit der Bewegung und dem Reagieren auf andere Blöcke hinzugefügt. Diese Funktionalität wird für alle passiven Blöcke nicht gebraucht.

#### D - Dependency Inversion

An vielen verschiedenen Stellen wird die Dependency Inversion genutzt. Als Beispiel soll hier die Game Engine dienen. Zunächst existiert das
_GameEngine_ Interface. Die Funktionen werden von _PygameGameEngine_ implementiert. In der _main_ wird eine
_PygameGameEngine_ definiert und an den _GameLoop_ und
_GameManager_ übergeben. Dort kann diese Klasse wie eine GameEngine genutzt werden. In Python ist es nicht nötig die Art der Klasse anzugeben, sodass die GameEngine hier auch weggelassen hätte können. Da die GameEngine, aber die Methoden definiert und die
_PygameGameEngine_ alle Methoden implementieren muss, wird erzwungen, dass eine abgeleitete Klasse alle Funktionalitäten übernimmt.

## Tests

In der Application wurden 12 Unit-Tests für zwei Klassen umgesetzt. Für die CollisionDetection sind 8 Tests vorhanden, um Kollisionen in alle vier Richtungen zu testen. Dafür gibt es für jede Richtung zwei Tests, da die detection mit und ohne border ausgeführt werden kann. Da das gewünschte Verhalten nicht Intuitiv zu programmieren ist, ist ein Test hier besonders wichtig, um das korrekte Verhalten sicherzustellen. An dieser Stelle hat der Test auch einmal einen Fehler erkannt. Während der Implementation der GameEngine, wurden Variablen durch einen Tippfehler falsch übergeben. Dadurch
entstand ein Fehler, der beim Spielen nicht sofort offensichtlich war. Der Test
hat aber angeschlagen, sodass der Fehler schnell gefunden und beseitigt werden
konnte.

## Refactoring