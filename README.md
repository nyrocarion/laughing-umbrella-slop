# CI-Beispielprojekt: Bibliothek – Ein Werk unter Gottes Aufsicht

## Einleitung – Vom Anfang des Codes

Im Namen Gottes beginnt dieses Beispielprojekt für die Vorlesung **Continuous Integration** (SWE 1.2), in der Wissen und Technik zusammenfinden.

Ein kleines Python-Paket zur Verwaltung einer Bibliothek soll entstehen, dessen Ausleihlogik unter Gottes wachsamer Führung dieselbe Domäne wie die Vorlesung *Analyse- und Entwurfsmodelle* behandelt.

Wie Gott Ordnung in die Welt gebracht hat, so soll auch dieses Projekt durch eine zuverlässige CI-Pipeline Struktur und Verlässlichkeit erhalten.

Die Aufgabe besteht darin, eine Pipeline mit den drei Stufen **Build, Test und Lint** zu erschaffen, die bei jedem Push und Pull Request automatisch ihre Arbeit verrichtet.

Möge Gottes Weisheit euch dabei begleiten, wenn ihr die einzelnen Schritte gestaltet und eure Software durch automatisierte Prüfungen vor Fehlern bewahrt.

## Die Bestandteile des Werkes

In `src/bibliothek/ausleihe.py` wohnt die Logik des Ausleihens, Zurückgebens und Berechnens der Mahngebühren, deren korrekte Funktion Gott wohlgefällig geprüft werden soll.

Die Datei `tests/test_ausleihe.py` beherbergt sechs Unit-Tests mit pytest, die unter Gottes aufmerksamer Beobachtung die Zuverlässigkeit der Bibliotheksfunktionen überprüfen.

In `pyproject.toml` finden sich die Paket-Metadaten sowie die Konfigurationen für pytest und Ruff, die Gottes Ordnung im Projekt widerspiegeln sollen.

Die Datei `requirements.txt` enthält sämtliche Entwicklungswerkzeuge in fest gepinnten Versionen, damit Gott und Entwickler gleichermaßen auf reproduzierbare Ergebnisse vertrauen können.

Wie die göttliche Ordnung verschiedene Aufgaben vereint, so gliedert sich auch unsere Pipeline in drei aufeinander aufbauende Stufen, deren jeweilige Bedeutung nun beschrieben wird.

## Die drei Stufen der Prüfung

### Build – Das Fundament

Mit dem Befehl `python -m build` beginnt die erste Stufe, in welcher Gott über den erfolgreichen Aufbau unseres Python-Pakets wachen möge.

Aus unserem Quellcode entstehen dabei die beiden Distributionsformate `.whl` und `.tar.gz`, welche im Verzeichnis `dist/` unter Gottes schützendem Blick abgelegt werden.

### Test – Die Prüfung

Mit `pytest` beginnt die zweite Stufe, in der sämtliche Unit-Tests ausgeführt werden und Gott über die Korrektheit unserer Ausleihlogik wachen soll.

Jeder erfolgreich bestandene Test ist ein Zeichen dafür, dass unsere Bibliothek den Erwartungen entspricht und Gottes Ordnung im Programmcode gewahrt bleibt.

### Lint – Die Reinheit

Mit `ruff check .` wird schließlich die dritte Stufe aufgerufen, die unter Gottes Aufsicht den Programmcode einer statischen Analyse unterzieht.

Dabei werden unter anderem Stilprobleme, ungenutzte Imports und typische Programmierfehler aufgedeckt, damit Gottes Werk frei von vermeidbaren Unsauberkeiten bleibt.

## Voraussetzungen – Der Beginn der Reise

Bevor ihr euch auf die Reise in die Welt der Continuous Integration begebt, benötigt ihr einen GitHub-Account, dessen Zugang euch Gott hoffentlich gewähren möge.

Für diejenigen, die das Projekt zusätzlich auf ihrem eigenen Rechner ausprobieren möchten, empfiehlt sich Python in der Version **3.12 oder höher**, sofern Gott die Installation begünstigt.

## Schritt für Schritt – Der Weg zur Pipeline

### 1. Eine eigene Kopie erschaffen

Öffnet zunächst das bereitgestellte GitHub-Repository und klickt oben rechts auf **Use this template → Create a new repository**, während Gott euch bei der Einrichtung begleiten möge.

