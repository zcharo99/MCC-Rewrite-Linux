from core import *
from core.ui.minecraft import *
def credits(main_ui):
    banner = """


                                   ██████╗██████╗ ███████╗██████╗ ██╗████████╗███████╗
                                  ██╔════╝██╔══██╗██╔════╝██╔══██╗██║╚══██╔══╝██╔════╝
                                  ██║     ██████╔╝█████╗  ██║  ██║██║   ██║   ███████╗
                                  ██║     ██╔══██╗██╔══╝  ██║  ██║██║   ██║   ╚════██║
                                  ╚██████╗██║  ██║███████╗██████╔╝██║   ██║   ███████║
                                   ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝   ╚═╝   ╚══════╝


                                 | luvsy's crib (https://discord.gg/luvsy)           |
                                 | Infinity Stuff (https://discord.gg/qvktQFtBsT)    |
                                 | fled. (https://discord.gg/epaxz643eE)             |
                                 | Ghost (https://discord.gg/UHBK3J8kfG)             |
                                 | WonderLand Library (https://discord.gg/pcsRpEDB6Z)| 
                                 | CookieAC (https://discord.gg/hey6PE5CWE)          |
                                 | Mimhax (mimhax.netlify.app)                       |
                                 | Trillium INC. (https://discord.gg/VF473pGEV5)     |
                                 | Splash Software (https://discord.gg/GUw9bwuWrm)   |
                                 | hvh.net (https://hackvshack.net)                  |
                                 | HydraReverse (t.me/hydrareverse)                  |
                                 | Anon-Team (https://t.me/anonteam1337)             |
                                 | JohnXina (https://johnspecial.ydns.eu)            |


                              Report to us if you found any invite link here not working.
                                             Press any key to return.
    """
    
    Anime.Fade(banner, Colors.white_to_black, Colorate.Vertical, enter=True)
    os.system('clear')
    print("Leaving Credit")
    main_ui(minecraft_ui)
