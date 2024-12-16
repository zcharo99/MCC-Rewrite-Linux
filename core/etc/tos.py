from core import *
from core.ui.main_ui import main_ui
from core.ui.minecraft import *
TOS = """



                                               \033[0;31m _       _____    __________
                                               \033[0;31m| |     / /   |  /  _/_  __/
                                               \033[0;31m| | /| / / /| |  / /  / /   
                                               \033[0;31m| |/ |/ / ___ |_/ /  / /    
                                               \033[0;31m|__/|__/_/  |_/___/ /_(_)
"""
TOS2 = """                  Before using MCC Loader, you must agree to our \033[0;31mTOS\033[1;39m.
                                    
              Only press enter if you want to see the \033[0;31mterms of service\033[1;39m."""[1:]
def display_tos():
    def confirm():
        Anime.Fade(Center.Center(TOS2), Colors.white_to_red, Colorate.Vertical, enter=True)

    os.system('cls')
    print(TOS)
    time.sleep(1)
    print("\033[1;39m[\033[0;31mMCC Loader\033[1;39m] \033[1;39mThe user hasn't accepted MCC Loader's terms of service.")
    time.sleep(1)
    print("\033[1;39m[\033[0;31mMCC Loader\033[1;39m] \033[1;39mRedirecting user to : \033[0;31mTOSArea.")
    time.sleep(3)
    os.system('cls')
    print(TOS2)
    confirm()

    if True:
        accept_tos(minecraft_ui)
def accept_tos(minecraft_ui):
    os.system('cls')

    confirmation = print("\033[1;31m                                Press any key only when you agree and understand the TOS.")
    
    TOS = print(Box.Lines("MCC's Archive Terms of Service (TOS)"))
    
    banner = f"""
              The term "We" refers to the entire Developer/Owner of MCC's Archive and MCC's Archive as a whole, 
                   while "You" refers to you as the user and person using the products of MCC's Archive.

     You need to ensure that you voluntarily download/use MCC Loader without any coercion from anyone/a third party.
  "Someone/a third party" here mainly refers to the cases You are asked by a server/stranger to start this application.

            By pressing continue(enter), you agree that you will not use MCC Loader in particular/MCC's Archive
                                products in general for commercial purposes(eg selling).

             You must also accept that you will be solely responsible for all situations/cases that MAY occur
               to your device during/after the period of using the PRODUCTS IN MCC Loader. (Not the loader.)

            At the same time, we will maintain and ensure the safety of all users when using MCC Loader and any 
 participation/influence on our actions may result in a PERMANENT BAN OF HWID of the person who committed the above act.

            By continuing to use any products maintained by MCC's Archive, you voluntarily agree to be bound 
                                by the most current version of the Terms of Service.
    """[1:]
    
    Write.Print(banner, Colors.white_to_green, interval=0.00025)
    msvcrt.getch()

    open("TOSVDOIAHWOIHSAKLFHWA.txt", "w").write("""This user has accepted MCC's Archive's terms of service.""")
    main_ui(minecraft_ui)