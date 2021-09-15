

import requests

print(
    """
                       _                                    
 _   _ ______ _ _   _| | __ _  ___ _ __      __  _____ ___ 
| | | |_  / _` | | | | |/ _` |/ _ \ '_ \ ____\ \/ / __/ __|
| |_| |/ / (_| | |_| | | (_| |  __/ | | |_____>  <\__ \__ \
 \__,_/___\__,_|\__, |_|\__, |\___|_| |_|    /_/\_\___/___/
                |___/   |___/                              
    """
)


hedef_site = input("Hedef site giriniz:")
site = ("http://" + hedef_site + "/index.php?q=")
txt = open("payload.txt", "r")
pay = txt.read()
txt.close()
for payloads in pay.splitlines():
    istek = requests.post(site + payloads)

    if payloads in istek.text:
        print("XSS açığı bulundu")
        print("İşlenen Payload:" + payloads)
        break
    else:
        print("XSS bulunamadı.")
