# Screenshot Copier (macOS)

This is the macOS version of Screenshot Copier.
There is also a Windows version available.
The purpose of the application is simple:
When you take a screenshot on one device, the app automatically sends it to your second device's clipboard.
You must install this application on both devices.
One device will act as the Sender
The other device will act as the Receiver
When the sender takes a screenshot, it will automatically be transferred to the receiver’s clipboard.
Both devices can be:
Windows
macOS
It does not matter — just make sure you download the correct repository version for your operating system.

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
source .venv/bin/activate
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