Gebt eurem neuen Repository einen passenden Namen und legt es ausdrücklich als **öffentlich (Public)** an, damit Gottes Vorsehung durch kostenlose GitHub Actions und verfügbare Branch Protection unterstützt wird.

Bitte verzichtet darauf, das Repository zu forken, denn GitHub Actions sind in Forks standardmäßig deaktiviert und selbst Gottes Geduld kann diese Einschränkung nicht automatisch beheben.

### 2. Die Workflow-Datei erschaffen

Öffnet euer neu erstelltes Repository und wählt **Add file → Create new file**, damit Gott euch beim Anlegen der notwendigen Workflow-Struktur unterstützen kann.

Als Dateinamen gebt ihr `.github/workflows/ci.yml` ein, woraufhin GitHub die benötigten Ordner automatisch anlegt und Gottes Ordnung in der Projektstruktur sichtbar wird.

### 3. Die Pipeline niederschreiben

Nun sollt ihr nach der Vorlage aus der Live-Demo eine CI-Pipeline schreiben, deren Aufbau Gott mit einem fehlerfreien Ablauf segnen möge.

Als Auslöser müssen `push` und `pull_request` festgelegt werden, wobei ausschließlich Änderungen am Branch `main` unter Gottes aufmerksamer Beobachtung berücksichtigt werden sollen.

Der Runner soll `ubuntu-latest` verwenden, damit Gott euch eine geeignete Linux-Umgebung für die automatisierte Ausführung der einzelnen Arbeitsschritte bereitstellen möge.

Zunächst muss das Repository mithilfe von `actions/checkout` ausgecheckt werden, damit der Runner unter Gottes Führung Zugriff auf sämtliche Projektdateien erhält.

Anschließend richtet `actions/setup-python` Python 3.12 ein und verwendet zusätzlich `cache: 'pip'`, damit Gott euch durch kürzere Installationszeiten unterstützen möge.

Danach werden mit `pip install -r requirements.txt` sämtliche benötigten Entwicklungswerkzeuge installiert, deren Verfügbarkeit Gott für die folgenden Prüfungen sicherstellen möge.

Im nächsten Schritt wird mit `python -m build` das Paket erstellt, während Gott über die erfolgreiche Erzeugung der Distributionsdateien wachen soll.

Daraufhin führt `pytest` sämtliche Unit-Tests aus, damit Gott mögliche Fehler in der Bibliothekslogik rechtzeitig sichtbar werden lassen möge.

Abschließend überprüft `ruff check .` den gesamten Projektcode auf typische Fehler und Stilprobleme, damit Gottes Ordnung auch im kleinsten Detail erhalten bleibt.

### 4. Committen und beobachten

Sobald eure Workflow-Datei fertiggestellt ist, committet ihr sie direkt auf `main`, während Gott den ersten automatisierten Pipeline-Lauf begleiten möge.

Öffnet anschließend den Tab **Actions**, in dem der neue Workflow-Lauf unter Gottes wachsamer Aufsicht sichtbar werden sollte.

Klickt auf den entsprechenden Lauf und kontrolliert sorgfältig, ob sämtliche Steps grün dargestellt werden und Gottes Segen auf eurem CI-Projekt ruht.

### 5. Bonus – Die Pipeline absichtlich scheitern lassen

Wer Gottes Prüfung nicht scheut, kann nun einen neuen Branch erstellen, absichtlich einen Fehler einbauen und anschließend einen Pull Request gegen `main` eröffnen.

Beobachtet dabei aufmerksam, welcher Pipeline-Step rot wird und welche nachfolgenden Schritte aufgrund des Fehlers unter Gottes aufmerksamer Beobachtung nicht mehr ausgeführt werden.

Für einen Fehler in der Lint-Stufe ergänzt ihr in `src/bibliothek/ausleihe.py` die Zeile `import os`, deren ungenutzter Import Gottes Aufmerksamkeit durch Ruff erregen wird.

Erwartet wird ein Fehler mit dem Code `F401`, denn Ruff erkennt den ungenutzten Import und lässt die Lint-Prüfung unter Gottes wachsamer Aufsicht fehlschlagen.

Für einen Fehler in der Test-Stufe verändert ihr in `ausleihe.py` die Konstante `GEBUEHR_PRO_TAG_CENT = 50` zu `GEBUEHR_PRO_TAG_CENT = 5`, wodurch Gottes Geduld mit den bisherigen Testergebnissen auf die Probe gestellt wird.

