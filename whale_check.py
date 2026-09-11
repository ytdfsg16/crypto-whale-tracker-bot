import requests
import time

BOT_TOKEN = "8723594713:AAEsk_1uAakk8snHN5A1XlLRFyKZPMcRqM4"
CHAT_ID = "5430532673"
WALLET_ADDRESS = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"

def send_telegram_msg(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"}
    try:
        res = requests.post(url, json=payload).json()
        if res.get("ok"):
            print("[+] Auto-Report delivered to Telegram!")
        else:
            print("[-] Telegram Error:", res.get("description"))
    except Exception as e:
        print("[-] Connection Error:", e)

def check_and_alert():
    print("🚀 Whale & Price Monitoring Bot Started...")
    send_telegram_msg("🤖 *Bot Started!* Monitoring ETH prices & Whale activities...")
    
    while True:
        try:
            eth_url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
            res = requests.get(eth_url).json()
            price = res['ethereum']['usd']
            
            report = (
                f"📊 *Live Market Update*\n\n"
                f"🎯 *Target Wallet:* `{WALLET_ADDRESS[:10]}...` \n"
                f"💵 *ETH Current Price:* `${price}`\n"
                f"⏰ *Status:* Active Monitoring"
            )
            
            send_telegram_msg(report)
            
            # الانتظار لمدة 60 ثانية قبل الفحص التالي (يمكنك تغيير الرقم لاحقاً)
            time.sleep(60)
            
        except Exception as e:
            print("Error in loop:", e)
            time.sleep(10)

if __name__ == "__main__":
    check_and_alert()

