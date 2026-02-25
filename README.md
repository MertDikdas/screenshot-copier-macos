# 📸 Screenshot Copier (macOS)

A lightweight command-line tool that processes screenshots and copies them directly to the macOS clipboard.

---

## 🧰 System Requirements

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
git clone https://github.com/yourusername/screenshot-copier.git
cd screenshot-copier
```
## Install Dependencies
Create a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate
Install requirements:
pip install -r requirements.txt
```
## Run in Development Mode
```bash
python -m src/main.py
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