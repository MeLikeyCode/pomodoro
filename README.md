# Pomodoro
A distraction-free pomodoro timer that helps you stay focused.
- runs in the system tray
- shows notifications when its time to work or take a break
- plays study/work music in the background (no browser/music player winows or even an internet connection needed while you work anymore)
- keeps track of time worked (and time spent taking breaks) in a *local* log file so you can see your habbits

Installation is easy, just download the installer (see [releases](https://github.com/MeLikeyCode/pomodoro/releases)) and run it.

Currently this app only works on windows, but if you are a linux/mac user and wanna use this, create an issue on the github repo and I'll make it happen.

If you are a developer, see the `docs` folder, in particular `docs/developer_notes.md`.

# Screenshots
![](/docs/screenshots/initial.png)

![](/docs/screenshots/started.png)

![](/docs/screenshots/tray_menu.png)

![](/docs/screenshots/tray_break.png)

![](/docs/screenshots/tray_work.png)

# Motivation
The motivation for creating this app came about because I was looking for a pomodor timer that **did not need to have a window up all the time**, one that just stayed out of your way and notified you when it was time to work, break, etc.

I was not able to find such a timer, so I created my own.

I also like to listen to music (study music) when I'm working, but having to open up a browser just to play some music opens a whole can of distraction-worms. So I added the ability for my app to play study music in the background, without any distracting windows up!

Furthermore, I like to review my habbits and such, so I made the app record the amount of time you work/break, in a *local* file, no one except you will see it.

# Credits
- First, thanks a **whole bunch** to all the amazong people who contributed to the open source libraries, tools, IDEs, etc that were used to create this app
    - namely python, plyer, pystray, customtkinter, PIL, pygame, anaconda, pyinstaller, and NSIS
- images
    - tomato icon created by **Freepik**, [hosted on Flaticom.com](https://www.flaticon.com/free-icons/tomato)
    - play icon created by **Bingge Liu**, [hosted on Flaticon.com](https://www.flaticon.com/free-icons/video)
    - stop icon created by **moogun**, [hosted on Flaticon.com](https://www.flaticon.com/free-icons/stop)
    - hamburger icon created by **Lizel Arina**, [hosted on Flaticon.com](https://www.flaticon.com/free-icons/hamburger) (TODO if hamburger is not used, remove)
