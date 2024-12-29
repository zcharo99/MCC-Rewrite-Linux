from core import *

def windowtitle(a):
    os.system(f"title {a}")
windowtitle("MCC Loader 2.0.0")
def update():
    current_version = "2.0.0"
    version_url = "https://raw.githubusercontent.com/mcc-loader/Loader/refs/heads/main/version"

    response = requests.get(version_url)
    github_version = response.text.strip()

    if current_version != github_version:
        user_input = input("\033[1;39m[\033[0;31mMCC Loader\033[1;39m] \033[1;39mThere is a new version avalible,do you want to download? (yes/no): ").strip().lower()
        time.sleep(1)

        if user_input == "yes":
            webbrowser.open("https://github.com/mcc-loader/Loader/")
            os._exit(0)
        else:
            print("\033[1;39m[\033[0;31mMCC Loader\033[1;39m] \033[1;39mContinuing with the current version.")
            time.sleep(1)
    else:
        print("\033[1;39m[\033[0;31mMCC Loader\033[1;39m] \033[1;39mMCC Loader is up-to-date!")
        time.sleep(1)
update()
try:
    f = open('tos.txt')
except FileNotFoundError:
    display_tos()
else:
    f.close
    subprocess.check_call(["attrib", "+H", "tos.txt"])
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

