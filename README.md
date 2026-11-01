# CI-Beispielprojekt: Bibliothek

Beispielprojekt für die Vorlesung **Continuous Integration** (SWE 1.2).
Ein kleines Python-Paket mit Ausleih-Logik für eine Bibliothek, also dieselbe Domäne wie in der Vorlesung *Analyse- und Entwurfsmodelle*.

Ihre Aufgabe: eine CI-Pipeline mit **Build, Test und Lint** bauen, die bei jedem Push und jedem Pull Request automatisch läuft.

## Was im Projekt steckt

| Datei | Inhalt |
|---|---|
| `src/bibliothek/ausleihe.py` | Ausleihen, Zurückgeben, Mahngebühr berechnen |
| `tests/test_ausleihe.py` | 6 Unit-Tests (pytest) |
| `pyproject.toml` | Paket-Metadaten, Konfiguration für pytest und Ruff |
| `requirements.txt` | Entwicklungs-Werkzeuge, fest gepinnt |

Die drei Pipeline-Stufen entsprechen diesen Befehlen:

| Stufe | Befehl | Was passiert |
|---|---|---|
| Build | `python -m build` | baut das Paket (`.whl` und `.tar.gz` in `dist/`) |
| Test | `pytest` | führt die Unit-Tests aus |
| Lint | `ruff check .` | statische Analyse: Stil, ungenutzte Imports, typische Fehler |

## Voraussetzungen

- GitHub-Account
- Optional zum lokalen Ausprobieren: Python ≥ 3.12

## Schritt für Schritt

### 1. Eigene Kopie anlegen

Oben rechts auf **"Use this template" → "Create a new repository"** klicken.
Das Repository **öffentlich** (Public) anlegen. Dann sind GitHub Actions kostenlos und Branch Protection ist verfügbar.

> Bitte **nicht forken**: In Forks sind GitHub Actions standardmäßig deaktiviert.

### 2. Workflow-Datei anlegen

Im eigenen Repository: **"Add file" → "Create new file"**, als Dateiname eingeben:

```
.github/workflows/ci.yml
```

GitHub legt die Ordner automatisch an.

### 3. Pipeline schreiben

Bauen Sie die Pipeline nach der Vorlage aus der Live-Demo. Sie braucht:

- **Trigger:** `push` und `pull_request` auf `main`
- **Runner:** `ubuntu-latest`
- **Steps:**
  1. Repository auschecken (`actions/checkout`)
  2. Python 3.12 einrichten (`actions/setup-python`), mit `cache: 'pip'`
  3. Abhängigkeiten installieren: `pip install -r requirements.txt`
  4. Build: `python -m build`
  5. Test: `pytest`
  6. Lint: `ruff check .`

### 4. Committen und beobachten

Datei committen (direkt auf `main`). Im Tab **"Actions"** erscheint ein neuer Lauf.
Klicken Sie hinein und prüfen Sie, ob alle Steps grün sind.

### 5. Bonus: Pipeline absichtlich rot machen

Erstellen Sie einen **neuen Branch**, bauen Sie **einen** der folgenden Fehler ein und öffnen Sie einen **Pull Request** gegen `main`.
Beobachten Sie, welcher Step rot wird und welche Steps danach gar nicht mehr laufen.

| Sabotage | Änderung | Erwartung |
|---|---|---|
| **Lint** | in `src/bibliothek/ausleihe.py` eine Zeile `import os` ergänzen | Lint rot (`F401` ungenutzter Import) |
| **Test** | in `ausleihe.py` `GEBUEHR_PRO_TAG_CENT = 50` auf `5` ändern | Test rot, Lint läuft nicht mehr |
| **Build** | in `pyproject.toml` `version = "1.0.0"` auf `"1.0 beta"` ändern | Build rot, Test und Lint laufen nicht mehr |

### 6. Bonus: Merge blockieren

**Settings → Branches → "Add branch ruleset"** (oder "Add classic branch protection rule") für `main`:
**"Require status checks to pass"** aktivieren und den Job `build-test-lint` auswählen.
Jetzt lässt sich ein Pull Request mit roter Pipeline nicht mehr mergen.

## Typische Stolperfallen

| Symptom | Ursache |
|---|---|
| `setup-python` meldet "No file … matched to [**/requirements.txt]" oder pip findet `requirements.txt` nicht | `actions/checkout` fehlt, der Runner hat kein Repository |
| Workflow taucht im Actions-Tab gar nicht auf | Datei liegt nicht genau unter `.github/workflows/` oder endet nicht auf `.yml` |
| YAML-Fehler, bevor ein Job startet | falsche Einrückung (YAML ist einrückungssensitiv, keine Tabs) |
| `ModuleNotFoundError: bibliothek` | Tests aus einem anderen Ordner gestartet; `pytest` im Projekt-Wurzelordner ausführen |
| Test-Step wird übersprungen | ein vorheriger Step (z. B. Build) ist bereits fehlgeschlagen |

## Lokal ausprobieren (optional)

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python -m build
pytest
ruff check .
```