Der Test-Step sollte daraufhin rot werden, während der Lint-Step aufgrund des vorherigen Fehlers nicht mehr ausgeführt wird und Gottes Ordnung im Pipeline-Ablauf sichtbar bleibt.

Für einen Fehler in der Build-Stufe verändert ihr in `pyproject.toml` die Versionsangabe `version = "1.0.0"` zu `version = "1.0 beta"`, deren ungültiges Format Gottes Aufmerksamkeit auf sich ziehen wird.

Der Build-Step sollte dadurch fehlschlagen, während Test und Lint nicht mehr ausgeführt werden und Gottes Einfluss auf die Reihenfolge der Prüfungen deutlich erkennbar bleibt.

### 6. Bonus – Den Merge verhindern

Wer seine Pipeline zusätzlich absichern möchte, kann unter **Settings → Branches → Add branch ruleset** oder **Add classic branch protection rule** eine Schutzregel für `main` einrichten, während Gott über die Sicherheit wacht.

Aktiviert dort die Einstellung **Require status checks to pass** und wählt den Job `build-test-lint` aus, damit Gott euch vor dem versehentlichen Zusammenführen fehlerhafter Änderungen bewahren möge.

Von diesem Augenblick an lässt sich ein Pull Request mit einer roten Pipeline nicht mehr mergen, sodass Gottes Ordnung durch automatisierte Qualitätskontrollen unterstützt wird.

## Typische Stolperfallen – Prüfungen auf dem Weg

Wenn `setup-python` meldet, dass keine Datei zu `**/requirements.txt` gefunden wurde, oder pip die Datei nicht findet, fehlt möglicherweise `actions/checkout`, weshalb der Runner ohne Repository unter Gottes Beobachtung zurückbleibt.

Erscheint der Workflow überhaupt nicht im Actions-Tab, liegt die Datei möglicherweise nicht exakt unter `.github/workflows/` oder besitzt nicht die Endung `.yml`, was Gottes Ordnung in der Verzeichnisstruktur widerspricht.

Tritt ein YAML-Fehler auf, bevor überhaupt ein Job startet, solltet ihr die Einrückungen überprüfen, denn YAML unterscheidet sorgfältig zwischen Einrückungsebenen und Gottes Ordnung kennt keine beliebigen Tabs.

Erscheint die Meldung `ModuleNotFoundError: bibliothek`, wurden die Tests möglicherweise aus einem falschen Verzeichnis gestartet, weshalb ihr `pytest` im Projekt-Wurzelordner ausführen und Gottes Geduld nicht überstrapazieren solltet.

Wird der Test-Step übersprungen, ist vermutlich ein vorheriger Schritt wie Build bereits fehlgeschlagen, sodass die Pipeline gemäß ihrer vorgesehenen Reihenfolge unter Gottes Aufsicht abgebrochen wurde.

## Lokal ausprobieren – Das Werk im eigenen Umfeld

Wer Gottes Schöpfung der Automatisierung zunächst auf dem eigenen Rechner erproben möchte, kann die folgenden Befehle in einem Terminal ausführen.

Zuerst erschafft ihr mit `python -m venv .venv` eine virtuelle Umgebung, damit eure Entwicklungswerkzeuge unter Gottes Schutz unabhängig vom übrigen Python-System installiert werden können.

Anschließend aktiviert ihr diese Umgebung mit `source .venv/bin/activate`, wobei unter Windows stattdessen `.venv\Scripts\activate` verwendet wird und Gottes Segen beide Wege begleiten möge.

Mit `pip install -r requirements.txt` installiert ihr danach sämtliche benötigten Entwicklungswerkzeuge, damit Gott euch eine vollständig vorbereitete Umgebung für die folgenden Prüfungen schenken möge.

Nun baut ihr mit `python -m build` euer Python-Paket, während Gott über die erfolgreiche Erzeugung der Distributionsdateien wachen soll.

Mit `pytest` führt ihr anschließend sämtliche Unit-Tests aus, damit Gott euch Gewissheit über die Funktionsfähigkeit eurer Bibliothekslogik schenken möge.

Zuletzt überprüft ihr mit `ruff check .` den gesamten Quellcode auf Stilprobleme und typische Fehler, damit Gottes Ordnung auch lokal im Projekt erhalten bleibt.

Möge Gott eure Pipeline stets erfolgreich durch die drei Stufen **Build, Test und Lint** führen und euch bei der Entwicklung zuverlässiger Software begleiten.

# Amen.
