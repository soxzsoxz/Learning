import requests
import json # ต้องใช้เพราะ Discord คุยด้วยภาษา JSON
import time
import os # เรียกใช้โมดูลระบบ
from dotenv import load_dotenv # เรียกตัวช่วยอ่าน .env

load_dotenv()

# เอา URL ยาวๆ ที่ Copy มาวางตรงนี้
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_URL")

def send_discord_notify(message):
    """ส่งข้อความเข้า Discord"""
    
    # Discord รับข้อมูลเป็น JSON 
    payload = {
        "content": message
    }
    
    try:
        # สังเกต: เปลี่ยนจาก data=... เป็น json=...
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        
        # Discord ถ้าสำเร็จมักจะตอบ 204 (No Content) หรือ 200
        if response.status_code in [200, 204]:
            print("✅ ส่ง Discord สำเร็จ!")
        else:
            print(f"❌ ส่งไม่ไป: {response.status_code}")
            print(response.text) # ปริ้นดูหน่อยว่าเขาด่าว่าอะไร
            
    except Exception as e:
        print(f"Discord Error: {e}")

def get_bitcoin_price():
    """ดึงราคา Bitcoin ทั้ง THB และ USD ในครั้งเดียว"""
    # สังเกตตรง vs_currencies=thb,usd (ขอทีเดียว 2 หน่วย)
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=thb,usd"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            
            # --- จุดที่แก้: เจาะเข้าไปเอาข้อมูลให้ถูกชั้น ---
            # data คือ {'bitcoin': {'thb': 3xxxxxx, 'usd': 9xxxx}}
            price_thb = data['bitcoin']['thb']
            price_usd = data['bitcoin']['usd']
            
            # ส่งค่ากลับไป 2 ตัวพร้อมกัน (Tuple)
            return price_thb, price_usd
        else:
            print("Server Error:", response.status_code)
            return None, None
    except Exception as e:
        print(f"Internet Error: {e}")
        return None, None
    
# --- Main Loop ---
print("🚀 เริ่มต้นดึงราคา Bitcoin Real-time (กด Ctrl+C เพื่อหยุด)...")

while True:
    # รับค่า 2 ตัวที่ส่งกลับมา
    thb, usd = get_bitcoin_price()
    
    if thb and usd:
        # \033[92m คือรหัสสีเขียว (ให้ดูเท่ๆ), \033[0m คือล้างสี
        send_discord_notify(f"💰 BTC: {thb:,.0f} THB | {usd:,.2f} USD")
    else:
        print("❌ เกิดข้อผิดพลาด")
    
    time.sleep(10) # รอ 5 วินาที