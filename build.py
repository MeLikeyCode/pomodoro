import shutil
import subprocess
import argparse
import os


description = """Package everything in an installer."""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=description)
    args = parser.parse_args()

    # get directory the script is in
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # find out location of customtkinter
    pip = subprocess.run(
        ["pip", "show", "customtkinter"], stdout=subprocess.PIPE, check=True
    )
    for v in pip.stdout.decode().splitlines():
        if v.startswith("Location:"):
            ctk_dir = v[10:]

    os.chdir(script_dir)

    # run pyinstaller, will create folder dist/pomodoro
    subprocess.run(
        [
            "pyinstaller",
            "--name=pomodoro",
            "--icon=images/tomato.ico",
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
    shutil.copytree("images", "dist/pomodoro/images")
    shutil.copy("settings.json", "dist/pomodoro")

    # create installer
    subprocess.run('makensis build_installer.nsi', shell=True, check=True)

        