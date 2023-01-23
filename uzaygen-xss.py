from colorama import Fore, Style
import requests
import urllib.parses

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
#URL geçerli mi kontrol et
if urllib.parse.urlparse(hedef_site).scheme == '':
    hedef_site = 'http://' + hedef_site
site = (hedef_site + "/index.php?q=")

txt = open("xssPayloads.txt", "r",encoding='utf-8')
pay = txt.read()
txt.close()

payload_count = len(pay.splitlines())
processed_count = 0

for payloads in pay.splitlines():
    processed_count +=1
    istek = requests.post(site + payloads, timeout=5)
    if payloads in istek.text:
        print(Fore.YELLOW + "XSS açığı bulundu" + Style.RESET_ALL)
        print(Fore.YELLOW + "İşlenen Payload:" + payloads + Style.RESET_ALL)
        print(Fore.YELLOW + "Açık bulunan yer:" + site + payloads + Style.RESET_ALL)
        print(Fore.YELLOW + "Sömürülebilir:" + "kullanıcının girdiği veri siteye javascript kodu olarak gönderilir." + Style.RESET_ALL)
        break
    else:
        if processed_count == payload_count:
            print(Fore.RED + "XSS bulunamadı." + Style.RESET_ALL)
        else:
            print(Fore.RED + "XSS bulunamadı. {}/{} payload işlendi.".format(processed_count,payload_count) + Style.RESET_ALL)
