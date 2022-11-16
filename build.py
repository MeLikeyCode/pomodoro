import shutil
import subprocess
import argparse
import glob


description = """Package as standalone executable and dependent files (dlls, images, config files, etc)."""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=description)
    args = parser.parse_args()

    # find out location of customtkinter
    pip = subprocess.run(
        ["pip", "show", "customtkinter"], stdout=subprocess.PIPE, check=True
    )
    for v in pip.stdout.decode().splitlines():
        if v.startswith("Location:"):
            ctk_dir = v[10:]

    # run pyinstaller
    subprocess.run(
        [
            "pyinstaller",
            "--name=pomodoro",
            "--icon=tomato.ico",
            "--hidden-import",
            "plyer.platforms.win.notification",
            "--noconfirm",
            "--onedir",
            "--windowed",
            "--add-data",
            f"{ctk_dir}\customtkinter;customtkinter",
            "main.py",
        ],
        check=True,
    )

    # copy images/config files
    for v in glob.glob("*.png"):
        shutil.copy(v, "dist/pomodoro")
    for v in glob.glob("*.ico"):
        shutil.copy(v, "dist/pomodoro")
    shutil.copy("settings.json", "dist/pomodoro")
        