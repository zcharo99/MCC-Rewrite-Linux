from core import *
def ss_tools(minecraft_ui):
    clean = """
\033[1;39m

                         ░██████╗░██████╗░░░░░░████████╗░█████╗░░█████╗░██╗░░░░░░██████╗
                         ██╔════╝██╔════╝░░░░░░╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝
                         ╚█████╗░╚█████╗░█████╗░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░
                         ░╚═══██╗░╚═══██╗╚════╝░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗
                         ██████╔╝██████╔╝░░░░░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝
                         ╚═════╝░╚═════╝░░░░░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░
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
                                                \033[1;32m║   \033[1;39m   SS-Tools      \033[1;32m║          
                                                \033[1;39m└────────────────────┘
                                    \033[1;97mThis section has not been audited by MCC's Archive.    
                                \033[1;97mThat means that most of the things here may not working. 
                           \033[1;97mPlease report to us if you found a tools that is buggy/not working.
\033[1;31m[\033[1;39m-\033[1;31m] \033[1;32mMinecraft Section
\033[1;31m[\033[1;39m1\033[1;31m] \033[1;32mMasew Cleaner \033[1;31m[\033[1;33mUse at your own risk\033[1;31m] 
\033[1;31m[\033[1;39m2\033[1;31m] \033[1;32mKatana SS Tool \033[1;31m[\033[1;33mWorking with clickers\033[1;31m] \033[1;31m[\033[1;33mUse at your own risk\033[1;31m] 
\033[1;31m[\033[1;39m3\033[1;31m] \033[1;32mPrestige Self Destructor [\033[1;33mWorking with forge mods\033[1;31m] 
\033[1;31m[\033[1;39m4\033[1;31m] \033[1;32mValorant Spoofer \033[1;31m[\033[1;33mUse at your own risk\033[1;31m] 
\033[1;31m[\033[1;39m5\033[1;31m] \033[1;32mXelo HWID Spoofer \033[1;31m[\033[1;33mUse at your own risk\033[1;31m] \033[1;31m[\033[1;33mPassword : XELO-FREE-XhSAc\033[1;31m] 
\033[1;31m[\033[1;39m6\033[1;31m] \033[1;32mEzPing \033[1;31m[\033[1;33mUse at your own risk\033[1;31m]
\033[1;31m[\033[1;39m7\033[1;31m] \033[1;32mMighty Solutions Temp Spoofer \033[1;31m[\033[1;33mUse at your own risk\033[1;31m]
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    """


    while True:
        os.system('clear')
        print(clean)
        chon = input('                                               \033[1;39m[\033[1;31m×\033[1;39m] \033[1;39m>> ')
        if chon == '-':
            os.system('clear')
            minecraft_ui(ss_tools)
        elif chon == '1':
            webbrowser.open_new("https://cdn.discordapp.com/attachments/1148033696641859584/1171827433549336657/Masew_Cleaner.exe?ex=655e1857&is=654ba357&hm=9b7cd01dfe5d28b2b8d14c20db6209a9aa8b608085f4fa7b84a2e046896fc87d&")
        elif chon == '2':
            webbrowser.open_new("https://www.mediafire.com/file/fzkswm766mu35dz/Katana_SS_Tool.zip/file")
        elif chon == '3':
            webbrowser.open_new("https://www.mediafire.com/file/mb6o9ja40sd8fmy/Sess.zip/file")
        elif chon == '4':
            webbrowser.open_new("https://cdn.discordapp.com/attachments/1129999297857990660/1184463535108018216/Sp.zip?ex=658c10a1&is=65799ba1&hm=00c375377f32f1c47ae679a96f7078e9211fc4facf3447623f86b5bc0bc215ad&")
        elif chon == '5':
            webbrowser.open_new("https://mega.nz/file/VzMlwaxJ#pSI8kQTN3xAOXyb_ZWfJkScHVs5pLjRZZy4BTn_tHEs")
        elif chon == '6':
            webbrowser.open_new("https://www.mediafire.com/file/jg25vzubtv324dg/ezping.zip/file")
        elif chon == '7':
            os.system("start https://www.mediafire.com/file/0gcr905qpet5ybb/Mighty+Solutions+Free+temp.7z/file")

        else:
            continue
