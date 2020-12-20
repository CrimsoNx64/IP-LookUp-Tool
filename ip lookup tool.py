#   _____      _                     _   _ 
#  / ____|    (_)                   | \ | |
# | |     _ __ _ _ __ ___  ___  ___ |  \| |
# | |    | '__| | '_ ` _ \/ __|/ _ \| . ` |
# | |____| |  | | | | | | \__ \ (_) | |\  |
#  \_____|_|  |_|_| |_| |_|___/\___/|_| \_|

#IP lookup tool

import webbrowser

ip=input("Enter the IP: ")

url="https://whatismyipaddress.com/ip/"+ip#website link + the ip user inputted

webbrowser.open(url)#opens new link
