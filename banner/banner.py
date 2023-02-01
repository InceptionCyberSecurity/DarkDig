
class Banner(object):
    def LoadDarkdumpBanner(self):
        try:
            from termcolor import cprint, colored
            banner = '''

          ___           _   ___  _
         |   \ __ _ _ _| |_|   \(_)__ _
         | |) / _` | '_| / / |) | / _` |
         |___/\__,_|_| |_\_\___/|_\__, |
                          |___/

          Developed By: Josh Schiavone & Nat Jones
https://github.com/josh0xA and https://github.com/ArcadeusOPS/DarkDig
                       Version: 2.1
                          '''

            cprint(banner, 'magenta', attrs=['bold'])

        except ImportError as ie:
            print(banner)
