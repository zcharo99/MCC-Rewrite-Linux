from core import *

current_version = "2.0.0"

def windowtitle(a):
    sys.stdout.write(f"\033]0;{a}\007")
    sys.stdout.flush()
windowtitle(f"MCC Loader {current_version}")
def update():
    official_ver_url = "https://raw.githubusercontent.com/mcc-loader/Loader/refs/heads/main/version"
    version_url = "https://raw.githubusercontent.com/zcharo99/MCC-Rewrite-Linux/refs/heads/main/version"

    official_response = requests.get(official_ver_url)
    response = requests.get(version_url)
    if official_response != response:
        print("\033[1;39m[\033[0;31mMCC Loader\033[1;39m] \033[1;39mFork version mismatch. Please report this error. Continuing in 5 seconds.")
        time.sleep(5)

    github_version = response.text.strip()

    if current_version != github_version:
        user_input = input("\033[1;39m[\033[0;31mMCC Loader\033[1;39m] \033[1;39mThere is a new version avalible,do you want to download? (yes/no): ").strip().lower()
        time.sleep(1)

        if user_input == "yes":
            webbrowser.open("https://github.com/zcharo99/MCC-Rewrite-Linux")
            os._exit(0)
        else:
            print("\033[1;39m[\033[0;31mMCC Loader\033[1;39m] \033[1;39mContinuing with the current version.")
            time.sleep(1)
    else:
        print("\033[1;39m[\033[0;31mMCC Loader\033[1;39m] \033[1;39mMCC Loader is up-to-date!")
        time.sleep(1)
update()
try:
    f = os.open("tos.txt", os.O_RDONLY)
except FileNotFoundError:
    display_tos()
else:
    os.close(f)
    os.rename("tos.txt", ".tos.txt")
banner = f"""                                      You have accepted MCC Loader's terms of service.

                 ███╗░░░███╗░█████╗░░█████╗░██╗░██████╗  ░█████╗░██████╗░░█████╗░██╗░░██╗██╗██╗░░░██╗███████╗
                 ████╗░████║██╔══██╗██╔══██╗╚█║██╔════╝  ██╔══██╗██╔══██╗██╔══██╗██║░░██║██║██║░░░██║██╔════╝
                 ██╔████╔██║██║░░╚═╝██║░░╚═╝░╚╝╚█████╗░  ███████║██████╔╝██║░░╚═╝███████║██║╚██╗░██╔╝█████╗░░
                 ██║╚██╔╝██║██║░░██╗██║░░██╗░░░░╚═══██╗  ██╔══██║██╔══██╗██║░░██╗██╔══██║██║░╚████╔╝░██╔══╝░░
                 ██║░╚═╝░██║╚█████╔╝╚█████╔╝░░░██████╔╝  ██║░░██║██║░░██║╚█████╔╝██║░░██║██║░░╚██╔╝░░███████╗
                 ╚═╝░░░░░╚═╝░╚════╝░░╚════╝░░░░╚═════╝░  ╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚══════╝

                                                Press ENTER to continue.                                                                     
"""[1:]
Anime.Fade(Center.Center(banner), Colors.black_to_white, Colorate.Vertical, enter=True)

main_ui(minecraft_ui)

