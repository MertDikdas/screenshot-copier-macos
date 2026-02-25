# Screenshot Copier (macOS)

This is the macOS version, there is windows version too.
The purpose of the application is when you screenshot something and it saved to your clipboard, app will send it to your seconde device's clipboard.
You should download this application to both devices and one of them will be reciever and one of them will be sender.
When sender screenshot it will automaticly will send to receiver device's clipboard.
Both devices can be windows or macos it doesn't matter. Just download right git repository

---

## System Requirements

- macOS 11+
- Python 3.9+
- Git
- pip

---

## Install Git (if not installed)

Check:

```bash
git --version
```

If not installed:

```bash
xcode-select --install
```
or download from:
https://git-scm.com

## Clone the Repository
```bash
git clone https://github.com/MertDikdas/screenshot-copier-macos.git
cd screenshot-copier-macos
```
## Install Dependencies
Create a virtual environment (recommended):
```bash
python3 -m venv .venv
source venv/bin/activate
Install requirements:
pip install -r requirements.txt
```
## Run in Development Mode
```bash
python -m src.main.py
```

## Build Standalone Binary
Install PyInstaller:
```bash
pip install pyinstaller
```
Build:
```bash
pyinstaller --onefile src/main.py --name screenshot-copier --paths .
```
Output:
dist/screenshot-copier
Run:
```bash
cd dist
./screenshot-copier
```
and you can drag the dist/screenshot-copier to applications folder
