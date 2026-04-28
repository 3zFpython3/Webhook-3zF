import requests
import os

# ألوان
G = "\033[92m"   # أخضر
R = "\033[91m"   # أحمر
Y = "\033[93m"   # أصفر
B = "\033[94m"   # أزرق

os.system("clear")

print(G + r"""
██████╗ ███████╗███████╗
╚════██╗╚══███╔╝██╔════╝
 █████╔╝  ███╔╝ █████╗
██╔═══╝  ███╔╝  ██╔══╝
███████╗███████╗██║
╚══════╝╚══════╝╚═╝

═══════ 3zF WEBHOOK TOOL ═══════
Fast • Simple • Powerful
""")

print(Y + "\n══════════════════════════════")
print("        Webhook Sender        ")
print("══════════════════════════════\n")

webhook = input(G + "[+] Webhook URL : ")
username = input(B + "[+] Username    : ")
message = input(Y + "[+] Message     : ")

data = {
    "content": message,
    "username": username
}

try:
    r = requests.post(webhook, json=data)

    if r.status_code in [200, 204]:
        print(G + "\n[✓] Sent Successfully")
    else:
        print(R + f"\n[✗] Failed | Status: {r.status_code}")

except Exception as e:
    print(R + f"\n[!] Error: {e}")
