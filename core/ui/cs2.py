from core import *
from core.ui.csgo import *
def cs2(main_ui):
       mine = """\033[1;39m

                                                        ░█████╗░░██████╗██████╗░
                                                        ██╔══██╗██╔════╝╚════██╗
                                                        ██║░░╚═╝╚█████╗░░░███╔═╝
                                                        ██║░░██╗░╚═══██╗██╔══╝░░
                                                        ╚█████╔╝██████╔╝███████╗
                                                        ░╚════╝░╚═════╝░╚══════╝
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
                                                \033[1;39m┌────────────────────┐         
                                                \033[1;32m║        \033[1;39mFREE        \033[1;32m║          
                                                \033[1;39m└────────────────────┘          
\033[1;31m[\033[1;39m1.1\033[1;31m] \033[1;32mPassathook
\033[1;31m[\033[1;39m1.2\033[1;31m] \033[1;32manyx.gg
\033[1;31m[\033[1;39m1.3\033[1;31m] \033[1;32mAimWare CS2 \033[1;31m[\033[1;33mupdated23/12/24\033[1;31m]
\033[1;31m[\033[1;39m1.4\033[1;31m] \033[1;32mSirius \033[1;31m[\033[1;33mpasted af\033[1;31m]
\033[1;31m[\033[1;39m1.5\033[1;31m] \033[1;32mVoidWare
\033[1;31m[\033[1;39m1.6\033[1;31m] \033[1;32mXenon
\033[1;31m[\033[1;39m1.7\033[1;31m] \033[1;32mPlagueCheat 
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
\033[1;31m[\033[1;39m-\033[1;31m] \033[1;32mBack to cs:go page

"""
       while True:
           os.system('clear')
           print(mine)
           chon = input('                                               \033[1;39m[\033[1;31m×\033[1;39m] \033[1;39m>> ')
           if chon == '-':
               os.system('clear')
               csgo(main_ui)
           elif chon == '1.1':
               webbrowser.open_new("https://github.com/JannesBonk/PassatHook")
           elif chon == '1.2':
               webbrowser.open_new("https://www.anyx.gg/")
           elif chon == '1.3':
               webbrowser.open_new("https://workupload.com/file/KpwtfnnSgtG")
           elif chon == '1.4':
               webbrowser.open_new("https://workupload.com/file/Uvjh3qe3LM6")
           elif chon == '1.5':
               webbrowser.open_new("https://workupload.com/file/G46sz5ACp4f")
           elif chon == '1.6':
               webbrowser.open_new("https://workupload.com/file/gPZURyFKJNA")
           elif chon == '1.7':
               webbrowser.open_new("https://workupload.com/file/VzSSbYShNw2")

           else:
               continue
