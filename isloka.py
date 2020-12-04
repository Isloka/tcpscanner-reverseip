import requests

apikey = '' # If you do not have one, leave it blank, it will automatically use the free mode.

print('\n[!] Made by Isloka\n[!] Simple TCPScanner & Reverse IP Lookup\n')

victim = input('[?] IP > ')

def free():
    print('[+] TCPScan: Fetching for the scan results...\n')
    tcpscan = requests.get('https://api.hackertarget.com/nmap/?q='+victim)
    print('-----------------------------------------------------------------\n'+tcpscan.text+'-----------------------------------------------------------------\n')

    print('[+] ReverseIP: Fetching for the domains...\n')
    reverseip = requests.get('https://api.hackertarget.com/reverseiplookup/?q='+victim)
    print('-----------------------------------------------------------------\n'+reverseip.text+'\n-----------------------------------------------------------------\n')
def api():
    print('[+] TCPScan: Fetching for the scan results...\n')
    tcpscan = requests.get('https://api.hackertarget.com/nmap/?q='+victim)
    print('-----------------------------------------------------------------\n'+tcpscan.text+'-----------------------------------------------------------------\n')

    print('[+] ReverseIP: Fetching for the domains...\n')
    reverseip = requests.get('https://api.hackertarget.com/reverseiplookup/?q='+victim+'&apikey='+apikey)
    print('-----------------------------------------------------------------\n'+reverseip.text+'\n-----------------------------------------------------------------\n')

if apikey != '':
    print('[+] API Key detected! Using PAID mode...')
    api()
else:
    print('[+] No API Key detected! Using FREE mode...')
    free()
