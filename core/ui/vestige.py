from core import *
def vestige(minecraft_ui):
  ves = """\033[1;39m

                              ██╗░░░██╗███████╗░██████╗████████╗██╗░██████╗░███████╗
                              ██║░░░██║██╔════╝██╔════╝╚══██╔══╝██║██╔════╝░██╔════╝
                              ╚██╗░██╔╝█████╗░░╚█████╗░░░░██║░░░██║██║░░██╗░█████╗░░
                              ░╚████╔╝░██╔══╝░░░╚═══██╗░░░██║░░░██║██║░░╚██╗██╔══╝░░
                              ░░╚██╔╝░░███████╗██████╔╝░░░██║░░░██║╚██████╔╝███████╗
                              ░░░╚═╝░░░╚══════╝╚═════╝░░░░╚═╝░░░╚═╝░╚═════╝░╚══════╝
\033[1;39m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;39m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
       \033[1;39m┌─────────────────────────────────────────── Archive ────────────────────────────────────────────┐            
       \033[1;32m║                           \033[1;39m  Version          : \033[1;30m 2.0.0                                          \033[1;32m║
       \033[1;32m║                           \033[1;39m  Discord          : \033[1;34m discord.gg/chiterl                             \033[1;32m║
       \033[1;32m║                           \033[1;39m  Source           : \033[1;33m github.com/mcc-loader/Loader                   \033[1;32m║
       \033[1;32m║                           \033[1;39m  Loader Plan      : \033[1;32m Free                                           \033[1;32m║
       \033[1;39m└────────────────────────────────────────────────────────────────────────────────────────────────┘
 \033[0;31m                               Create a ticket if u found a client that not working.
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
                                            \033[1;39m┌─────────────────────┐         
                                            \033[1;32m║    \033[1;39m   Vestige       \033[1;32m║          
                                            \033[1;39m└─────────────────────┘          
\033[1;31m[\033[1;39m-\033[1;31m] \033[1;32mBack to previous page 
\033[1;31m[\033[1;39m1.9.5\033[1;31m] \033[1;32mVestige \033[1;31m[\033[1;33mv1.9.5\033[1;31m] 
\033[1;31m[\033[1;39m2.0.2\033[1;31m] \033[1;32mVestige \033[1;31m[\033[1;33mv2.0.2\033[1;31m] 
\033[1;31m[\033[1;39m3.0\033[1;31m] \033[1;32mVestige \033[1;31m[\033[1;33mv3.0\033[1;31m] 
\033[1;31m[\033[1;39mVR\033[1;31m] \033[1;32mVestige Reborn
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
"""

  while True:
    os.system('clear')
    print(ves)
    chon = input('                                               \033[1;39m[\033[1;31m×\033[1;39m] \033[1;39m>> ')
    if chon == '-':
        os.system('clear')
        minecraft_ui(vestige)
    elif chon == '1.9.5':
        webbrowser.open_new("https://www.mediafire.com/file/fowj4gm0k6a67ey/Vestige_1.9.5.zip/file")
    elif chon == '2.0.2':
        webbrowser.open_new("https://www.mediafire.com/file/7q25p9jm42j3v4z/Vestige+2.0.2.zip/file")
    elif chon == '3.0':
        webbrowser.open_new("https://www.mediafire.com/file/hdt5u3i5wibo67h/Vestige+3.0.zip/file")
    elif chon == 'VR':
        webbrowser.open_new("https://www.mediafire.com/file/q3bubemjy14yx0s/Vestige_Reborn.zip/file")
    else:
        continue
