from core import *
from core.etc.credits import *  
from core.ui.minecraft import *
from core.ui.csgo import *
from core.ui.cs2 import *

def main_ui(minecraft_ui):
    nig = """
                                                 \033[1;39mMCC Loader is FREE.

            \033[1;32m\033[1;39mWhat's new in MCC Loader 1.0.8 ? Checkout new feature & cheats here : discord.gg/chiterl


                          \033[1;36m______  ___________________   ______              _________            
                          \033[1;36m___   |/  /_  ____/_  ____/   ___  / ____________ ______  /____________
                          \033[1;36m__  /|_/ /_  /    _  /        __  /  _  __ \  __ `/  __  /_  _ \_  ___/
                          \033[1;36m_  /  / / / /___  / /___      _  /___/ /_/ / /_/ // /_/ / /  __/  /    
                          \033[1;36m/_/  /_/  \____/  \____/      /_____/\____/\__,_/ \__,_/  \___//_/                                                                            


                                                         \033[1;31m[\033[1;39mC\033[1;31m]
\033[1;39m                                                    \033[1;35m For credits.
   \033[0;31m                                            Choose your favourite game. 


                                 \033[1;31m[\033[1;39m1\033[1;31m] \033[1;32mMinecraft           \033[1;31m[\033[1;39m2\033[1;31m] \033[1;32mCS:GO           \033[1;31m[\033[1;39m3\033[1;31m] \033[1;32mCS2
    """
    print(nig)
    while True:
        os.system('clear')
        print(nig)
        chon = Write.Input("           [×] >>  ", Colors.red_to_purple, interval=0.0025)
        
        if chon == '1':
            print("                                              \033[1;39mLoading Minecraft Page..")
            os.system('clear')
            minecraft_ui(main_ui)
        if chon == '2':
            print("                                              \033[1;39mLoading CS:GO Page..")
            os.system('clear')
            csgo(main_ui)
        if chon == '3':
            print("                                              \033[1;39mLoading CS2 Page..")
            os.system('clear')
            cs2(main_ui)
        elif chon == 'c' or chon == 'C':
            print("                                                  \033[1;39mRendering Credits..")
            os.system('clear')
            credits(main_ui)
        
        else:
            continue
