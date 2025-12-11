# CLIPTest

Dieses Projekt ist ein kleines Playground-Repo, um mit CLIP (Contrastive Language–Image Pretraining) in Python zu experimentieren.  
Dieses README erklärt **Schritt für Schritt**:

1. Wie man eine **Python-virtuelle Umgebung (venv)** erstellt und betritt  
2. Wie man das Projekt mit **Git und GitHub** verbindet  
3. Wie ein typischer Workflow mit **Commit & Push** aussieht  

Beispiele sind für **Windows + PowerShell** geschrieben, funktionieren aber konzeptionell auf allen Systemen ähnlich.

---

## 1. Voraussetzungen

- **Python 3** ist installiert  
  - Unter Windows kann man das mit prüfen:
    ```powershell
    py --version
    ```
- **Git** ist installiert  
  - Prüfen mit:
    ```powershell
    git --version
    ```
- Ein GitHub-Account (hier: `github.com/Megajodok`)  
- Optional: Visual Studio Code als Editor

---

## 2. Projekt lokal anlegen oder klonen

Es gibt zwei typische Startpunkte:

### Variante A: Github-Repo existiert bereits → Repo klonen (empfohlen für andere Rechner)

```powershell
cd C:\Users\DEINNAME\Desktop\PRAEDOC
git clone https://github.com/Megajodok/CLIPTest.git
cd CLIPTest
```

### Variante B: Neues Projekt lokal entwickeln und später mit GitHub verbinden

1. Ordner anlegen:
```powershell
cd C:\Users\DEINNAME\Desktop\PRAEDOC
mkdir CLIP
cd CLIP
```
2. Git-Repo initialisieren:

```poweshell
git init
```
3. (Später) mit GitHub verbinden - siehe Kapitel 4

## 3. Virtuelle Umgebung (venv) erstellen und betreten
Das hat den Vorteil, dass alle für dieses Projekt nötigen Python-Pakete auch nur für dieses Projekt installiert werden, nicht systemweit.
### 3.1 venv erstellen (windows)
```powershell
py -m venv .venv
```
Dadurch entsteht im Projektordner ein ordner `.venv/`, die virtuelle Umgebung.
### 3.2 PowerShell: Execution Policy anpassen (einmalig)
Damit PowerShell das Aktivierungsskript ausführen darf, muss man (einmal pro Benutzer) die Policy lockern:
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
```
`RemoteSigned` = Lokale Skripte dürfen ausgeführt werden
`-Scope CurrentUser` = Nur für deinen Account
`-Force` = keine Rückfragen - KEINE WIDERREDE!
### 3.3 venv aktivieren
```powershell
.\venv\Scripts\Activate
```
Wenn das klappt, sieht man im Prompt:
```powershell
(.venv) PS C:\Users\deinname\Desktop\PRAEDOC\CLIP>
```
Ab jetzt beziehen sich `python` und `pip` auf diese virtuelle Umgebung.
### 3.4 venv deaktivieren
Wenn man fertig ist:
```powershell
deactivate
```
## GitHub-Repo mit lokalem Projekt verbinden
Angenommen, auf GitHub existiert bereits ein Repo, z.B.: `https://github.com/Megajodok/CLIPTest`
Und man befindest sich in einem lokalen Projektordner:
`cd C:\Users\deinname\Desktop\PRAEDOC\CLIP`
### 4.1 `.gitignore` anlegen (wichtig!)
Damit die virtuelle Umgebung nicht mit ins Repo kommt:
```powershell
ni .gitignore
notepad .gitignore
```
Inhalt der `.gitignore`:
```
# Python
__pycache__/
*.pyc

# Virtual env
.venv/

# Sonstiges
.env
```
Datei speichern.
### 4.2 Git initialisieren (falls noch nicht passiert)
```
git init
```
### 4.3 Remote-Repo hinzufügen
```
git remote add origin https://github.com/Megajodok/CLIPTest.git
```
Prüfen:
```
git remote -v
```
Ausgabe sollte z.B. so aussehen:
```
origin  https://github.com/Megajodok/CLIPTest.git (fetch)
origin  https://github.com/Megajodok/CLIPTest.git (push)
```
### 4.4 Ersten Commit erstellen
Alle aktuellen Dateien zum Commit vormerken:
```powershell
git add .
```
Commit erstellen:
```powershell
git commit -m "Initial project setup"
```
### 4.5 Hauptbranch auf `main` setzen
```powershell
git branch -M main
```
### 4.6 Erster Push zu GitHub
```powershell
git push -u origin main
```
- Beim ersten Mal wird man nach Login / Token gefragt.
- Danach sind `main` lokal und auf GitHub verknüpft.
Wenn Git meldet, dass im Remote bereits Commits existieren (z.B. ein automatisch erstelltes README), und man seinen lokalen Stand als **Quelle der Wahrheit** verwenden will, kann man im Ausnahmefall:
```powershell
git push --force origin main
```
Vorsicht: Das überschreibt den `main`-Branch auf GitHub mit dem lokalen Stand.

## Typischer Arbeits-Workflow
Sobald das Setup steht, ist der Alltag simpel:
1. Änderungen im Code machen
2. Status prüfen:
```powershell
git status
```
3. Dateien zum Commit hinzufügen:
```powershell
git add .
```
4. Commit mit Nachricht:
```powershell
git commit -m "Beschreibe kurz, was geändert wurde"
```
5. Änderungen hochladen:
```powershell
git push
```
Auf einem anderen Rechner:
1. Repo klonen
```powershell
git clone https://github.com/Megajodok/CLIPTest.git
```
2. venv erstellen und aktivieren:
```powershell
py -m venv .venv
.\.venv\Scripts\Activate
```
3. Abhängigkeiten installieren (falls `requirements.txt` existiert):
```powershell
pip install -r requirements.txt
```
## 6. (Optional) Python-Abhängigkeiten verwalten
Wenn man später Pakete installiert, z.B.:
```powershell
pip install torch torchvision pillow
pip install git+https://github.com/openai/CLIP.git
```
kann man seinen Stand einfrieren:
```powershell
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Add requirements file"
git push
```
Auf einem anderen Rechner reicht dann:
```powershell
pip install -r requirements.txt
```
## Kurzfassung als Cheat Sheet
Einmalig pro Projekt:
```powershell
# Projektordner erstellen
mkdir CLIP
cd CLIP

# Git & venv
git init
py -m venv .venv
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force  # nur einmal nötig
.\.venv\Scripts\Activate

# .gitignore anlegen und befüllen
ni .gitignore
notepad .gitignore

# Remote verbinden
git remote add origin https://github.com/Megajodok/CLIPTest.git

# Erster Commit & Push
git add .
git commit -m "Initial project setup"
git branch -M main
git push -u origin main
```
Jeder Arbeitstag:
```powershell
cd C:\Users\deinname\Desktop\PRAEDOC\CLIP
.\.venv\Scripts\Activate

# Code ändern …

git status
git add .
git commit -m "…"
git push
```

FERTIG!
